import os
from Classes.Model.Embedder import Embedder
from Classes.Model.OpenAIFinetuner import OpenAIFinetuner
from Classes.Helpers.ORCADataset import ORCADataset
from Scripts.PromptEngineering.get_prompts import get_contextual_prompt_for_input_file_generation
import argparse
import pandas as pd


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Run finetuning with given dataset.')
    parser.add_argument('--dataset', type=str, required=True,
                        help='Dataset to train on (BruteForce, FromManual or RuleBased)')
    parser.add_argument('--model', type=str, required=True,
                    help='LLM that you want to use')
    parser.add_argument('--prompting_technique', type=str, required=True,
                        help='Type of prompt engineering used (BASIC_EXTENDED or COT)')
    args = parser.parse_args()
    return args


def finetune(model, training_data_path, validation_data_path, dataset, prompting_technique):
    # We want to finetune 3 models: bruteforce, frommanual, rulebased.
    # Perhaps for each model even on a different amount of examples (100, 200, 300, 400)
    finetuner = OpenAIFinetuner()
    train_dataset_id = finetuner.upload_dataset(training_data_path)
    val_dataset_id = finetuner.upload_dataset(validation_data_path)
    finetuner.start_finetuning_job_parameterized(model=model,
                                   train_file=train_dataset_id,
                                   val_file=val_dataset_id,
                                   suffix=f"{dataset[0]}_{prompting_technique}",
                                   n_epochs=3,
                                   batch_size=1,
                                   learning_rate_multiplier=2
                                   )


if __name__ == "__main__":
    args = parse_arguments()
    training_data_path = os.path.join("Data", "Finetuning", args.dataset, f"dataset_{args.prompting_technique}.jsonl")
    validation_data_path = os.path.join(
        "Data", "Test", f"val_{args.prompting_technique}.jsonl")
    finetune(model=args.model, training_data_path=training_data_path, validation_data_path=validation_data_path,
             dataset=args.dataset, prompting_technique=args.prompting_technique)

