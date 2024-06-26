from openai import OpenAI
from sacrebleu.metrics import BLEU
from Classes.Model.Embedder import Embedder
from Classes.Helpers.ORCAInputFileManipulator import ORCAInputFileManipulator
from Classes.Helpers.ORCAManualManipulator import ORCAManualManipulator
from Classes.Helpers.ORCARunner import ORCARunner
import re
import os


class Tester:
    """
    Tester class for evaluating GPT-3.5 model performance on predicting input files for ORCA calculations.

    Parameters:
        model (str): The GPT model identifier.
        data (list): List of tuples containing prompts and corresponding input files.
        system_prompt (str): System prompt used during GPT completion.
        eval_file_path (str): File path to store evaluation metrics.
        output_file_path (str): File path to store output prompts and full outputs.
        metrics (list): List of metrics to compute if not provided.
        use_embeddings (bool): Flag indicating whether to use RAG.
        client (OpenAI): OpenAI API client instance.
        naive_bleu (BLEU): BLEU instance for naive scoring with ordered n-grams.
        naive_bleu_unordered (BLEU): BLEU instance for naive scoring with unordered n-grams.
    """

    def __init__(self, model, data, system_prompt, eval_file_path, output_file_path, metrics=None, use_embeddings=False):
        self.client = OpenAI()
        self.system_prompt = system_prompt
        self.model = model
        self.data = data
        self.eval_file_path = eval_file_path
        self.output_file_path = output_file_path
        self.metrics = ["run_succesful", "naive_bleu", "bleu_vocab_overlap", "total_f1", "total_precision", "total_recall",
                        "kw_f1", "kw_precision", "kw_recall",
                        "option_f1", "option_precision", "option_recall",
                        "setting_f1", "settings_precision", "settings_recall"] if metrics is None else metrics
        self.naive_bleu = BLEU(smooth_method="floor", effective_order=True)
        self.naive_bleu_unordered = BLEU(
            max_ngram_order=1, effective_order=True)
        self.use_embeddings = use_embeddings

    def test(self):
        """
        Runs the testing process using the GPT model to predict input files, evaluates predictions, 
        and writes evaluation metrics and outputs to files.
        """
        with open(self.eval_file_path, 'a', encoding='utf-8') as f:
            f.write(",".join(self.metrics))

        for i, (prompt, input_file) in enumerate(self.data):
            if self.use_embeddings:
                prompt = Embedder.add_relevant_context_to_prompt(model='gpt-3.5-turbo',
                                                                 system_prompt=self.system_prompt,
                                                                 prompt=prompt,
                                                                 embedding_folder=os.path.join(
                                                                     "Data", "Documents", "Embedded", "index_merged"),
                                                                 k=1,
                                                                 token_limit=15000)
            # Lower, remove whitespace  like we did with training data
            predicted_input_file, full_output = self.predict_input_file_with_gpt(
                prompt)
            predicted_input_file = predicted_input_file.lower()
            predicted_input_file = self.remove_unnecessary_empty_lines(
                input_file=predicted_input_file)

            metrics = self.compute_evaluation_metrics(
                input_file, predicted_input_file)

            with open(self.eval_file_path, 'a', encoding='utf-8') as f:
                f.write("\n")
                f.write(",".join(metrics))

            with open(self.output_file_path, 'a', encoding='utf-8') as f:
                f.write("---PROMPT---\n")
                f.write(prompt)
                f.write("\n---OUTPUT---\n")
                f.write(full_output)
                f.write("\n")
                f.write("---END---")
                f.write("\n")

    def predict_input_file_with_gpt(self, user_prompt):
        """
        Uses GPT model to predict input file content based on user prompt.

        Returns:
            tuple: Tuple containing predicted input file content and full output message.
        """
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        )
        message = completion.choices[0].message.content
        matches = re.findall(r"```(.*?)```", message, flags=re.DOTALL)

        try:
            # It's possible that this is in the code block of gpt
            match = matches[-1].replace('plaintext', '')
            return match, message
        except:
            try:
                return ORCAManualManipulator.extract_processed_input_files_wo_xyz(message)[-1], message
            except:
                return "", message

    def compute_evaluation_metrics(self, reference_input_file, predicted_input_file):
        """
        Computes evaluation metrics comparing reference and predicted input files.

        Returns:
            list: List of computed evaluation metrics.
        """
        orca_run_folder = os.path.join('Data', 'Generated', 'Evaluation')
        input_file_name = "predicted.inp"
        with open(os.path.join(orca_run_folder, input_file_name), 'w', encoding='utf-8') as f:
            f.write(ORCAInputFileManipulator.add_xyz(predicted_input_file,
                    molecule_type='Molecules', molecule_file='O.txt'))  # add H20 for ease of running
        return_code = ORCARunner.run_orca(orca_run_folder,
                                          input_file_name, 'Orca Output', r"C:\Users\Pieter\Orca\orca.exe")
        runnable = 1 if return_code == 0 else 0
        # runnable=1
        reference_keywords, _ = ORCAInputFileManipulator.extract_keywords(
            reference_input_file)
        predicted_keywords, _ = ORCAInputFileManipulator.extract_keywords(
            predicted_input_file)
        _, reference_input_block_options, reference_input_block_settings = ORCAInputFileManipulator.extract_input_blocks(
            reference_input_file)
        _, predicted_input_block_options, predicted_input_block_settings = ORCAInputFileManipulator.extract_input_blocks(
            predicted_input_file)

        # Mark the options with an % to make sure that the evaluation does not count a keyword with the same name as an option
        # correct (when for instance the model predicts %uno when UNO is supposed to be a keyword)
        reference_input_block_options = [
            f'%{option}' for option in reference_input_block_options]
        predicted_input_block_options = [
            f'%{option}' for option in predicted_input_block_options]

        reference_input_block_settings = [setting for setting_block in reference_input_block_settings for setting in setting_block.strip(
        ).split("\n")]  # get every setting line as an entry
        predicted_input_block_settings = [setting for setting_block in predicted_input_block_settings for setting in setting_block.strip(
        ).split("\n")]  # get every setting line as an entry

        # same reason as mentioned before, now for the settings
        reference_settings = [f"={"=".join(setting.split())}" for setting in "\n".join(
            reference_input_block_settings).split("\n") if setting != '']
        predicted_settings = [f"={"=".join(setting.split())}" for setting in "\n".join(
            predicted_input_block_settings).split("\n") if setting != '']

        naive_bleu = self.naive_bleu.sentence_score(hypothesis=re.sub(
            r"![/s]*", "", predicted_input_file).strip(), references=[re.sub(r"![/s]*", "", reference_input_file).strip()])

        # Order doesnt matter, since we use 1grams in bleu
        predicted_input_file_1grams = predicted_keywords + \
            predicted_input_block_options + predicted_settings
        reference_input_file_1grams = reference_keywords + \
            reference_input_block_options + reference_settings

        bleu_vocab_overlap = self.naive_bleu_unordered.sentence_score(references=[" ".join(reference_input_file_1grams)],
                                                                      hypothesis=" ".join(predicted_input_file_1grams))

        total_f1, total_precision, total_recall = self.calculate_f1(
            predicted_input_file_1grams, reference_input_file_1grams)
        kw_f1, kw_precision, kw_recall = self.calculate_f1(
            predicted_keywords, reference_keywords)
        option_f1, option_precision, option_recall = self.calculate_f1(
            predicted_input_block_options, reference_input_block_options)
        setting_f1, setting_precision, setting_recall = self.calculate_f1(
            predicted_settings, reference_settings)

        def format_number(num):
            return f"{num:.4f}"

        return [str(runnable)] + list(map(format_number, [naive_bleu.score, bleu_vocab_overlap.score,
                                                          total_f1, total_precision, total_recall,
                                                          kw_f1, kw_precision, kw_recall,
                                                          option_f1, option_precision, option_recall,
                                                          setting_f1, setting_precision, setting_recall]))

    def calculate_f1(self, predicted, reference):
        """Calculates F1 score for NLP settings."""
        if len(predicted) == 0 and len(reference) == 0:
            return 1, 1, 1
        # TP: Amount of ngrams that were predicted that are also in the reference
        true_positives = len(
            [keyword for keyword in predicted if keyword in reference])
        # FP: Amount of ngrams that were predicted that are not in the reference
        false_positives = len(
            [keyword for keyword in predicted if keyword not in reference])
        # FN: Amount of ngrams in the reference that were not predicted
        false_negatives = len(
            [keyword for keyword in reference if keyword not in predicted])
        # TN is not intersting in our context, as it is basically every single ngrams an llm can predict
        precision = true_positives / \
            (true_positives+false_positives) if (true_positives +
                                                 false_positives) > 0 else 0
        recall = true_positives / \
            (true_positives+false_negatives) if (true_positives +
                                                 false_negatives) > 0 else 0
        f1_score = 2 * (precision * recall) / (precision +
                                               recall) if (precision + recall) > 0 else 0
        return f1_score, precision, recall

    def remove_unnecessary_empty_lines(self, input_file):
        """Remove unnecasary whitespace from the input file, if there is any left."""
        # Replace multiple whitespace characters including double newlines with a single space
        return re.sub(r'\n\s*\n+', '\n', input_file).strip()
