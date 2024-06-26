import random
from Classes.Calculations.SinglePointCalculations.DFTCalculation import DFTCalculation
from Classes.Calculations.SinglePointCalculations.HFCalculation import HFCalculation
from Classes.Calculations.SinglePointCalculations.CCCalculation import CCCalculation
from Data.ExtractedDocumentation import keywords_simple_input
from Classes.Helpers.ORCADocumentationHandler import ORCADocumentationHandler


class CCExcitedStatesCalculation(CCCalculation):
    """
    Implements a CC based excited states calculation.

    Parameters:
        xyz (str): The XYZ coordinates of the molecule.
        molecule_file (str): The file containing molecular information.
        molecule_type (str): The type of molecule (e.g., 'Molecules', 'MoleculesRadical').
        add_solvation (bool): Flag to add solvation effects.
        use_densities (bool): Flag to use densities in the calculation.
        use_triplets (bool): Flag to include triplet states.
        do_db_filter (bool): Flag to enable database filtering.
        use_QROs (bool): Flag to use quasi-restricted orbitals (QROs).
    """

    def __init__(self, xyz, molecule_file, molecule_type, add_solvation=False, use_densities=False,
                 use_triplets=False, do_db_filter=False, use_QROs=False):
        super().__init__(xyz, molecule_file, molecule_type, add_solvation, use_densities)
        self.use_triplets = use_triplets if self.hf_type == 'rhf' else False
        self.use_QROs = use_QROs if self.hf_type == 'uhf' else False
        self.do_db_filter = do_db_filter
        self.add_solvation = add_solvation

    def choose_functional(self):
        """Chooses a random functional suitable for excited state calculations."""
        functional = ORCADocumentationHandler.choose_random_keyword(
            keywords_simple_input.mdci_methods_for_excited_states)
        if functional == 'dlpno-steom-ccsd' and self.hf_type == 'uhf':
            functional = 'steom-ccsd'
        return functional

    def determine_hf_type(self):
        """Determines the Hartree-Fock type based on the molecule type."""
        if self.molecule_type == 'Molecules':
            return 'rhf'
        return 'uhf'

    def create_mdci_input_block(self):
        """Creates the, extended, MDCI input block for the calculation."""
        input_block = "%mdci"
        input_block += ("\nnroots 9")
        input_block += ("\nDoAlpha true") if self.molecule_type == "MoleculesRadical" and (
            self.functional == 'ip-eom-ccsd' or self.functional == 'ea-eom-ccsd') else ''
        # Recommended settings for eom-cc calculations (page 918)
        if self.functional == 'eom-ccsd' or self.functional == 'ip-eom-ccsd' or self.functional == 'ea-eom-ccsd':
            input_block += f"\nDoCOSXEOM true\nDoAOX3e true\nKCOpt {
                "KC_AOBLAS" if self.molecule_type == "Molecules" else "KC_AOX"}"
        if 'bt-pno' in self.functional and self.hf_type == 'rhf':
            input_block += ("\nDLPNOLINEAR true\nNEWDOMAINS true")
        if 'steom' in self.functional:
            input_block += ("\nuseQROs true") if self.use_QROs else ""
            input_block += ("\ndoDbFilter true") if self.do_db_filter else ""
            input_block += ("\ndoTriplet true") if self.use_triplets else ""
        input_block += ("\ndorootwise true") if self.functional == 'steom-dlpno-ccsd' else ''
        input_block += ("\nDoSOLV true") if self.add_solvation else ""
        input_block += ("\nlocRandom 0")
        input_block += (f"\ndensity {random.choice(['linearized', 'unrelaxed', 'orbopt'] if not 'ccsd(t)' in self.functional else [
                        'linearalized', 'orbopt'])}") if self.use_densities else ""
        input_block += ("\nUseQROs true") if self.molecule_type == 'MoleculesRadical' else ''
        input_block += "\nend"
        return input_block


class HFExcitedStatesCalculation(HFCalculation):
    """
    Implements an HF based excited states calculation.


    Parameters:
        xyz (str): The XYZ coordinates of the molecule.
        molecule_file (str): The file containing molecular information.
        molecule_type (str): The type of molecule (e.g., 'Molecules', 'MoleculesRadical').
        add_solvation (bool): Flag to add solvation effects.
        use_mp2 (bool): Flag to use MP2 perturbation theory.
        use_ri (bool): Flag to use the RI approximation.
        print_population (bool): Flag to print population analysis.
        use_densities (bool): Flag to use densities in the calculation.
        do_soc (bool): Flag to include spin-orbit coupling effects.
        use_triplets (bool): Flag to include triplet states.
        use_nacme (bool): Flag to calculate nonadiabatic coupling matrix elements.
        use_spin_flip (bool): Flag to perform spin-flip calculations.
    """

    def __init__(self, xyz, molecule_file, molecule_type, add_solvation=False,
                 use_mp2=False, use_ri=False,
                 print_population=False, use_densities=False, do_soc=False, use_triplets=False, use_nacme=False, use_spin_flip=False):
        super().__init__(xyz, molecule_file, molecule_type, add_solvation, use_mp2, use_ri)

        # General es options
        self.print_population = print_population
        self.use_densities = use_densities
        self.use_triplets = use_triplets if self.hf_type == 'rhf' else False
        # SOC does not allow for double hybrids, but dcorr needs this
        self.do_soc = do_soc if self.use_triplets and not print_population else False
        # triplets has to be turned off for nacme
        self.use_nacme = use_nacme if not use_triplets else False
        self.use_spin_flip = use_spin_flip if self.hf_type != 'rhf' else False

    def process_keywords(self):
        """Implements the keywords for an HF excited states calculation"""
        super().process_keywords()
        if self.print_population and self.use_densities:
            self.keywords.append('engrad')

    def process_input_blocks(self):
        """Implements the input blocks for an HF excited states calculation"""

        super().process_input_blocks()
        if self.hf_type == 'rohf':
            # use rocis block when employing rohf
            self.input_blocks.append("%rocis nroots 3 end")
        else:
            self.input_blocks.append(self.create_excited_states_input_block())
        # Always converge wavefunction
        self.input_blocks.append('%scf convforced true end')

    def create_excited_states_input_block(self):
        """Creates the cis block necessary for an HF excited states calculation"""
        input_block = "%cis"
        input_block += '\nnroots 9'  # nroots always needed for es calculation
        input_block += '\niroot 1' if self.use_nacme else ''
        input_block += ('\nupop true') if self.print_population and not self.use_densities else ''
        input_block += ('\nnacme true\netf true') if self.use_nacme else ''
        input_block += ('\ndosoc true\nscspar 0.333, 1.2, 0.43, 1.24') if self.do_soc else ''
        input_block += ('\nsf true') if self.use_spin_flip else ''
        input_block += '\nend'
        return input_block

    def choose_ri_approximation(self, use_mp2):
        return random.choice(['rijcosx', 'rijonx'])


class DFTExcitedStatesCalculation(DFTCalculation):
    """
    Implements a DFT based excited states calculation.

    Parameters:
        xyz (str): The XYZ coordinates of the molecule.
        molecule_file (str): The file containing molecular information.
        molecule_type (str): The type of molecule (e.g., 'Molecules', 'MoleculesRadical').
        add_solvation (bool): Flag to add solvation effects.
        use_ri_approximation (bool): Flag to use the RI approximation.
        use_dispersion (bool): Flag to include dispersion corrections.
        use_nl (bool): Flag to include nonlocal corrections.
        print_population (bool): Flag to print population analysis.
        use_densities (bool): Flag to use densities in the calculation.
        do_soc (bool): Flag to include spin-orbit coupling effects.
        use_triplets (bool): Flag to include triplet states.
        use_nacme (bool): Flag to calculate nonadiabatic coupling matrix elements.
        use_dcorr (bool): Flag to use double hybrid correlation.
        use_scs (bool): Flag to use spin-component scaling.
        use_tda (bool): Flag to use the Tamm-Dancoff approximation.
        mode (str): Mode of the TDDFT calculation ('stda' or other modes).
        use_spin_flip (bool): Flag to perform spin-flip calculations.
    """

    def __init__(self, xyz, molecule_file, molecule_type, add_solvation=False,
                 use_ri_approximation=True, use_dispersion=False, use_nl=False,
                 print_population=False, use_densities=False, do_soc=False, use_triplets=False, use_nacme=False,
                 use_dcorr=False, use_scs=False, use_tda=False, mode='stda', use_spin_flip=False):

        # DFT options for es
        self.use_dcorr = use_dcorr
        self.use_scs = use_scs if use_dcorr else False  # scs only works when dcorr is on
        self.mode = mode
        self.use_tda = use_tda

        super().__init__(xyz, molecule_file, molecule_type,
                         add_solvation, use_ri_approximation, use_dispersion, use_nl)

        # General es options
        self.print_population = print_population
        self.use_densities = use_densities
        self.use_triplets = use_triplets if self.hf_type == 'rhf' else False
        self.do_soc = do_soc if (self.use_triplets and not use_dcorr and
                                 # SOC does not allow for double hybrids, but dcorr needs this
                                 not self.functional_type == 'double-hybrid' and not print_population) else False
        self.use_spin_flip = use_spin_flip if self.hf_type != 'rhf' and not self.use_dcorr else False

        # triplets has to be turned off for nacme
        self.use_nacme = use_nacme if not use_triplets else False

    def choose_functional(self, functional_type=None, molecule_type=None):
        """Randomly choose a hybrid of double hybrid, except for when double correction is applied."""
        if self.use_dcorr:  # dcorr only works with double hybrid
            return super().choose_functional(functional_type='double-hybrid')
        # Meta-GGA functionals are not yet implemented for CIS and TDDFT gradient
        return super().choose_functional(functional_type=random.choice(['hybrid', 'double-hybrid']))

    def process_keywords(self):
        """Implements the keywords for a DFT based excited states calculation"""
        super().process_keywords()
        if self.print_population and self.use_densities:
            self.keywords.append('engrad')
        if self.mode is not False and self.functional_type == 'hybrid':  # Use numerical gradient for hybrids
            self.keywords.append('numgrad')

    def process_input_blocks(self):
        """Implements the input blocks for a DFT based excited states calculation"""

        super().process_input_blocks()
        if self.hf_type == 'rohf':
            self.input_blocks.append("%rocis nroots 3 end")
        else:
            self.input_blocks.append(self.create_excited_states_input_block())
        self.input_blocks.append('%scf convforced true end')

    def create_excited_states_input_block(self):
        """Creates the tddft block necessary for an HF excited states calculation"""

        input_block = "%tddft"
        input_block += '\nnroots 9'  # nroots always needed for es calculation
        input_block += '\niroot 1' if self.use_nacme else ''
        input_block += ('\nupop true') if self.print_population and not self.use_densities else ''
        input_block += ('\nmode ' +
                        self.mode) if self.mode is not False and self.functional_type == 'hybrid' else ''
        input_block += ('\ndcorr 1') if self.use_dcorr else ''
        input_block += ('\ndoscs true') if self.use_scs else ''
        input_block += ('\ntda true') if self.use_tda else ''
        input_block += ('\nnacme true\netf true') if self.use_nacme else ''
        input_block += ('\ndosoc true\nscspar 0.333, 1.2, 0.43, 1.24') if self.do_soc else ''
        input_block += ('\nsf true') if self.use_spin_flip else ''
        input_block += '\nend'
        return input_block

    def choose_ri_approximation(self):
        return random.choice(['rijcosx', 'rijonx']) if not self.functional_is_range_seperated() else 'rijcosx'

    def add_aux_basis_sets_to_keywords(self):
        """Add necassary auxiliary basis sets, for dft excited states, we need /c for double hybrids."""
        super().add_aux_basis_sets_to_keywords()
        if self.functional_type == 'double-hybrid':
            c_basis_set, is_new_aux = self.basisSetHandler.get_aux_basis_set(
                'c')
            if is_new_aux:
                self.keywords.append(c_basis_set)
