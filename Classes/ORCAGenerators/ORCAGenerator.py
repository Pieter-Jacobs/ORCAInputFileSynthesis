from Classes.Helpers.OrcaInputFileManipulator import OrcaInputFileManipulator
import os
from abc import ABC, abstractmethod


class ORCAGenerator(ABC):
    def __init__(self, save_folder, input_file_prefix, output_folder="Orca Output"):
        self.save_folder = save_folder
        self.output_folder = output_folder
        self.generated_input_files = [OrcaInputFileManipulator.remove_xyz(
            OrcaInputFileManipulator.remove_smiles_comment(
                OrcaInputFileManipulator.read_file(os.path.join(save_folder, filename))))
            for filename in os.listdir(save_folder) if os.path.isfile(os.path.join(save_folder, filename))]
        self.n_input_files_generated = 0
        self.input_file_prefix = input_file_prefix

    def generate_input_files(self, N, generation_params={"accept_warnings": True}, few_shot=False, save_warnings=True, save_errors=True):
        while self.n_input_files_generated < N:
            succes, input_file = self.generate_input_file(
                **generation_params) if not few_shot else self.generate_input_file_few_shot(n_shot=5, **generation_params)
            if succes:
                self.generated_input_files.append(OrcaInputFileManipulator.remove_xyz(
                    OrcaInputFileManipulator.remove_smiles_comment(input_file=input_file)))
                if save_warnings:
                    self.write_warnings_to_file(input_file=input_file)
            elif not succes and save_errors and input_file is not None:
                self.write_errors_to_file(input_file=input_file)
            self.n_input_files_generated += succes

    def generate_input_file_few_shot(self, accept_warnings, n_shot):
        input_file = self.generate_input_file()
        for shot in n_shot:
            pass  # @TODO improve based on errors
        return input_file

    def add_parallelization(self, input_file, n_pal):
        index = input_file.find('!') + 1
        exclamation_mark = input_file[:index]  # Can have whitespace
        rest_of_keywords = input_file[index:]
        return f"{exclamation_mark.strip()}pal{n_pal} {rest_of_keywords.strip()}"

    @ abstractmethod
    def generate_input_file(self, accept_warnings):
        pass

    def get_warnings(self, input_file_name):
        try:
            warnings = OrcaInputFileManipulator.extract_warnings(OrcaInputFileManipulator.read_file(os.path.relpath(
                os.path.join(self.output_folder,
                            input_file_name,
                            f"{input_file_name}_completed.txt"), os.getcwd())))
            return warnings
        except: 
            return [""]

    def write_warnings_to_file(self, input_file, save_path="warnings.txt"):
        warnings = self.get_warnings(f"{self.input_file_prefix}_{
                                     len(self.generated_input_files) - 1}.inp")
        OrcaInputFileManipulator.write_file(save_path, input_file + "\n" + ("\n".join([" ".join(
            map(str, tup)) for tup in warnings])) + "\n" + "-----------------" + "\n", writing_type="a")

    def write_errors_to_file(self, input_file, save_path="errors.txt"):
        input_file_name = f"{self.input_file_prefix}_{
            len(self.generated_input_files)}.inp"
        try:
            error = OrcaInputFileManipulator.read_file(os.path.relpath(
                os.path.join(self.output_folder,
                            input_file_name,
                            f"{input_file_name}_error.txt"), os.getcwd()))
            OrcaInputFileManipulator.write_file(
                save_path, input_file + "\n" + "\n".join(error.splitlines()[-20:]) + "\n" + "-----------------" + "\n", writing_type="a")
        except:
            pass
        
    def save_inp_to_file(self, input_file):
        input_file_name = f"{self.input_file_prefix}_{
            len(self.generated_input_files)}.inp"
        data_folder = os.path.relpath(self.save_folder, os.getcwd())
        input_file_path = os.path.join(data_folder, input_file_name)
        OrcaInputFileManipulator.write_file(input_file_path, input_file)
        return input_file_name, input_file_path
