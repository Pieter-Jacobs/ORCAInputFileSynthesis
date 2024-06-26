
import os
import sys
sys.path.append(os.getcwd())
import pandas as pd
from Classes.Model.Tester import Tester

def run_preliminary_experiment(data_path):
    """Runs the base model for all prompt engineering techniques on the provided path to a csv file."""

    model = "gpt-3.5-turbo" # We use the baseline model

    results_folder = os.path.join(
        "Results", "Experiment0", "".join(x for x in model if x.isalnum()))
    os.makedirs(results_folder, exist_ok=True)

    # Load the data from file and transform it to the desired format
    df = pd.read_csv(data_path, sep="|")
    data = [(sample, label) for sample, label in zip(
        df['sample'].to_list(), df['label'].to_list())]

    # Run the base model for all prompt engineering types
    for prompt_engineering_technique in ['none', 'basic', 'cot', 'cove', 'tot', 'got']:
        system_prompt = open(os.path.join("Data", "Prompts", "PromptEngineeringTechniques", f"{
                         prompt_engineering_technique.lower()}.txt"), 'r', encoding='utf-8').read()
        tester = Tester(model=model,
                        data=data,
                        system_prompt=system_prompt,
                        eval_file_path=f'{results_folder}{
                            os.sep}{prompt_engineering_technique}.csv',
                        output_file_path=os.path.join(results_folder, f'output_{prompt_engineering_technique}.txt'),)
        tester.test()

if __name__ == "__main__":
    validation_data_path = os.path.join("Data", "Test", "val.csv")
    run_preliminary_experiment(validation_data_path)