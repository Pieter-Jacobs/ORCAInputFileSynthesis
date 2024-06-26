import sys
import os
# Add the parent directory (project_root) to the Python path
sys.path.append(os.getcwd())
import hashlib

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
    """Renames the data in a folder to a desired name, together with a suffix indicating its index."""
    
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
    ensure_unique_files(os.path.join("Data", "Generated", "InputFilesFromManual"))
    rename_data(os.path.join("Data", "Generated", "InputFilesFromManual"), "manual_based")

if __name__ == "__main__":
    clean_generated_data()