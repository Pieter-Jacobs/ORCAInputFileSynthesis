# Data

This folder encompasses all datasets used in our research. Below, we explain its structure. Note that `periodic_table.py` holds the different elements with their associated numbers, which is used to determine what molecules can be used for which data.

## Documents

This folder contains the documents used by RAG to add external context to the user prompt. Note that the ORCA manual is copyrighted, and that we are not its copyright holders. The copyright notice is provided in the README in the `Documents` folder. We provide the PDF file of the manual in `Documents/Regular` folder. The manual can also be downloaded from the ORCA forum: https://orcaforum.kofo.mpg.de/index.php. Here, more recent versions of the manual are provided as well. 

Moreover, while we provide a PDF file with the scraped pages of the ORCA input library website, the user can also scrape it themselves by running `Scripts/Scraping/input_file_library_scraper.py`.

The folder also contains the FAISS embeddings used for RAG in the `Documents/Embedded` folder. These can also be recreated by the user by running the script to process the manual and the input file library documents (`embed.py`).

## ExtractedDocumentation

Here, we store all the documentation we extracted from the ORCA manual, split into the following categories: 
1. Basis sets with their descriptions
2. Input block options with their descriptions
3. Density functional keywords with their descriptions
4. Other keywords with their descriptions
5. Possible setting lines for different options

## Finetuning

Here, we hold our final brute-force, manual-based, and rule-based datasets processed for fine-tuning. Each sample is in the following format:
```
{
  system: [SYSTEM PROMPT],
  user: [USER PROMPT],
  assistant: [LABEL]
}
```
The label can be either an ORCA input file for 'basic' prompt engineering or a CoT reasoning process for 'cot' prompt engineering.

## Generated

This folder holds the 500 input files we generated with our brute-force, manual-based, and rule-based approaches. The `Evaluation` folder is used during evaluation to hold the predicted input files so ORCA can run them.

## Molecules & MoleculesRadical

These two folders hold the `Gen3Molecules` dataset described in our study. They contain valid coordinate blocks for molecules with up to three atoms. The first folder holds regular molecules, while the second contains molecules with an abstracted hydrogen atom.

## ORCAExtracted & Test

These folders hold our real-world data, referred to in our study as `ORCAExtracted`. The input files were extracted both from IoChem and internally within the Pollice Research Group and are found in the `ORCAExtracted` folder. The `Test` folder holds these same input files, but with user prompts associated with them, making them ready for evaluation. Both the test and validation sets have associated .csv files, with the validation set also having a .jsonl files that can be used in a finetuning job.

## Prompts

This folder holds both the `RealPrompts` data (prompts written by chemistry experts) as well as the system prompts used in our prompt engineering experiments, those employed for RAG, and synthetic prompt creation.