from Classes.ORCAGenerators.ORCAGenerator import ORCAGenerator
from Classes.Helpers.OrcaDocumentationHandler import OrcaDocumentationHandler
from Classes.Helpers.OrcaInputFileManipulator import OrcaInputFileManipulator
from Classes.Helpers.OrcaRunner import OrcaRunner
import random
import os
import json


class BruteForceORCAGenerator(ORCAGenerator):
    def __init__(self, save_folder, max_len_keywords, max_len_input_blocks,
                 input_file_prefix="brute_force", output_folder="Orca Output"):
        super().__init__(save_folder, input_file_prefix, output_folder)
        self.max_len_keywords = max_len_keywords
        self.max_len_input_blocks = max_len_input_blocks
        self.keywords_simple_input = list(
            OrcaDocumentationHandler.get_keywords_simple_input_documentation().keys())
        self.keywords_dft = list(
            OrcaDocumentationHandler.get_density_functional_documentation().keys())
        self.basis_sets = list(
            OrcaDocumentationHandler.get_basis_set_documentation().keys())

    def generate_input_file(self, accept_warnings, add_input_block=True, use_df=None):
        add_input_block = random.choice(
            [True, False]) if add_input_block is None else add_input_block
        use_df = random.choice([True, False]) if use_df is None else use_df

        # Randomly choose a subset of entries from the simple input dictionary
        random_simple_input_count = random.randint(1, self.max_len_keywords)
        simple_input_entries = random.sample(
            self.keywords_simple_input, random_simple_input_count)
        basis_set = random.choice(self.basis_sets)
        density_functional = random.choice(self.keywords_dft)
        input_block = self.generate_random_input_block() if add_input_block else ""

        input_file = f"!{basis_set} {" ".join(simple_input_entries)}{
            density_functional if use_df else ""}\n{input_block}"
        input_file = self.add_parallelization(input_file=input_file,
                                              n_pal=6)
        input_file = OrcaInputFileManipulator.add_xyz(input_file)

        # Check if the file is unique
        if OrcaInputFileManipulator.remove_xyz(OrcaInputFileManipulator.remove_smiles_comment(input_file)) not in self.generated_input_files:

            input_file_name, input_file_path = self.save_inp_to_file(
                input_file)

            completed = OrcaRunner.run_orca(
                self.save_folder, input_file_name, self.output_folder, r"C:\Users\Pieter\Orca\orca.exe")
            if completed != 0:
                os.remove(input_file_path)
                return False, input_file

            if not accept_warnings and len(self.get_warnings(input_file_name=input_file_name)) > 0:
                return False, None

            print(f"Input file saved to {input_file_path}")
            return True, input_file
        return False, None

    def generate_random_input_block(self):
        # Parse the JSON data
        with open('Data\Manual\ExtractedDocumentation\input_block_settings.json', 'r') as f:
            data = json.load(f)

        # Choose a random method
        method = random.choice(list(data.keys()))

        # Get the lines for the chosen method
        lines = data[method]

        # Construct the ORCA input block
        input_block = f"%{method}\n"
        for i in range(random.randint(1, self.max_len_input_blocks)):
            if len(lines) > 0:
                line = random.choice(lines)
                lines.remove(line)
                input_block += f"{line}\n"
        input_block += "end"
        return input_block
