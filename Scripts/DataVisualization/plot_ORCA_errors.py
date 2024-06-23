import argparse
import os
import sys
sys.path.append(os.getcwd())

def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Plot the ORCA errors from a given experiment.')
    parser.add_argument('--experiment_nr', type=int,
                        required=True, help='Experiment number')
    parser.add_argument('--model_folder', type=int, default='gpt35turbo0125',
                        required=False, help='Used Model')
    parser.add_argument('--prompting_technique', type=int, default='BASIC_EXTENDED',
                        required=False, help='Used Prompt Engineering')
    args = parser.parse_args()
    return args


def extract_inp_files_from_output_file(filepath):
    with open(filepath, 'r') as file:
        data = file.read()    
    # Split the data into chunks by "---END---"
    input_files = data.split('---END---')
    input_files = [input_file.strip() for input_file in input_files if input_file.strip()]
    return input_files

def plot_ORCA_errors(experiment_nr, model_folder, prompting_technique):
    path = os.path.join('Results', f"Experiment{experiment_nr}", model_folder, f"output_{prompting_technique}.txt")
    input_files = extract_inp_files_from_output_file(path)
    print(input_files)

if __name__ == "__main__":
    args = parse_arguments()
    plot_ORCA_errors(args.experiment_nr, args.model_folder, args.prompting_technique)