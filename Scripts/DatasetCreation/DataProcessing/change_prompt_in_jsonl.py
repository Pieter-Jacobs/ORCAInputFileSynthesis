import os
import json
from Classes.PromptCreation.Prompter import Prompter
from Scripts.PromptEngineering.get_prompts import get_contextual_prompt_for_input_file_generation
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Change a jsonl dataset so that a different contextual prompt is used')
    parser.add_argument('--old_prompting_technique', type=str, required=True,
                        help='Type of prompt engineering used in dataset to be changed')
    parser.add_argument('--new_prompting_technique', type=str, required=True,
                        help='Type of prompt engineering used in newly created dataset')
    args = parser.parse_args()
    return args


def change_prompt_in_jsonl(input_file_path, output_file_prompt, prompting_technique, prompter):
    contextual_prompt = get_contextual_prompt_for_input_file_generation(
        prompting_technique)
    with open(input_file_path, 'r') as infile, open(output_file_prompt, 'w') as outfile:
        # Process each line in the input file
        for line in infile:
            # Parse the JSON from the current line
            data = json.loads(line.strip())

            # Modify the JSON data (example: add a new key-value pair)
            data['messages'][0]['content'] = contextual_prompt
            data['messages'][2]['content'] = prompter.create_cot_label_from_input_file(data['messages'][2]['content'])
            # Write the modified JSON data to the output file
            outfile.write(json.dumps(data) + '\n')


if __name__ == "__main__":
    args = parse_arguments()
    for data_type in ["BruteForce", "FromManual", "RuleBased"]:
        prompter = Prompter(contextual_prompt=get_contextual_prompt_for_input_file_generation(args.new_prompting_technique),
                        data_folder=f"Data{os.sep}Generated{
                            os.sep}InputFiles{data_type}",
                        create_synthetic_labels=False)
    
        # change_prompt_in_jsonl(input_file_path=os.path.join("Data", "Finetuning", data_type, f"dataset_{args.old_prompting_technique}.jsonl"),
        #                        output_file_prompt=os.path.join("Data", "Finetuning", data_type, f"dataset_{args.new_prompting_technique}.jsonl"),
        #                        prompting_technique=args.new_prompting_technique, prompter=prompter)
    
    change_prompt_in_jsonl(input_file_path=os.path.join("Data", "Test", f"val_{args.old_prompting_technique}.jsonl"),
                            output_file_prompt=os.path.join("Data", "Test", f"val_{args.new_prompting_technique}.jsonl"),
                            prompting_technique=args.new_prompting_technique, prompter=prompter)