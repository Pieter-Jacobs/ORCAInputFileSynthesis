# Inference

This folder contains the scripts to run the experiments described in the paper.

## Overview of Files

### 1. run_preliminary_experiment.py
- **Purpose**: 
  - Conduct the preliminary experiment where the base model is ran on the desired validation dataset set 
  for all implemented prompt engineering techniques.
- **Usage**:
  Run this script from the root directory:
  ```bash
  python Scripts/Inference/run_preliminary_experiment.py
  ```
- **Further Instructions**
1. Ensure the `Data/Test/val.csv` file contains the validation dataset.
3. Results will be saved in the `Results/Experiment0` folder.

### 2. run_main_experiment.py
- **Purpose**: 
  - Perform the evaluation of a specified model configuration on the test dataset.
  - If no arguments are provided, the script will default to running GPT-3.5 Turbo with 'basic' prompt engineering.
- **Usage**:
  The script should be run from the root directory, and allows for the following arguments:
  ```bash
    --experiment_nr
    --model
    --prompt_engineering_technique 
    --rag
    --k
  ```
  The allowed values are found in the `parse_arguments` function. 
  An example of how one could run the base model with CoT and RAG would be:
  ```bash
  python run_main_experiment.py --prompt_engineering_technique cot --rag 1 --k 5 
  ```
- **Further Instructions**
1. Ensure the `Data/Test/test.csv` file contains the desired test dataset.
2. If using RAG, ensure the relevant context data is available in `Data/Documents/Embedded/index_merged`.
3. Results will be saved in the `Results/Experiment[experiment_nr]` folder.


### 3. run_real_prompts_experiment.py
- **Purpose**: 
  - Perform the evaluation of a specified model configuration on the `RealPrompts` dataset.
  - If no arguments are provided, the script will default to running GPT-3.5 Turbo with 'basic' prompt engineering.
- **Usage**:
  The script should be run from the root directory, and allows for the following arguments:
  ```bash
    --experiment_nr
    --model
    --prompt_engineering_technique 
    --rag
    --k
  ```
  The allowed values are found in the `parse_arguments` function. 
  An example of how one could run the base model with CoT and RAG would be:
  ```bash
  python run_real_prompts_experiment.py --prompt_engineering_technique cot --rag 1 --k 5 
  ```
- **Further Instructions**
1. Ensure the `Data/Prompts/RealPrompts` folder contains the necessary prompt files.
2. If using RAG, ensure the relevant context data is available in `Data/Documents/Embedded/index_merged`.
3. Results will be saved in the `Results/RealPrompts` folder.
