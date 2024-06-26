from Classes.ORCAGenerators.ORCAGenerator import ORCAGenerator  # Importing necessary modules
from Classes.Helpers.ORCAInputFileManipulator import ORCAInputFileManipulator
from Classes.Helpers.ORCAManualManipulator import ORCAManualManipulator
from Classes.Helpers.ORCARunner import ORCARunner
import os
import random


class ManualBasedORCAGenerator(ORCAGenerator):
    """
    A class to generate ORCA input files based on the ORCA manual.

    Parameters:
        save_folder (str): Folder path where input files are saved.
        path_to_manual (str): Path to the ORCA manual text file.
        input_file_prefix (str): Prefix for input file names.
        output_folder (str): Folder path where ORCA output files are stored.
        input_blocks (list): List of input blocks extracted from the ORCA manual.
        keyword_lines (list): List of known keyword lines extracted from the ORCA manual.
    """

    def __init__(self, save_folder, path_to_manual=f'Data{os.sep}Documents{os.sep}Regular{os.sep}orca_manual_5_0_4.txt',
                 input_file_prefix="manual_based", output_folder="Orca Output"):
        super().__init__(save_folder, input_file_prefix, output_folder)
        # Read ORCA manual text file and extract input blocks and keyword lines
        orca_manual_text = ORCAInputFileManipulator.read_file(path_to_manual)
        self.input_blocks, _ = ORCAManualManipulator.extract_input_file_blocks(
            orca_manual_text)
        _, self.keyword_lines = ORCAManualManipulator.extract_known_keywords(
            orca_manual_text)

    def generate_input_file(self, accept_warnings, add_input_block=False):
        """Generates an ORCA input file based on ORCA manual input blocks and keyword lines."""
        keyword_line = random.choice(self.keyword_lines)  # Randomly choose a keyword line
        input_block = random.choice(
            self.input_blocks) if add_input_block else ""  # Optionally choose a random input block

        # Construct the ORCA input file
        input_file = f"!{' '.join(keyword_line)}\n{input_block}"
        input_file = self.add_parallelization(input_file=input_file,
                                              n_pal=6)  # Add parallelization information
        input_file = ORCAInputFileManipulator.add_xyz(input_file)  # Add XYZ coordinates if needed

        # Check if the generated input file is unique
        if ORCAInputFileManipulator.remove_xyz(ORCAInputFileManipulator.remove_smiles_comment(input_file)) not in self.generated_input_files:
            input_file_name, input_file_path = self.save_inp_to_file(
                input_file)  # Save the input file

            completed = ORCARunner.run_orca(
                self.save_folder, input_file_name, self.output_folder, r"C:\Users\Pieter\Orca\orca.exe")  # Run ORCA simulation

            if completed != 0:  # Handle failed ORCA runs
                os.remove(input_file_path)
                return False, input_file
            else:
                if not accept_warnings and len(self.get_warnings(input_file_name=input_file_name)) > 0:
                    return False, None  # Handle warnings if not accepted
                print(f"Input file saved to {input_file_path}")  # Print success message
            return True, input_file  # Return success status and generated input file
        return False, None  # Return failure status if input file is not unique
