from Classes.ORCAGenerators.ORCAGenerator import ORCAGenerator
from Classes.Helpers.ORCAInputFileManipulator import ORCAInputFileManipulator
from Classes.Helpers.ORCAManualManipulator import ORCAManualManipulator
from Classes.Helpers.ORCARunner import ORCARunner
import os
import random


class ManualBasedORCAGenerator(ORCAGenerator):
    def __init__(self, save_folder, path_to_manual=f'Data{os.sep}Documents{os.sep}Regular{os.sep}orca_manual_5_0_4.txt',
                 input_file_prefix="manual_based", output_folder="Orca Output"):
        super().__init__(save_folder, input_file_prefix, output_folder)
        orca_manual_text = ORCAInputFileManipulator.read_file(path_to_manual)
        self.input_blocks, _ = ORCAManualManipulator.extract_input_file_blocks(
            orca_manual_text)
        _, self.keyword_lines = ORCAManualManipulator.extract_known_keywords(
            orca_manual_text)

    def generate_input_file(self, accept_warnings, add_input_block=False):
        keyword_line = random.choice(self.keyword_lines)
        input_block = random.choice(
            self.input_blocks) if add_input_block else ""

        input_file = f"!{" ".join(keyword_line)}\n{input_block}"
        input_file = self.add_parallelization(input_file=input_file,
                                              n_pal=6)
        input_file = ORCAInputFileManipulator.add_xyz(input_file)
        # Check if the file is unique, otherwise no point in running it
        if ORCAInputFileManipulator.remove_xyz(ORCAInputFileManipulator.remove_smiles_comment(input_file)) not in self.generated_input_files:
            input_file_name, input_file_path = self.save_inp_to_file(
                input_file)

            completed = ORCARunner.run_orca(
                self.save_folder, input_file_name, self.output_folder, r"C:\Users\Pieter\Orca\orca.exe")

            if completed != 0:
                os.remove(input_file_path)
                return False, input_file
            else:
                if not accept_warnings and len(self.get_warnings(input_file_name=input_file_name)) > 0:
                    return False, None
                print(f"Input file saved to {input_file_path}")
            return True, input_file
        return False, None
