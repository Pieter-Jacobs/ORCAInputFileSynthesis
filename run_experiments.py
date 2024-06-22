
import os
import json
import base64
import pandas as pd
from Classes.Model.Tester import Tester
from Scripts.PromptEngineering.get_prompts import get_contextual_prompt_for_input_file_generation
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Run experiment with given parameters.')
    parser.add_argument('--experiment_nr', type=int,
                        required=True, help='Experiment number')
    parser.add_argument('--prompting_technique', type=str, required=False,
                        default="BASIC_EXTENDED", help='Technique used for prompt engineering.')
    parser.add_argument('--model', type=str, required=False,
                        default='gpt-3.5-turbo', help="Model to use")
                        
    args = parser.parse_args()
    return args


def print_results():
    for experiment_nr in range(9):
        print(f"EXPERIMENT {experiment_nr}")
        results_folder = os.path.join(
        "Results", f"Experiment{experiment_nr}")
        for root, dirs, files in os.walk(results_folder):
                for filename in files:
                    if filename.endswith(".csv"):
                        file_path = os.path.join(root, filename)
                        # Read the CSV file
                        print(file_path)
                        df = pd.read_csv(file_path, sep=',')
                        print(df.mean())
                        print("Average_f1:")
                        print((df['kw_f1'].mean() + df['option_f1'].mean() + df['setting_f1'].mean()) / 3.0)
                        print("------------")

def get_system_prompt(experiment_nr, prompting_technique):
    system_prompt = ""
    if experiment_nr in [3, 4, 6, 8]:  # We use prompt engineering
        system_prompt = get_contextual_prompt_for_input_file_generation(
            context_type=prompting_technique)
    else:  # We use the standard prompt
        system_prompt = get_contextual_prompt_for_input_file_generation(
            context_type="BASIC_EXTENDED")
    if experiment_nr in [2, 4, 7, 8]:
        embedding_suffix = get_contextual_prompt_for_input_file_generation(
            context_type="EMBEDDINGS")
        system_prompt = f'{system_prompt}{embedding_suffix}'
    return system_prompt


def run_experiment(experiment_nr, data_path, model, prompting_technique=None):
    # Test set is the real, extracted data out of iochem and from the research group. This is split in 50/50 to get a validation dataset.
    # The validation set is used in selecting the params for the llm (and for at what epoch we stop finetuning).
    # We have three generated training sets (brute_force, from_manual, rule_based), to fine tune the model on.
    # CHECK Experiment 0: run gpt4o on the validation set with different system prompts, to get an idea what prompt methods (help with getting to a better dataset without any finetuning
    # Experiment 1: run gpt4o without anything on the test set
    # Experiment 2: run gpt4o with embeddings (and a piece on using them in the system prompt) on the test set
    # Experiment 3: run gpt4o with the prompt engineering
    # Experiment 4: run gpt4o with both prompt engineering tactic and embeddings (and a piece on using them in the system prompt)
    # Experiment 5: Finetune gpt4o to get gpt4o_bruteforce, gpt4o_manual and gpt4o_rulebased and test them on the testing data
    # Experiment 6: Finetune gpt4o with a chosen prompt engineering tactic, like cot, to get gpt4o_cot_bruteforce, gpt4o_cot_manual and gpt4o_cot_rulebased and test them on the testing data
    # Experiment 7: Use the models from experiment 5 with embeddings added
    # Experiment 8: (hypothesised to be the best model) Use the models from experiment 6 with embeddings added

    results_folder = os.path.join(
        "Results", f"Experiment{experiment_nr}", "".join(x for x in model if x.isalnum()))
    os.makedirs(results_folder, exist_ok=True)

    df = pd.read_csv(data_path, sep="|")
    data = [(sample, label) for sample, label in zip(
        df['sample'].to_list(), df['label'].to_list())]

    if experiment_nr == 0:
        for prompt_type in ['BASIC', 'BASIC_EXTENDED', 'COV', 'TOT', 'COT', 'GOT']:
            tester = Tester(model=model,
                            data=data,
                            system_prompt=get_contextual_prompt_for_input_file_generation(
                                context_type=prompt_type),
                            eval_file_path=f'{results_folder}{
                                os.sep}{prompt_type}.csv',
                            output_file_path=os.path.join(results_folder, f'output_{prompt_type}.txt'),)
            tester.test()
    else:
        system_prompt = get_system_prompt(experiment_nr, prompting_technique)
        tester = Tester(model=model,
                        data=data,
                        system_prompt=system_prompt,
                        eval_file_path=os.path.join(results_folder, f'eval_{
                                                    prompting_technique}.csv'),
                        output_file_path=os.path.join(results_folder, f'output_{
                                                      prompting_technique}.txt'),
                        use_embeddings=True if experiment_nr in [2, 4, 7, 8] else False)
        tester.test()


if __name__ == "__main__":
    print_results()
    # args = parse_arguments()
    # experiment_nr = args.experiment_nr
    # data_path = os.path.join("Data", "Test", "test.csv") if experiment_nr != 0 else os.path.join(
    #     "Data", "Test", "val.csv")
    # # data_path = os.path.join("Data", "Test", "val.csv") 
    # run_experiment(experiment_nr=experiment_nr, data_path=data_path,
    #                prompting_technique=args.prompting_technique, 
    #                model=args.model)
