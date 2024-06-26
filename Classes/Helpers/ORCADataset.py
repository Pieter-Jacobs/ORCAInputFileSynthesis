import os
import json
import pandas as pd
from sklearn.model_selection import train_test_split
from Classes.Helpers.ORCAInputFileManipulator import ORCAInputFileManipulator
import random

class ORCADataset:
    def __init__(self, prompts, input_files, system_prompt, type = 'gpt'):
        self.prompts = prompts
        self.input_files = input_files
        self.system_prompt = system_prompt
        self.type = type
        if type == 'gpt':
            self.data = self.build_dataset_gpt(
                prompts=prompts, input_files=input_files) 
        elif type == 'csv':
            self.data = self.build_dataset_csv(prompts=prompts, input_files=input_files)

    def build_dataset_gpt(self, prompts, input_files):
        data = []
        for prompt, input_file in zip(prompts, input_files):
            input_file = input_file.replace("pal6 ", "")
            input_file = ORCAInputFileManipulator.remove_xyz(input_file)
            data.append({"messages": [{"role": "system", "content": self.system_prompt},
                                    {"role": "user", "content": prompt},
                                    {"role": "assistant", "content": input_file}]})
        return data
    
    def build_dataset_csv(self, prompts, input_files):
        data = {
            'sample': prompts,
            'label': [ORCAInputFileManipulator.remove_xyz(input_file) for input_file in input_files]
        }
        df = pd.DataFrame(data)
        return df

    
    def save_to_jsonl(self, saving_folder, data = None, filename="dataset"):
        data = self.data if data is None else data
        with open(os.path.join(saving_folder, filename + ".jsonl"), "w") as jsonl_file:
            for entry in data:
                json.dump(entry, jsonl_file)
                jsonl_file.write('\n')

    def split(self, val_size):
        sample_size = int(len(self.data) * val_size)
        val = test = []
        if self.type == 'gpt':
            val = random.sample(self.data, sample_size)
            test = [item for item in self.data if item not in val]
        elif self.type == 'csv':
            val, test = train_test_split(self.data, test_size=1-val_size, random_state=2000)
        return val, test