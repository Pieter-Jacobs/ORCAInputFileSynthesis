# Scripts
This folder contain all the necassary scripts that one has to run to replicate our study.
This involves creating and processing the training and testing datasets (including the scraping of data), 
creating the `Gen3Molecules` dataset, and running our experiments.

## DatasetCreation
This folder contains all scripts used to gather the necassary data for inference. The most important file in this folder is
`generate_input_files.py`. One can use it to generate input files for the brute-force, manual-based and rule-based datasets by specifying the arguments:
  ```bash
    --method
    --N
    --save_warnings
    --save_errors
    --accept_warnings
    --add_input_block
    --calculation_type
    --add_solvation
  ```
  The allowed values are found in the `parse_arguments` function. One should run this file from the root directory.
   An example of how one could generate 50 ORCA input files with the brute-force approach, that all have input blocks would be the following:
  ```bash
  python Scripts/DatasetCreation/generate_input_files.py --method 0 --N 50 --add_input_block
  ```

The following subsections will briefly describe the scripts in the other folders.

### Scraping
This folder contains two simple scrapers, which have to be run from the root folder:
- `input_file_library_scraper.py`: used for scraping the different pages of https://sites.google.com/site/orcainputlibrary/home. This data gets used when RAG is employed during inference.
- `iochem_scraper.py`: scrapes the ORCA input files available on IoChem.
Note though, that we already provide the final `ORCAExtracted` dataset and that the iochem_scraper should thus only be used when trying to reproduce our study.

### DataCleaning
After one has generated the desired amount of input files with `generate_input_files.py`, they can be processed by running
 ```bash
  python Scripts/DatasetCreation/DataCleaning/clean_generated_data.py
  ```
from the root directory. This renames the data and ensures that all input files in it are unique.

More importantly, when one has run `iochem_scraper.py` to scrape the input files from the IoChem database, they can run
 ```bash
  python Scripts/DatasetCreation/DataCleaning/clean_extracted_data.py
 ```
This script:
1. Deletes duplicate input files, 
2. Removes unnecassary whitespace from them
3. Removes all comment lines from them
4. Replaces possible outdated keywords
5. Makes the input files lower case 
6. Changes the input files their coordinate block to its corresponding SMILES comment.
Note though, that we already provide the final `ORCAExtracted` dataset in the folder which this script cleans. It should thus only be used when trying to reproduce our study.


### DataFormatting
The scripts in this folder are used to reformat the generated and extracted validation data into their final formats. 
**In doing this, the script also assigns the user prompts to the various input files.**

- `create_training_data.py`: Use either a brute-force, manual-based or rule-based dataset to reformat into a finetuning dataset. Note that we have already provided these in
`Data/Finetuning` and that this is thus used for reproducibility purposes. An example run, to reformat the brute-force dataset (which should be in `Data/Generated/InputFilesBruteForce`) can be done as follows:
```bash
python Scripts/DatasetCreation/DataFormatting/create_training_data.py --prompt_engineering_technique basic --dataset BruteForce
```

- `create_testing_and_val_data.py`: Used to reformat the data in the `Data/ORCAExtracted` folder into csv format so that it can easily be used for evaluation. Moreover, the validation set is also created in jsonl format so that it can be used in finetuning. Note though, that we already provide the final `ORCAExtracted` dataset and that the iochem_scraper should thus only be used when trying to reproduce our study. An example run, using CoT prompt engineering:
```bash
python Scripts/DatasetCreation/DataFormatting/create_testing_and_val_data --prompt_engineering_technique cot
```

### MoleculeGeneration
This folder contains the script used to generate our `Gen3Molecules` dataset.
One can generate a dataset of radical molecules using:

```bash
python run_main_experiment.py --prompt_engineering_technique cot --rag 1 --k 5 
```
As for regular molecules, one can use: 
```bash
python run_main_experiment.py --prompt_engineering_technique cot --rag 1 --k 5 
```

## Inference

This folder contains the scripts to run the experiments described in the paper.

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
2. Results will be saved in the `Results/Experiment0` folder.

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
  python Scripts/Inference/run_main_experiment.py --prompt_engineering_technique cot --rag 1 --k 5 
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
  python Scripts/Inference/run_real_prompts_experiment.py --prompt_engineering_technique cot --rag 1 --k 5 
  ```
- **Further Instructions**
1. Ensure the `Data/Prompts/RealPrompts` folder contains the necessary prompt files.
2. If using RAG, ensure the relevant context data is available in `Data/Documents/Embedded/index_merged`.
3. Results will be saved in the `Results/RealPrompts` folder.

