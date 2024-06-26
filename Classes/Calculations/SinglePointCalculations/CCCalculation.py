from Classes.Calculations.Calculation import Calculation
from Data.ExtractedDocumentation import keywords_simple_input
from Classes.Helpers.ORCADocumentationHandler import ORCADocumentationHandler
import random

random.seed(2000)


class CCCalculation(Calculation):
    """ Initializes a single point Coupled Cluster calculation.

    Parameters:
    - xyz: coordinate-block of the used molecule.
    - molecule_file: file containing molecule data.
    - molecule_type: Molecule or MoleculeRadical, used to determine what type of molecule is used
    - add_solvation: boolean indicating whether to add a random solvation model.
    - use_densities: boolean indicating whether to randomly alter the normally used densities.
    """

    def __init__(self, xyz, molecule_file, molecule_type, add_solvation=False,
                 use_densities=False):
        super().__init__(xyz, molecule_file, molecule_type, add_solvation)
        self.functional = self.choose_functional()
        self.use_densities = use_densities

    def choose_functional(self):
        """Chooses a random functional from the available ones for coupled cluster calculations."""
        functional = ORCADocumentationHandler.choose_random_keyword(keywords_simple_input.ci_type + "\n"
                                                                    + keywords_simple_input.local_correlation_mcdi_methods
                                                                    + keywords_simple_input.autoci_methods) if self.hf_type != 'rohf' else random.choice(['dlpno-ccsd', 'dlpno-ccsd(t)', 'dlpno-ccsd(t1)'])
        return functional

    def process_keywords(self):
        """Implements all necessary keywords for a CC calculation."""
        self.keywords.extend(['tightscf',
                              self.basisSetHandler.basis_set,
                              self.functional,
                              self.hf_type,
                              "uno" if self.molecule_type == 'MoleculesRadical' else None,
                              self.choose_accuracy_control() if 'pno' in self.functional else None,
                              ])
        # Remove all None, these were not defined in this calculation
        self.keywords = list(filter(lambda x: x is not None, self.keywords))
        self.add_aux_basis_sets_to_keywords()

    def process_input_blocks(self):
        """Appends the input blocks necassary for a CC calculation 
        Coupled cluster is post-HF method so always needs a converged wavefunction."""
        self.input_blocks.append("%scf ConvForced true end")
        self.input_blocks.append(self.create_mdci_input_block())

    def choose_accuracy_control(self):
        return 'tightpno'  # We always use tight accuracy control

    def add_aux_basis_sets_to_keywords(self):
        """Adds the necassary auxilary basis sets based on chosen keywords. CC calculations always need a /c basis set."""
        c_basis_set, is_new_aux = self.basisSetHandler.get_aux_basis_set("c")
        if is_new_aux:
            self.keywords.append(c_basis_set)
        if 'f12' in self.functional:
            f12_basis_set, is_new_aux = self.basisSetHandler.get_f12_basis_set()
            if is_new_aux:
                self.keywords.append(f12_basis_set)

    def create_mdci_input_block(self):
        """Creates the input block specific to the multi-determinant coupled cluster calculations."""
        input_block = "%mdci"
        input_block += ("\nlocRandom 0")
        input_block += (f"\ndensity {random.choice(['linearized', 'unrelaxed', 'orbopt'] if not 'ccsd(t)' in self.functional else [
                        'linearalized', 'orbopt'])}") if self.use_densities else ""
        input_block += ("\nUseQROs true") if self.molecule_type == 'MoleculesRadical' else ''
        input_block += "\nend"
        return input_block
