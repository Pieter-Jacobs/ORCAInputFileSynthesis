import sys
import os
# Add the parent directory (project_root) to the Python path
sys.path.append(os.getcwd())
import hashlib
from Classes.Helpers.OrcaManualManipulator import OrcaManualManipulator
from Classes.Helpers.BasisSetHandler import BasisSetHandler
import random

def replace_basis_set(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        with open(file_path, 'r') as file:
            content = file.read()
        xyz = OrcaManualManipulator.extract_input_file_coordinates(content)[0]
        basisSetHandler = BasisSetHandler(xyz)
        # Replace all instances of 'STO-3G' with the replacement string
        modified_content = content.replace('STO-3G', random.choice(basisSetHandler.possible_basis_sets).lower())
        # # Write the modified content back to the file
        with open(file_path, 'w') as file:
            file.write(modified_content)

def ensure_unique_files(folder):
    seen_hashes = set()

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                file_hash = hashlib.sha256(file.read()).hexdigest()
                
            if file_hash in seen_hashes:
                print(f"Deleted duplicate file: {filename}")
                os.remove(file_path)
            else:
                seen_hashes.add(file_hash)

def rename_data(folder, name):
    # Check if folder exists
    if not os.path.isdir(folder):
        print(f"Error: Folder '{folder}' does not exist.")
        return

    # Iterate over files in the folder
    for i, filename in enumerate(os.listdir(folder)):
        file_path = os.path.join(folder, filename)
        # Check if the file is a regular file
        if os.path.isfile(file_path):
            os.rename(file_path, file_path.removesuffix(filename) + f"{name}_{i}.inp")

def clean_generated_data():
    # replace_basis_set(os.path.join("Data", "Generated", "InputFilesRuleBased"))
    # ensure_unique_files(os.path.join("Data", "Generated", "InputFilesFromManual"))
    rename_data(os.path.join("Data", "Generated", "InputFilesFromManual"), "manual_based")

if __name__ == "__main__":
    clean_generated_data()