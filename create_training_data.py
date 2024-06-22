from Classes.PromptCreation.Prompter import Prompter
from Classes.Helpers.ORCADataset import ORCADataset
from Classes.Helpers.OrcaInputFileManipulator import OrcaInputFileManipulator
from Scripts.PromptEngineering.get_prompts import *
import os
import json
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Create training dataset from generated input files with a given context type.')
    parser.add_argument('--prompting_technique', type=str, required=True,
                        help='Type of prompt engineering used (BASIC or COT)')
    args = parser.parse_args()
    return args

def create_dataset(prompting_technique):
    if prompting_technique != 'BASIC_EXTENDED' and prompting_technique != 'COT':
        print("Currently, only basic prompting and COT prompting is available for a finetuning dataset.")
        
    using_prompt_engineering = True if prompting_technique != "BASIC" else False

    contextual_prompt_prompting = get_contextual_prompt_for_prompt_creation()
    contextual_prompt_input_file = get_contextual_prompt_for_input_file_generation(
        prompting_technique)

    prompter = Prompter(contextual_prompt=contextual_prompt_prompting,
                        data_folder=f"Data{os.sep}Generated{
                            os.sep}InputFilesBruteForce",
                        create_synthetic_labels=True if using_prompt_engineering else False)
    
    prompts_brute_force = prompter.prompt()

    dataset_brute_force = ORCADataset(
        prompts=prompts_brute_force, input_files=prompter.prompt_engineered_input_files if using_prompt_engineering else prompter.input_files, system_prompt=contextual_prompt_input_file)

    prompter.input_files = prompter.load_input_files(
        f"Data{os.sep}Generated{os.sep}InputFilesFromManual")
    prompts_from_manual = prompter.prompt()
    dataset_from_manual = ORCADataset(

        prompts=prompts_from_manual, input_files=prompter.prompt_engineered_input_files if using_prompt_engineering else prompter.input_files, system_prompt=contextual_prompt_input_file)

    prompter.input_files = prompter.load_input_files(
        f"Data{os.sep}Generated{os.sep}InputFilesRuleBased")
    prompts_rule_based = prompter.prompt()
    dataset_rule_based = ORCADataset(
        prompts=prompts_rule_based, input_files=prompter.prompt_engineered_input_files if using_prompt_engineering else prompter.input_files, system_prompt=contextual_prompt_input_file)

    for dataset, description in zip([dataset_brute_force, dataset_from_manual, dataset_rule_based],
                                    ['BruteForce', 'FromManual', 'RuleBased']):
        dataset.save_to_jsonl(os.path.join(
            "Data", "Finetuning", description), filename=f"dataset_{prompting_technique}")


if __name__ == "__main__":
    args = parse_arguments()
    create_dataset(args.prompting_technique)
