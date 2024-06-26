
import argparse
import os
import sys
sys.path.append(os.getcwd())
import pandas as pd
from Classes.Model.Tester import Tester

def parse_arguments():
    """Parsess the arguments that are used to determine which model is to be ran on the ORCAExtracted test dataset"""
    parser = argparse.ArgumentParser(
        description='Run experiment with given parameters.')
    parser.add_argument('--prompt_engineering_technique', type=str, required=False,
                        default="basic", choices=['none', 'basic', 'cot', 'cove', 'tot', 'got'],
                        help='Prompt engineering technique to be used (none, basic, cot, cove, tot, or got).')
    parser.add_argument('--model', type=str, required=False,
                        default='gpt-3.5-turbo', help="OpenAI model to use, if a finetuned model is used one should copy full model name from the OpenAI finetuning dashboard.")
    parser.add_argument('--rag', type=int, required=False,
                        default=0, choices=[0, 1], help="Determines whether the model should use RAG during inference (0 or 1)")
    parser.add_argument('--k', type=int, required=False,
                        default=1, help="Amount of documents to retrieve when using RAG.")
    parser.add_argument('--experiment_nr', type=int,
                        required=True, help='Experiment number used to create the folder to save the gathered results to.')
    args = parser.parse_args()
    return args


def run_experiment(experiment_nr, data_path, model='gpt-3.5-turbo', prompt_engineering_technique='none', rag=0, k=1):
    """Runs a specified model on provided dataset in a csv file using a specified prompt engineering technique.
    Parameters:
    - experiment_nr (int): The number of the experiment that will be run, 
    used as an identifier for the folder to which the results will be saved
    - model (str): The name or identifier of the model to be used.
    - data_path (str): The path to the csv file containing the data (seperator has to be |)
    - prompt_engineering_technique (str): The technique to be used for prompt engineering.
    - rag (bool): Flag indicating whether to use Retrieval-Augmented Generation (RAG).
    - k (int): The number of relevant contexts to retrieve if RAG is enabled."""

    results_folder = os.path.join(
        "Results", f"Experiment{experiment_nr}", "".join(x for x in model if x.isalnum()))
    os.makedirs(results_folder, exist_ok=True)

    df = pd.read_csv(data_path, sep="|")
    data = [(sample, label) for sample, label in zip(
        df['sample'].to_list(), df['label'].to_list())]

    system_prompt = open(os.path.join("Data", "Prompts", "PromptEngineeringTechniques", f"{
                         prompt_engineering_technique.lower()}.txt"), 'r', encoding='utf-8').read()
    
    # If rag is employed, we extend the system prompt with relevant instructions on how to handle context.
    if rag:
        rag_instructions = open(os.path.join("Data", "Prompts", "PromptEngineeringTechniques", "rag.txt"),
                                'r', encoding='utf-8').read()
        system_prompt = f'{system_prompt}{rag_instructions}'

    tester = Tester(model=model,
                    data=data,
                    system_prompt=system_prompt,
                    eval_file_path=os.path.join(results_folder, f'eval_{
                                                prompt_engineering_technique}.csv'),
                    output_file_path=os.path.join(results_folder, f'output_{
                        prompt_engineering_technique}.txt'),
                    use_embeddings=rag)
    tester.test()


if __name__ == "__main__":
    args = parse_arguments()
    test_data_path = os.path.join("Data", "Test", "test.csv")
    run_experiment(experiment_nr=args.experiment_nr, data_path=test_data_path,
                   prompt_engineering_technique=args.prompt_engineering_technique,
                   model=args.model,
                   rag=args.rag,
                   k=args.k)
