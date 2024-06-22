import os
import pandas as pd
from Classes.PromptCreation.Prompter import Prompter
from Classes.Helpers.ORCADataset import ORCADataset
from Scripts.PromptEngineering.get_prompts import *
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Run finetuning with given dataset.')
    parser.add_argument('--prompting_technique', type=str, required=True,
                        help='Type of prompt engineering used for validation data (BASIC_EXTENDED or COT)')
    args = parser.parse_args()
    return args


def save_val_data_to_jsonl(validation_data_path, prompting_technique):
    val_data_df = pd.read_csv(validation_data_path, sep='|')
    val_dataset = ORCADataset(prompts=val_data_df['sample'].to_list(), input_files=val_data_df["label"].to_list(),
                              system_prompt=get_contextual_prompt_for_input_file_generation(prompting_technique))
    val_dataset.save_to_jsonl(validation_data_path.removesuffix(
        "val.csv"), filename=f"val_{prompting_technique}")


def create_testing_and_val_data(folder_path_testing_input_files, saving_folder_path, prompting_technique):
    prompter = Prompter(contextual_prompt=get_contextual_prompt_for_prompt_creation(
    ), data_folder=folder_path_testing_input_files)
    prompts = prompter.prompt()

    dataset = ORCADataset(
        prompts=prompts, input_files=prompter.input_files, system_prompt=None, type='csv')
    val, test = dataset.split(val_size=0.5)
    # CSV format is used for the preliminary experiment
    val.to_csv(os.path.join(saving_folder_path,
               "val.csv"), index=False, sep="|")
    # Jsonl is used for all the finetuning experiments
    save_val_data_to_jsonl(os.path.join(saving_folder_path,
                                        "val.csv"), prompting_technique=prompting_technique)

    test.to_csv(os.path.join(saving_folder_path,
                             "test.csv"), index=False, sep="|")


if __name__ == "__main__":
    args = parse_arguments()
    data_folder = os.path.join("Data", "Extracted")
    saving_folder = os.path.join("Data", "Test")
    create_testing_and_val_data(folder_path_testing_input_files=data_folder,
                                saving_folder_path=saving_folder,
                                prompting_technique=args.prompting_technique)
