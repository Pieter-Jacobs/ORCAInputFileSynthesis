
import os
import sys
sys.path.append(os.getcwd())
from Classes.ORCAGenerators.RuleBasedORCAGenerator import RuleBasedORCAGenerator
from Classes.ORCAGenerators.BruteForceORCAGenerator import BruteForceORCAGenerator
from Classes.ORCAGenerators.ManualBasedORCAGenerator import ManualBasedORCAGenerator
import random
import argparse


random.seed(2000)


def parse_arguments():
    """Parses the arguments to be used in the generation of ORCA input files."""
    parser = argparse.ArgumentParser(
        description="Generate input files for different methods.")
    parser.add_argument('--method', type=int, choices=[0, 1, 2], default=2,
                        help="Method to use: 0 (brute-force), 1 (manual-based), 2 (rule-based)")
    parser.add_argument('--N', type=int, default=None,
                        help="Amount of input files that is to be generated")
    parser.add_argument('--save_warnings', action='store_true',
                        help="Save the warnings ORCA returns for executable files")
    parser.add_argument('--save_errors', action='store_true',
                        help="Save the errors ORCA returns for executable files")
    parser.add_argument('--accept_warnings', action='store_true',
                        help="Only save input files without warnings.")
    parser.add_argument('--add_input_block', action='store_true',
                        help="Add an input block to the file when using the brute-force or manual-based method")
    parser.add_argument('--add_solvation', action='store_true',
                        help="Set add_solvation to True for the rule-based method")
    parser.add_argument('--calculation_type', type=str, required=False,
                        default='dft', choices=['dft', 'hf', 'cc', 'dft_opt', 'hf_opt', 'cc_opt',
                                                'dft_es', 'hf_es', 'cc_es', 'dft_freq', 'hf_freq', 'cc_freq'],
                        help="Value for calculation_type parameter")
    args = parser.parse_args()
    return args


def generate_input_files(method, params):
    """Generate the ORCA input files with a given method, also checks that only valid params are passed to the generators."""
    generator = None
    if method == 0:
        valid_args = ['N', 'save_warnings', 'save_errors', 'add_input_block', 'accept_warnings']
        params = {k: v for k, v in params.items() if k in valid_args}
        generator = BruteForceORCAGenerator(save_folder=f"Data{os.sep}Generated{os.sep}InputFilesBruteForce",
                                            max_len_input_blocks=5,
                                            max_len_keywords=10)

    elif method == 1:
        valid_args = ['N', 'save_warnings', 'save_errors', 'add_input_block', 'accept_warnings']
        params = {k: v for k, v in params.items() if k in valid_args}
        generator = ManualBasedORCAGenerator(save_folder=f"Data{os.sep}Generated{
                                             os.sep}InputFilesManualBased")
    if method == 2:
        valid_args = ['N', 'save_warnings', 'save_errors', 'accept_warnings', 'calculation_type', 'add_solvation']
        params = {k: v for k, v in params.items() if k in valid_args}
        generator = RuleBasedORCAGenerator(
            save_folder=f"Data{os.sep}Generated{os.sep}InputFilesRuleBased")
        
    generator.generate_input_files(**params)


if __name__ == "__main__":
    args = parse_arguments()

    params = {
        "N": args.N,
        "save_warnings": args.save_warnings,
        "save_errors": args.save_errors,
        "generation_params": {
            "accept_warnings": args.accept_warnings,
            "add_input_block": args.add_input_block,
            "calculation_type": args.calculation_type,
            "add_solvation": args.add_solvation
        }
    }

    generate_input_files(method=args.method, params=params)
