import json
import os

def get_contextual_prompt_for_prompt_creation(context_type="COT"):
    with open(f"Data{os.sep}Prompts{os.sep}prompt_creation.json", encoding='utf-8') as f:
        prompts = json.load(f)
    with open(f"Data{os.sep}Prompts{os.sep}{prompts[context_type]}", 'r') as f:
        prompt = f.read()
    return prompt

def get_contextual_prompt_for_input_file_generation(context_type="COT"):
    with open(f"Data{os.sep}Prompts{os.sep}input_file_generation.json", encoding='utf-8') as f:
        prompts = json.load(f)
    with open(f"Data{os.sep}Prompts{os.sep}{prompts[context_type]}", 'r') as f:
        prompt = f.read()
    return prompt
