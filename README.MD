# Using Large Language Models for Domain Specific Language Synthesis: A Case Study for Quantum Chemistry Simulations with ORCA
This repository encompasses all code that was used to run the experiments described the paper with the same title shown above.
Aside from the the code of our system architecture, we include datasets described in the study, which can now be used in further research. 
Moreover, the repository contains some general helpful classes.

To reproduce the results from our study, we refer you to the `Scripts` folder, where more is explained on the scripts we use to run our experiments 
and gather our data. To get more insight into the classes used, and how one can implement use them in their own research we refer you to the `Classes` folder.
Lastly, one could inspect and extract the different datasets we used in the `Data` folder, where all datasets available are explained as well.

One general thing to note is that to be able to use the code in this repository, one should have configured their own OpenAI API key
in their system path. 

Furthermore, to be sure that you can run all code you can run the following:
```bash
pip install rdkit langchain basis-set-exchange pandas selfies beautifulsoup4 fpdf pypdf openai molmod basis-set-exchange scikit-learn glob shutil psutil sacrebleu langchain tiktoken
```