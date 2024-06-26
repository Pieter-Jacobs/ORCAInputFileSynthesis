import random
from Classes.Calculations.SinglePointCalculations.DFTCalculation import DFTCalculation
from Classes.Calculations.SinglePointCalculations.HFCalculation import HFCalculation
from Classes.Calculations.SinglePointCalculations.CCCalculation import CCCalculation
from Data.ExtractedDocumentation import keywords_simple_input
from Classes.Helpers.ORCADocumentationHandler import ORCADocumentationHandler

class CCExcitedStatesCalculation(CCCalculation):
    def __init__(self, xyz, molecule_file, molecule_type, add_solvation=False, use_densities=False,
                 use_triplets=False, do_db_filter=False, use_QROs= False):
        super().__init__(xyz, molecule_file, molecule_type, add_solvation, use_densities)
        self.use_triplets = use_triplets if self.hf_type == 'rhf' else False
        self.use_QROs = use_QROs if self.hf_type == 'uhf' else False
        self.do_db_filter = do_db_filter
        self.add_solvation = add_solvation

    def choose_functional(self):
        functional =  ORCADocumentationHandler.choose_random_keyword(keywords_simple_input.mdci_methods_for_excited_states)
        if functional == 'dlpno-steom-ccsd' and self.hf_type == 'uhf':
            functional = 'steom-ccsd'
        return functional
    
    def determine_hf_type(self):
        """Determine the hartree fock type to use for a calculation. This is necassary for all hybrid-DFT calculations as well.
            Return the hartree fock type."""
        if self.molecule_type == 'Molecules':
            return 'rhf'
        return 'uhf'

    def create_mdci_input_block(self):
        input_block = "%mdci"
        input_block += ("\nnroots 9")
        input_block += ("\nDoAlpha true") if self.molecule_type == "MoleculesRadical" and (self.functional == 'ip-eom-ccsd' or self.functional == 'ea-eom-ccsd') else ''
        if self.functional == 'eom-ccsd' or self.functional == 'ip-eom-ccsd' or self.functional == 'ea-eom-ccsd': # Recommended settings for eom-cc calculations (page 918)
            input_block += f"\nDoCOSXEOM true\nDoAOX3e true\nKCOpt {"KC_AOBLAS" if self.molecule_type == "Molecules" else "KC_AOX"}" 
        if 'bt-pno' in self.functional and self.hf_type == 'rhf':
            input_block += ("\nDLPNOLINEAR true\nNEWDOMAINS true")
        if 'steom' in self.functional:
            input_block += ("\nuseQROs true") if self.use_QROs else ""
            input_block += ("\ndoDbFilter true") if self.do_db_filter else ""
            input_block += ("\ndoTriplet true") if self.use_triplets else ""
        input_block += ("\ndorootwise true") if self.functional == 'steom-dlpno-ccsd' else ''
        input_block += ("\nDoSOLV true") if self.add_solvation else ""
        input_block += ("\nlocRandom 0")
        input_block += (f"\ndensity {random.choice(['linearized', 'unrelaxed', 'orbopt'] if not 'ccsd(t)' in self.functional else ['linearalized', 'orbopt'])}") if self.use_densities else ""
        input_block += ("\nUseQROs true") if self.molecule_type == 'MoleculesRadical' else ''
        input_block += "\nend"
        return input_block
    
    
class HFExcitedStatesCalculation(HFCalculation):
    def __init__(self, xyz, molecule_file, molecule_type, add_solvation=False,
                 use_mp2=False, use_ri=False, 
                 print_population=False, use_densities=False, do_soc=False, use_triplets=False, use_nacme=False, use_spin_flip=False):
        super().__init__(xyz, molecule_file, molecule_type, add_solvation, use_mp2, use_ri)
        
        # General es options
        self.print_population = print_population
        self.use_densities=use_densities
        self.use_triplets=use_triplets if self.hf_type == 'rhf' else False
        self.do_soc = do_soc if self.use_triplets and not print_population else False # SOC does not allow for double hybrids, but dcorr needs this
        self.use_nacme = use_nacme if not use_triplets else False # triplets has to be turned off for nacme
        self.use_spin_flip = use_spin_flip if self.hf_type != 'rhf' else False

    def process_keywords(self):
        super().process_keywords()
        if self.print_population and self.use_densities:
            self.keywords.append('engrad')

    def process_input_blocks(self):
        super().process_input_blocks()
        if self.hf_type == 'rohf':
            self.input_blocks.append("%rocis nroots 3 end")
        else:
            self.input_blocks.append(self.create_excited_states_input_block())
        self.input_blocks.append('%scf convforced true end')
    
    def create_excited_states_input_block(self):
        input_block = "%cis"
        input_block += '\nnroots 9' # nroots always needed for es calculation
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
    def __init__(self, xyz, molecule_file, molecule_type, add_solvation=False, 
                 use_ri_approximation=True, use_dispersion=False, use_nl=False,
                 print_population=False, use_densities=False, do_soc=False, use_triplets=False, use_nacme=False, 
                 use_dcorr=False, use_scs=False, use_tda=False, mode='stda', use_spin_flip=False):
        
        # DFT options for es
        self.use_dcorr = use_dcorr 
        self.use_scs = use_scs if use_dcorr else False # scs only works when dcorr is on
        self.mode = mode
        self.use_tda = use_tda

        super().__init__(xyz, molecule_file, molecule_type, add_solvation, use_ri_approximation, use_dispersion, use_nl)
        
        # General es options
        self.print_population = print_population
        self.use_densities=use_densities
        self.use_triplets=use_triplets if self.hf_type == 'rhf' else False
        self.do_soc = do_soc if (self.use_triplets and not use_dcorr and 
                                 not self.functional_type == 'double-hybrid' and not print_population) else False # SOC does not allow for double hybrids, but dcorr needs this
        self.use_spin_flip = use_spin_flip if self.hf_type != 'rhf' and not self.use_dcorr else False

        self.use_nacme = use_nacme if not use_triplets else False # triplets has to be turned off for nacme

    def choose_functional(self, functional_type=None, molecule_type=None):
        if self.use_dcorr: # dcorr only works with double hybrid
            return super().choose_functional(functional_type='double-hybrid')
        # Meta-GGA functionals are not yet implemented for CIS and TDDFT gradient
        return super().choose_functional(functional_type=random.choice(['hybrid', 'double-hybrid']))
    
    def process_keywords(self):
        super().process_keywords()
        if self.print_population and self.use_densities:
            self.keywords.append('engrad')
        if self.mode is not False and self.functional_type == 'hybrid':
            self.keywords.append('numgrad')
    
    def process_input_blocks(self):
        super().process_input_blocks()
        if self.hf_type == 'rohf':
            self.input_blocks.append("%rocis nroots 3 end")
        else:
            self.input_blocks.append(self.create_excited_states_input_block())
        self.input_blocks.append('%scf convforced true end')
    
    def create_excited_states_input_block(self):
        input_block = "%tddft"
        input_block += '\nnroots 9' # nroots always needed for es calculation
        input_block += '\niroot 1' if self.use_nacme else ''
        input_block += ('\nupop true') if self.print_population and not self.use_densities else ''
        input_block += ('\nmode ' + self.mode) if self.mode is not False and self.functional_type == 'hybrid' else ''
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
        super().add_aux_basis_sets_to_keywords()
        if self.functional_type == 'double-hybrid':
            c_basis_set, is_new_aux = self.basisSetHandler.get_aux_basis_set('c')
            if is_new_aux: self.keywords.append(c_basis_set)
