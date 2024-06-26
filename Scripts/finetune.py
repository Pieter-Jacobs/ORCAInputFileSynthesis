import argparse
import os
import sys
sys.path.append(os.getcwd())
from Classes.Model.OpenAIFinetuner import OpenAIFinetuner

def parse_arguments():
    """Parses the arguments that specify the type of finetuning job"""
    parser = argparse.ArgumentParser(
        description='Run finetuning with given settings.')
    parser.add_argument('--dataset', type=str, required=True,
                        help='Dataset to train on (BruteForce, ManualBased or RuleBased)')
    parser.add_argument('--model', type=str, required=True, default='gpt-3.5-turbo',
                        help='LLM that you want to use')
    parser.add_argument('--prompt_engineering_technique', type=str, required=True, choices=['basic', 'cot'],
                        default='basic', help='Type of prompt engineering used (basic or cot)')
    parser.add_argument('--lr', type=float, required=True,
                        help='Learning rate Multiplier')
    parser.add_argument('--epochs', type=int, required=True,
                        help='Amount of epochs to finetune for')
    parser.add_argument('--batch_size', type=int, required=True,
                        help='Batch size used for finetuning')
    args = parser.parse_args()
    return args


def finetune(model, training_data_path, validation_data_path, dataset, prompt_engineering_technique, epochs, batch_size, lr):
    """Uploads the training and validation datasets and starts a finetuning job"""
    finetuner = OpenAIFinetuner()
    train_dataset_id = finetuner.upload_dataset(training_data_path)
    val_dataset_id = finetuner.upload_dataset(validation_data_path)
    finetuner.start_finetuning_job_parameterized(model=model,
                                                 train_file=train_dataset_id,
                                                 val_file=val_dataset_id,
                                                 suffix=f"{dataset[0]}_{
                                                     prompt_engineering_technique}",
                                                 n_epochs=epochs,
                                                 batch_size=batch_size,
                                                 learning_rate_multiplier=lr
                                                 )


if __name__ == "__main__":
    args = parse_arguments()
    training_data_path = os.path.join("Data", "Finetuning", args.dataset, f"dataset_{
                                      args.prompt_engineering_technique}.jsonl")
    validation_data_path = os.path.join(
        "Data", "Test", f"val_{args.prompt_engineering_technique}.jsonl")
    finetune(model=args.model, training_data_path=training_data_path, validation_data_path=validation_data_path,
             dataset=args.dataset, prompt_engineering_technique=args.prompt_engineering_technique, epochs=args.epochs, batch_size=args.batch_size, lr=args.lr)
