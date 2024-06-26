import sys
import os
sys.path.append(os.getcwd())
from Classes.PromptCreation.Prompter import Prompter
from Classes.Helpers.ORCADataset import ORCADataset
import argparse

def parse_arguments():
    """Parses the dataset and prompting technique needed to create the finetuning dataset"""
    parser = argparse.ArgumentParser(
        description='Create training dataset from generated input files with a prompt engineering technique and dataset type.')
    parser.add_argument('--prompt_engineering_technique', type=str, required=True, choices=['basic', 'cot'],
                        help='Type of prompt engineering used (basic or cot)')
    parser.add_argument('--dataset', type=str, required=True, choices=['RuleBased', 'ManualBased', 'BruteForce'],
                        help='Type of dataset used (RuleBased, ManualBased or BruteForce)')
    args = parser.parse_args()
    return args


def create_dataset(prompt_engineering_technique, dataset):
    """Creates a finetuning dataset in jsonl format based on a given prompt engineering technique"""
    using_prompt_engineering = True if prompt_engineering_technique != "basic" else False

    # Define the system prompts for creating synthetic prompts and for generating input files
    system_prompt_prompting = open(os.path.join(
        "Data", "Prompts", "PromptEngineeringTechniques", f"prompt_creation.txt"), 'r', encoding='utf-8').read()
    system_prompt_input_file = open(os.path.join("Data", "Prompts", "PromptEngineeringTechniques", f"{
        prompt_engineering_technique}.txt"), 'r', encoding='utf-8').read()

    # Create synthetic prompts for all input files 
    prompter = Prompter(contextual_prompt=system_prompt_prompting,
                        data_folder=f"Data{os.sep}Generated{os.sep}InputFiles{dataset}",
                        create_synthetic_labels=True if using_prompt_engineering else False)
    prompts = prompter.prompt()

    # Create an ORCADataset, and save it to file
    dataset = ORCADataset(
        prompts=prompts,
        input_files=prompter.prompt_engineered_input_files if using_prompt_engineering else prompter.input_files,
        system_prompt=system_prompt_input_file
    )
    dataset.save_to_jsonl(os.path.join(
        "Data", "Finetuning", dataset), filename=f"dataset_{prompt_engineering_technique}")


if __name__ == "__main__":
    args = parse_arguments()
    create_dataset(args.prompt_engineering_technique, args.dataset)
