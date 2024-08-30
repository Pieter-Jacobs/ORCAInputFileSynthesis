# Using Large Language Models for Domain Specific Language Synthesis: A Case Study for Quantum Chemistry Simulations with ORCA

This repository encompasses all code used to run the experiments described in the study titled *"Developing Large Language Models for Quantum Chem-
istry Simulation Input Generation"*.  

In addition to the code for our system architecture, we include the datasets described in the study, which can be used for further research. The repository also contains some generally helpful classes.

To reproduce the results from our study, refer to the `Scripts` folder, where we explain the scripts used to run our experiments and gather data. For more insight into the classes used and how to implement them in your own research, refer to the `Classes` folder. We for instance show how to easily use our rule-based system to generate different calculations. Additionally, you can inspect and extract the various datasets we used from the `Data` folder, where all available datasets are explained. The `Orca Output` folder stores all output files gathered from running ORCA calculations.

One important note is that to use the code in this repository, you should configure your own OpenAI API key in your system path. Moreover, to use RAG, one should scrape the ORCA input library with our provided script and add the ORCA manual to the `Documents/Regular` folder. We do not publish this here as we are not the writers.

Furthermore, to ensure you can run all the code, you can download the necessary dependencies by running the following:
```bash
pip install rdkit langchain basis-set-exchange pandas selfies beautifulsoup4 fpdf pypdf openai molmod basis-set-exchange scikit-learn psutil sacrebleu langchain tiktoken
```