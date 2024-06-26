import hashlib
import sys
import os
# Add the parent directory (project_root) to the Python path
import re
sys.path.append(os.getcwd())
from Classes.Helpers.OrcaInputFileManipulator import OrcaInputFileManipulator


def remove_unnecessary_empty_lines(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    # Replace multiple whitespace characters including double newlines with a single space
    cleaned_content = re.sub(r'\n\s*\n+', '\n', content).strip()

    with open(file_path, 'w') as file:
        file.write(cleaned_content)


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


def rename_data(folder):
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
    # Check if the file is a regular file
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        new_content = OrcaInputFileManipulator.replace_xyz(content)[0]
        with open(file_path, 'w') as file:
            file.write(new_content)


def remove_extra_defgrid3(filename):
    # Read the file contents
    with open(filename, 'r') as file:
        content = file.read()

    keywords, _ = OrcaInputFileManipulator.extract_keywords(content)

    # Count the occurrences of 'defgrid3'
    defgrid3_count = keywords.count('defgrid3')
    if defgrid3_count > 1:
        new_content = re.sub(r'\bdefgrid3\b ', '', content, count=1)
        with open(filename, 'w') as file:
            file.write(new_content)


def update_grid_keywords(folder):
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

            _, keyword_lines = OrcaInputFileManipulator.extract_keywords(
                content)

            # Remove words starting with 'grid' and 'gridx'
            for keyword_line in keyword_lines:
                modified_keyword_line = re.sub(
                    r'\b(grid|gridx)\d+\b ', '', keyword_line, flags=re.IGNORECASE)
                # If there is an outdated GRID keyword
                if modified_keyword_line != keyword_line:
                    modified_keyword_line = modified_keyword_line + " defgrid3"
                    # Remove it
                    content = content.replace(
                        keyword_line, modified_keyword_line)

            # Write modified content back to the file
            with open(file_path, 'w') as file:
                file.write(content)


def remove_first_comment(file_path):
    """Made this because I mistakenly added comments twice about what molecule was used."""
    # Define the regex pattern to match the first comment (#) of the two consecutive comment lines and the xyz block
    pattern = r'(#.*)\n#.*\n\*\s?xyz'
    if os.path.isfile(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        try:
            wrong_comment = re.search(pattern, content).group(1)
            modified_content = re.sub(wrong_comment, "", content)
            # Write modified content back to the file
            with open(file_path, 'w') as file:
                file.write(modified_content)
        except:
            pass

def replace_placeholders(file_path):
    """
    Remove comments from an ORCA input file using regex.
    """
    with open(file_path, 'r') as file:
        content = file.read()
    
    cleaned_content = content.replace("mmmmm", "2000")
    cleaned_content = cleaned_content.replace("ccccc", "6")
    
    with open(file_path, 'w') as file:
        file.write(cleaned_content)


def make_input_file_lower_case(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    with open(file_path, 'w') as file:
        file.write(content.lower())


def remove_comments(file_path):
    """
    Remove comments from an ORCA input file using regex.
    """

    # Regex pattern to match comments
    comment_pattern = r'#.*\n(?!\*[\s]?xyz)'

    with open(file_path, 'r') as file:
        content = file.read()
    cleaned_content = re.sub(comment_pattern, "",
                             content)
    with open(file_path, 'w') as file:
        file.write(cleaned_content)


def clean_extracted_data():
    folder = os.path.join("Data", "Extracted")
    # ensure_unique_files(folder)
    # rename_data(folder)
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        replace_placeholders(file_path)
        # remove_comments(file_path)
        # remove_unnecessary_empty_lines(file_path)
        # make_input_file_lower_case(file_path)
        # change_xyz(file_path)
        # remove_extra_defgrid3(os.path.join(folder, filename))


if __name__ == "__main__":
    clean_extracted_data()
