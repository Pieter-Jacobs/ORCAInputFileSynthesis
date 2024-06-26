import hashlib
import sys
import os
# Add the parent directory (project_root) to the Python path
import re
sys.path.append(os.getcwd())
from Classes.Helpers.ORCAInputFileManipulator import ORCAInputFileManipulator


def remove_unnecessary_empty_lines(file_path):
    """Removes empty newlines from a file"""
    with open(file_path, 'r') as file:
        content = file.read()
    # Replace multiple whitespace characters including double newlines with a single space
    cleaned_content = re.sub(r'\n\s*\n+', '\n', content).strip()

    with open(file_path, 'w') as file:
        file.write(cleaned_content)


def ensure_unique_files(folder):
    """Removes any ORCA input files with the same keywords and input blocks"""
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


def rename_data(folder):
    """Renames the data to a standardized format"""
    # Check if folder exists
    if not os.path.isdir(folder):
        print(f"Error: Folder '{folder}' does not exist.")
        return

    # Iterate over files in the folder
    for i, filename in enumerate(os.listdir(folder)):
        file_path = os.path.join(folder, filename)
        # Check if the file is a regular file
        if os.path.isfile(file_path):
            os.rename(file_path, file_path.removesuffix(
                filename) + f"extracted_{i}.inp")


def change_xyz(file_path):
    """Replaces the coordinate block of an ORCA input file with its corresponding smiles"""
    # Check if the file is a regular file
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        new_content = ORCAInputFileManipulator.replace_xyz(content)[0]
        with open(file_path, 'w') as file:
            file.write(new_content)


def update_grid_keywords(folder):
    """Replaces the outdated grid keywords from ORCA version 4 with the more recent defgrid from ORCA version 5."""
    # Check if folder exists
    if not os.path.isdir(folder):
        print(f"Error: Folder '{folder}' does not exist.")
        return

    # Iterate over files in the folder
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        # Check if the file is a regular file
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                content = file.read()

            _, keyword_lines = ORCAInputFileManipulator.extract_keywords(
                content)

            # Remove words starting with 'grid' and 'gridx'
            for keyword_line in keyword_lines:
                modified_keyword_line = re.sub(
                    r'\b(grid|gridx)\d+\b ', '', keyword_line, flags=re.IGNORECASE)
                # If there is an outdated GRID keyword, we replace it
                if modified_keyword_line != keyword_line:
                    modified_keyword_line = modified_keyword_line + " defgrid3"
                    content = content.replace(
                        keyword_line, modified_keyword_line)

            # Write modified content back to the file
            with open(file_path, 'w') as file:
                file.write(content)


def make_input_file_lower_case(file_path):
    """Lower cases a string in a given file path"""
    with open(file_path, 'r') as file:
        content = file.read()
    with open(file_path, 'w') as file:
        file.write(content.lower())


def remove_comments(file_path):
    """Remove comments from an ORCA input file using regex."""

    # Regex pattern to match comments
    comment_pattern = r'#.*\n(?!\*[\s]?xyz)'

    with open(file_path, 'r') as file:
        content = file.read()
    cleaned_content = re.sub(comment_pattern, "",
                             content)
    with open(file_path, 'w') as file:
        file.write(cleaned_content)


def clean_extracted_data():
    """Clean all data from the ORCAExtracted folder."""
    folder = os.path.join("Data", "ORCAExtracted")
    ensure_unique_files(folder)
    rename_data(folder)
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        remove_comments(file_path)
        remove_unnecessary_empty_lines(file_path)
        make_input_file_lower_case(file_path)
        change_xyz(file_path)


if __name__ == "__main__":
    clean_extracted_data()
