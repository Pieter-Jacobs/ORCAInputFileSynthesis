import rdkit.Chem as chem
import selfies as sf
from rdkit.Chem.Descriptors import NumRadicalElectrons
import random
from Classes.Helpers.BasisSetHandler import BasisSetHandler
from Classes.Helpers.ORCAInputFileManipulator import ORCAInputFileManipulator
from Classes.Helpers.ORCADocumentationHandler import ORCADocumentationHandler
from Data.Manual.ExtractedDocumentation import keywords_simple_input

from abc import ABC, abstractmethod


class Calculation(ABC):
    def __init__(self, xyz: str, molecule_file: str, molecule_type: str, add_solvation=False):
        self.keywords = []
        self.input_blocks = []
        self.molecule_file = molecule_file
        self.molecule_type = molecule_type
        self.hf_type = self.determine_hf_type()
        self.basisSetHandler = BasisSetHandler(xyz)
        if add_solvation:
            self.add_solvent()

    @abstractmethod
    def process_keywords(self):
        pass

    @abstractmethod
    def process_input_blocks(self):
        pass

    @abstractmethod
    def add_aux_basis_sets_to_keywords(self):
        pass

    def generate_input_file(self):
        input_file = "!" + " ".join(self.keywords) + "\n"
        input_file += "\n".join(self.input_blocks)

        input_file = ORCAInputFileManipulator.add_xyz(
            input_file, molecule_file=self.molecule_file, molecule_type=self.molecule_type)
        return input_file

    def determine_hf_type(self):
        """Determine the hartree fock type to use for a calculation. This is necassary for all hybrid-DFT calculations as well.
            Return the hartree fock type."""
        if self.molecule_type == 'Molecules':
            return 'rhf'
        return random.choice(['uhf', 'rohf'])

    def add_solvent(self):
        solvent = ORCADocumentationHandler.choose_random_keyword(
            keywords_simple_input.solvent_types)
        self.keywords.append(solvent)
