import os
import sys
sys.path.append(os.getcwd())
import pandas as pd
from Classes.PromptCreation.Prompter import Prompter
from Classes.Helpers.ORCADataset import ORCADataset
import argparse


def parse_arguments():
    """Parses the prompting technique needed to create the evaluation datasets"""
    parser = argparse.ArgumentParser(
        description='Create the evaluation datasets for a given prompt engineering technique.')
    parser.add_argument('--prompt_engineering_technique', type=str, required=True, choices=['basic', 'cot'],
                        help='Type of prompt engineering used in the validation datasets (basic or cot)')
    args = parser.parse_args()
    return args


def save_val_data_to_jsonl(validation_data_path, prompt_engineering_technique):
    """Given the path to the .csv file containing the validation data, this function converts it into a jsonl format."""

    system_prompt =  open(os.path.join("Data", "Prompts", "PromptEngineeringTechniques", f"{
        prompt_engineering_technique}.txt"), 'r', encoding='utf-8').read()
    
    val_data_df = pd.read_csv(validation_data_path, sep='|')
    val_dataset = ORCADataset(prompts=val_data_df['sample'].to_list(), input_files=val_data_df["label"].to_list(),
                              system_prompt=system_prompt)
    
    val_dataset.save_to_jsonl(validation_data_path.removesuffix(
        "val.csv"), filename=f"val_{prompt_engineering_technique}")


def create_testing_and_val_data(folder_path_testing_input_files, saving_folder_path, prompt_engineering_technique):
    """Assigns prompts to the extracted evaluation data and splits and saves them."""
    prompter = Prompter(contextual_prompt=open(os.path.join(
        "Data", "Prompts", "PromptEngineeringTechniques", f"prompt_creation.txt"), 'r', encoding='utf-8').read(), data_folder=folder_path_testing_input_files)
    prompts = prompter.prompt()

    dataset = ORCADataset(
        prompts=prompts, input_files=prompter.input_files, system_prompt=None, type='csv')
    val, test = dataset.split(val_size=0.5)
    
    val.to_csv(os.path.join(saving_folder_path,
               "val.csv"), index=False, sep="|")
    save_val_data_to_jsonl(os.path.join(saving_folder_path,
                                        "val.csv"), prompt_engineering_technique=prompt_engineering_technique)
    test.to_csv(os.path.join(saving_folder_path,
                             "test.csv"), index=False, sep="|")


if __name__ == "__main__":
    args = parse_arguments()
    data_folder = os.path.join("Data", "ORCAExtracted")
    saving_folder = os.path.join("Data", "Test")
    create_testing_and_val_data(folder_path_testing_input_files=data_folder,
                                saving_folder_path=saving_folder,
                                prompt_engineering_technique=args.prompt_engineering_technique)
