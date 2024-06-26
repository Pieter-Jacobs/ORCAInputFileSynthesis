# Scripts

This folder contains all the necessary scripts required to replicate our study. It involves creating and processing the training and testing datasets, including data scraping, generating the `Gen3Molecules` dataset, finetuning models, and running our experiments. This README will describe all these scripts.

One of the key scripts in our research, `finetune.py`, is located at the top directory. It initiates an OpenAI finetuning job and can be executed from the root directory with the following arguments:
```bash
--dataset
--model
--prompt_engineering_technique
--lr
--epochs
--batch_size
```
The allowed values are detailed in the `parse_arguments` function. For example, to achieve our best performing model, you can run:
```bash
python Scripts/finetune.py --epochs 8 --lr 2 --batch_size 1 --dataset ManualBased --prompt_engineering_technique cot
```
Ensure that the desired training and validation datasets are available in `Data/Finetuning` and `Data/Test`, respectively.

## DatasetCreation

This folder contains scripts used to gather necessary data for inference. The most important file here is `generate_input_files.py`. It can generate input files for brute-force, manual-based, and rule-based datasets by specifying arguments such as:
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

Allowed values are specified in the `parse_arguments` function. For instance, to generate 50 ORCA input files using the brute-force approach with input blocks, you would run:
```bash
python Scripts/DatasetCreation/generate_input_files.py --method 0 --N 50 --add_input_block
```

Additionally, `embed.py` can be executed from the root directory when ORCA manuals and scraped ORCA input libraries from `Data/Documents/Regular` in PDF format are available. It indexes these documents with FAISS for use with RAG.

The following subsections briefly describe scripts in other folders.

### Scraping

This folder contains two simple scrapers which should be executed from the root folder:
- `input_file_library_scraper.py`: Scrapes pages from https://sites.google.com/site/orcainputlibrary/home. This data is used when RAG is employed during inference.
- `iochem_scraper.py`: Scrapes ORCA input files from IoChem. Note that we already provide the final `ORCAExtracted` dataset, so `iochem_scraper.py` should only be used to reproduce our study.

### DataCleaning

After generating desired input files with `generate_input_files.py`, they can be processed by running:
```bash
python Scripts/DatasetCreation/DataCleaning/clean_generated_data.py
```
from the root directory. This script renames data and ensures all input files are unique.

When `iochem_scraper.py` is used to scrape input files from the IoChem database, you can then run:
```bash
python Scripts/DatasetCreation/DataCleaning/clean_extracted_data.py
```
This script:
1. Deletes duplicate input files,
2. Removes unnecessary whitespace,
3. Removes all comment lines,
4. Updates outdated keywords,
5. Converts input files to lowercase,
6. Changes coordinate blocks to corresponding SMILES comments.

Note that we provide the final `ORCAExtracted` dataset, and this script should only be used for reproducing our study.

### DataFormatting

Scripts in this folder reformat generated and extracted validation data into their final formats, including assigning user prompts to input files.

- `create_training_data.py`: Reformats brute-force, manual-based, or rule-based datasets into a fine-tuning dataset. We have provided these in `Data/Finetuning` for reproducibility. For example, reformatting the brute-force dataset (`Data/Generated/InputFilesBruteForce`) can be done with:
```bash
python Scripts/DatasetCreation/DataFormatting/create_training_data.py --prompt_engineering_technique basic --dataset BruteForce
```

- `create_testing_and_val_data.py`: Reformats data in `Data/ORCAExtracted` into CSV format for evaluation and creates the validation set in JSONL format for fine-tuning. Note that we already provide the final `ORCAExtracted` dataset, and this script should only be used for reproducing our study. An example using CoT prompt engineering:
```bash
python Scripts/DatasetCreation/DataFormatting/create_testing_and_val_data --prompt_engineering_technique cot
```

### MoleculeGeneration

This folder contains the script used to generate our `Gen3Molecules` dataset. You can generate radical molecules dataset using:
```bash
python run_main_experiment.py --prompt_engineering_technique cot --rag 1 --k 5 
```
For regular molecules, you can use:
```bash
python run_main_experiment.py --prompt_engineering_technique cot --rag 1 --k 5 
```

## Inference

This folder contains scripts to run experiments described in the paper.

1. `run_preliminary_experiment.py`
   - **Purpose**: Conducts preliminary experiments where the base model is run on desired validation datasets for all implemented prompt engineering techniques.
   - **Usage**: Run from the root directory:
   ```bash
   python Scripts/Inference/run_preliminary_experiment.py
   ```
   - **Instructions**: Ensure `Data/Test/val.csv` contains the validation dataset. Results will be saved in `Results/Experiment0`.

2. `run_main_experiment.py`
   - **Purpose**: Evaluates specified model configurations on the test dataset.
   - **Usage**: Run from the root directory with arguments:
   ```bash
   --experiment_nr
   --model
   --prompt_engineering_technique 
   --rag
   --k
   ```
   Allowed values are in the `parse_arguments` function. For example, running the base model with CoT and RAG:
   ```bash
   python Scripts/Inference/run_main_experiment.py --prompt_engineering_technique cot --rag 1 --k 5 
   ```
   - **Instructions**:
   1. Ensure `Data/Test/test.csv` contains the test dataset.
   2. For RAG, ensure relevant context data is in `Data/Documents/Embedded/index_merged`.
   3. Results will be saved in `Results/Experiment[experiment_nr]`.

3. `run_real_prompts_experiment.py`
   - **Purpose**: Evaluates specified model configurations on the `RealPrompts` dataset.
   - **Usage**: Run from the root directory with arguments:
   ```bash
   --experiment_nr
   --model
   --prompt_engineering_technique 
   --rag
   --k
   ```
   Allowed values are in the `parse_arguments` function. For example, running the base model with CoT and RAG:
   ```bash
   python Scripts/Inference/run_real_prompts_experiment.py --prompt_engineering_technique cot --rag 1 --k 5 
   ```
   - **Instructions**:
   1. Ensure `Data/Prompts/RealPrompts` contains necessary prompt files.
   2. For RAG, ensure relevant context data is in `Data/Documents/Embedded/index_merged`.
   3. Results will be saved in `Results/RealPrompts`.
