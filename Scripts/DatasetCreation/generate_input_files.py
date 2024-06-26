from Classes.ORCAGenerators.RuleBasedORCAGenerator import RuleBasedORCAGenerator
from Classes.ORCAGenerators.BruteForceORCAGenerator import BruteForceORCAGenerator
from Classes.ORCAGenerators.ManualBasedORCAGenerator import ManualBasedORCAGenerator
import os
import random

random.seed(2000)

def generate_input_files(method=2, params={"N": 50}):
    generator = None
    if method == 0:
        generator = BruteForceORCAGenerator(save_folder=f"Data{os.sep}Generated{os.sep}InputFilesBruteForce",
                                            max_len_input_blocks=5,
                                            max_len_keywords=10)

    elif method == 1:
        generator = ManualBasedORCAGenerator(save_folder=f"Data{os.sep}Generated{
                                             os.sep}InputFilesFromManual")
    if method == 2:
        generator = RuleBasedORCAGenerator(
            save_folder=f"Data{os.sep}Generated{os.sep}InputFilesRuleBased")
    generator.generate_input_files(**params)


if __name__ == "__main__":
    brute_force_params = {
        "N": 100,
        "few_shot": False,
        "save_warnings": True,
        "save_errors": True,
        "generation_params":
            {
                "accept_warnings": True,
                "add_input_block": True
            }
    }
    from_manual_params = {
        "N": 100,
        "few_shot": False,
        "save_warnings": True,
        "save_errors": True,
        "generation_params":
            {
                "accept_warnings": True,
                "add_input_block": False
            }
    }
    rule_based_params = {
        "N": 1,
        "few_shot": False,
        "save_warnings": True,
        "save_errors": True,
        "generation_params":
            {
                "accept_warnings": True,
                "calculation_type": "cc_freq",
                "add_solvation": False
            }
    }

    # generate_input_files(method=0, params=brute_force_params)

    # generate_input_files(method=1, params=from_manual_params)
    # from_manual_params["N"] = 50

    # from_manual_params["generation_params"]["add_input_block"] = True
    # generate_input_files(method=1, params=from_manual_params)
    # from_manual_params["N"] = 29

    # from_manual_params["generation_params"]["add_input_block"] = False
    # generate_input_files(method=1, params=from_manual_params)
    

    count = 0
    supported_calculations = [x for x in RuleBasedORCAGenerator.get_supported_calculations() if x != 'cc_freq']
    while count <= 500:
        rule_based_params["generation_params"]['add_solvation'] = False
        for method in supported_calculations:
            rule_based_params["generation_params"]['calculation_type'] = method
            generate_input_files(method=2, params=rule_based_params)  
            count += 1
        rule_based_params["generation_params"]['add_solvation'] = True
        rule_based_params["generation_params"]['calculation_type'] = random.choice(supported_calculations)
        generate_input_files(method=2, params=rule_based_params)  
        count += 1