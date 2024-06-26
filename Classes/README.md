# Classes

Here we highlight how users can make use of the implemented functionalities that could easily be transferred for use in further research on ORCA input file synthesis.

## Calculations
In building our rule-based data generation approach, we created classes that represent different ORCA calculations. The use of these is straightforward once you have the molecule you want to run the calculation for:

```python 
molecule_xyz = '''*xyz 0 1 
    H   0.349900000   0.000000000   0.000000000
    H  -0.349900000   0.000000000   0.000000000
    *
'''
molecule_file = '[H][H].txt'
calculation = DFTCalculation(molecule_xyz, molecule_file, 'Molecules')
calculation.process_keywords()
calculation.process_input_blocks()
input_file = calculation.generate_input_file()
```

The different settings one can employ in generation are found in the respective calculation classes and are also described in our study.

## Generators
The generator classes are used to generate a dataset using one of our three approaches (brute-force, manual-based, and rule-based). They can be used as follows:

```python 
# Brute-force
bf_generator = BruteForceORCAGenerator(saving_folder="Data", max_len_keywords=10, max_len_input_blocks=5)
bf_input_files = bf_generator.generate_input_files(100)

# Manual-based
mb_generator = ManualBasedORCAGenerator(saving_folder="Data")
mb_input_files = mb_generator.generate_input_files(100)

# Rule-based (DFT Excited States calculations)
rb_generator = RuleBasedORCAGenerator(saving_folder="Data")
rb_input_files = rb_generator.generate_input_files(100, generation_params={"accept_warnings": True, "calculation_type": "dft_es"})
```

## Helpers
There are various helper classes that can be employed in handling ORCA input files:
1. `BasisSetHandler`: Given a coordinate block, allows for retrieval of possible datasets, including associated auxiliary and f12 datasets.
2. `ORCADataset`: Simple class that allows for a dataset of input files to be transferred to different formats.
3. `ORCADocumentationHandler`: Allows for easy retrieval of our extracted documentation.
4. `ORCAInputFileManipulator`: Very useful static class for extracting and manipulating different parts of ORCA input files, mainly through the use of regular expressions. Example functionalities: 
    ```python 
    xyz_block = ORCAInputFileManipulator.get_random_xyz()
    keywords = ORCAInputFileManipulator.extract_keywords(input_file)
    input_blocks, options, settings = ORCAInputFileManipulator.extract_input_blocks(input_file)
    ```
5. `ORCAManualManipulator`: Similar to ORCAInputFileManipulator but less general as it is specifically aimed at extracting ORCA documentation from the ORCA manual.
6. `ORCARunner`: Used to run ORCA files and handle its output. Example functionality:
    ```python 
    return_code = ORCARunner.run_orca(data_folder="Data",  
        input_file_name="file_1.inp", 
        main_output_folder="Orca Output", 
        orca_executable="executables/orca.exe"
    )
    ```

## Model
This folder holds the following parts of our system architecture:
1. `Tester`: A project-specific class that is used for evaluation of our model with the described metrics in our study.
2. `Embedder`: Used for embedding documents and retrieving relevant context to add to a user prompt.
3. `OpenAIFinetuner`: Simple wrapper class that facilitates the use of the OpenAI SDK.

## PromptCreation
The `Prompter` class makes use of the extracted documentation to synthetically create prompts for an input file. One can use it as follows to generate a single prompt:

```python 
prompter = Prompter(contextual_prompt="You generate prompts based on ORCA input files", data_folder="Data")
prompt = prompter.create_prompt_from_input_file(input_file)
```
