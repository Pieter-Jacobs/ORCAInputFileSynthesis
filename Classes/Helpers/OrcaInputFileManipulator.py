
import random
import os
import re
import selfies as sf
from molmod import Molecule
from rdkit.Chem import MolFromSmiles
from Classes.Helpers.ORCAManualManipulator import ORCAManualManipulator


class ORCAInputFileManipulator:
    """Static class that is able to extract and manipulate different parts of ORCA input files."""

    def get_random_xyz(max_atoms=4):
        """Returns a random xyz coordinate block from the molecules dataset, together with the file and molecule type"""
        found_molecule = False
        molecule_type = random.choice(['Molecules', 'MoleculesRadical'])
        while not found_molecule:
            molecule_file = random.choice(os.listdir(
                os.path.abspath(f'Data{os.sep}{molecule_type}')))
            # We search for a molecule that is of the requested number of atoms
            try:
                molecule_smiles = sf.decoder(sf.encoder(
                    molecule_file.removesuffix('.txt')))
                molecule = MolFromSmiles(molecule_smiles)
                n_atoms = molecule.GetNumAtoms(onlyExplicit=False)
                if n_atoms <= max_atoms:
                    found_molecule = True
            except:
                pass
        with open(f"{os.path.abspath(f'Data{os.sep}{molecule_type}')}{os.sep}{molecule_file}", 'r') as f:
            xyz = f.read()
        return xyz, molecule_file, molecule_type

    def add_xyz(input_file, xyz=None, molecule_file=None, molecule_type=None):
        """Add coordinates to an input file, based on a file or on a given xyz, or else randomly"""
        if molecule_type is None:
            molecule_type = random.choice(['Molecules', 'MoleculesRadical'])
        if xyz:
            input_file = input_file + "\n" + xyz
            return input_file
        if molecule_file is None:
            molecule_file = random.choice(os.listdir(
                os.path.abspath(f'Data{os.sep}{molecule_type}')))

        with open(f"{os.path.abspath(f'Data{os.sep}{molecule_type}')}{os.sep}{molecule_file}", 'r') as f:
            new_xyz = f.read()
        input_file = input_file + "\n" + '#' + \
            molecule_file.removesuffix(".txt").replace(
                "#", "(hashtag)") + "\n" + new_xyz
        return input_file

    def replace_xyz(input_file):
        """Replaces the coordinate block in an input file with its corresponding smiles"""
        molecule_type = "Molecules"
        if "UKS" in input_file or "uks" in input_file or "UHF" in input_file or "uhf" in input_file or "ROHF" in input_file or "rohf" in input_file or "ROKS" in input_file or "roks" in input_file:
            molecule_type = "MoleculesRadical"
        coordinate_pattern = r'\*\s?xyz.*?\*'
        file_pattern = r'\*\s?xyzfile.*?\n'
        combined_pattern = f'({coordinate_pattern}|{file_pattern})'
        matches = re.findall(combined_pattern, input_file, re.DOTALL)
        for match in matches:
            molecule_file = random.choice(os.listdir(
                os.path.abspath(f'Data{os.sep}{molecule_type}')))
            with open(f"{os.path.abspath(f'Data{os.sep}{molecule_type}')}{os.sep}{molecule_file}", 'r') as f:
                new_xyz = f.read()
            new_xyz = '#' + \
                molecule_file.removesuffix(".txt").replace(
                    "#", "(hashtag)") + "\n" + new_xyz
            input_file = input_file.replace(match, new_xyz)
        return input_file, matches

    def remove_xyz(input_file):
        """Removes the coordinate block from an ORCA input file"""
        coordinate_pattern = r'\*\s?xyz.*?\*'
        file_pattern = r'\*\s?xyzfile.*?\n'
        combined_pattern = f'({coordinate_pattern}|{file_pattern})'
        matches = re.findall(combined_pattern, input_file, re.DOTALL)
        for match in matches:
            input_file = input_file.replace(match, "")
        return input_file

    def remove_smiles_comment(input_file):
        """Removes the SMILES comment we created from an ORCA input file"""
        comment_pattern = r'(#.*\n)\*[\s]?xyz'
        matches = re.findall(comment_pattern, input_file, re.DOTALL)
        for match in matches:
            input_file = input_file.replace(match, "")
        return input_file

    def extract_molecule(xyz, n_atoms):
        """Extracts a molecule object from a provided coordinate block"""

        xyz_block = f"{n_atoms}\n\n{'\n'.join(xyz.splitlines()[1:-1])}"
        with open('molecule.xyz', 'w') as f:
            f.write(xyz_block)
        molecule = Molecule.from_file('molecule.xyz')
        os.remove('molecule.xyz')
        return molecule

    def extract_molecule_smiles(input_file):
        """Extract the SMILES out of an ORCA input file we created"""
        try:
            return re.search(r'#(.*)\n\*[\s]?xyz', input_file).group(1)
        except:
            return False

    def extract_elements(input_file):
        """Extract the different atoms out of an ORCA input file"""

        coordinates = ORCAManualManipulator.extract_input_file_coordinates(
            input_file)
        elements_pattern = r'\b[A-Z][a-z]?\b'
        elements = re.findall(elements_pattern, coordinates[0])
        return elements

    def extract_input_blocks(input_file):
        """Extract all parts of input blocks out of an ORCA input file"""

        options = []
        input_blocks = []
        settings = []
        # First extract MaxCore, this is an option that is on one line and has no 'end'
        input_file_wo_maxcore = re.sub(
            r'%maxcore.*?\n', "", input_file, flags=re.DOTALL | re.IGNORECASE)
        if input_file != input_file_wo_maxcore:
            options.append("maxcore")

        input_blocks_raw = re.findall(
            r'(%\s*\w+\n?.*?\n?end)\n', input_file_wo_maxcore, flags=re.DOTALL | re.IGNORECASE)

        for input_block in input_blocks_raw:
            try:
                options.append(
                    re.search(r'%\s*(\w+)', input_block).group(1).lower())
                settings.append(re.search(r'%\s*\w+(.*?)end',
                                input_block, flags=re.DOTALL).group(1).lower())
                input_blocks.append(input_block)
            except:
                pass
        # prevent empty strings
        options = [option for option in options if option != ""]
        settings = [setting for setting in settings if setting != ""]
        return input_blocks_raw, options, settings

    def extract_keywords(text):
        """Extract all words out of lines starting with !, thus extracting keywords"""
        keywords = []
        keyword_lines = re.findall(
            r'![^\n\r]*', text)
        # Remove "!"
        keyword_lines = [re.sub("[!\b]", "", line) for line in keyword_lines]
        keywords.extend([keyword.lower()
                        for line in keyword_lines for keyword in line.split()])
        # No empty strings
        keywords = [keyword for keyword in keywords if keyword != ""]
        return keywords, keyword_lines

    def extract_warnings(orca_output_file):
        """Extracts ORCA warnings out of a given output file"""
        warning_block_pattern = r'''================================================================================
                                        WARNINGS
                       Please study these warnings very carefully!
================================================================================(.*?)================================================================================'''
        warning_block = re.search(
            warning_block_pattern, orca_output_file, flags=re.DOTALL).group(1)

        # Find all warnings, group the warning and what Orca does automatically to fix it
        warning_pattern = r'WARNING:(.*?)(?:===>)(.*?)(?:WARNING|INFO)'
        warnings_with_changes = re.findall(
            warning_pattern, warning_block, flags=re.DOTALL)

        return warnings_with_changes

    def read_file(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()

    def write_file(file_path, content, writing_type="w"):
        with open(file_path, writing_type, encoding="utf-8") as file:
            file.write(content)
