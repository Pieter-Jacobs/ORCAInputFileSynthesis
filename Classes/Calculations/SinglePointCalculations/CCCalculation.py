from Classes.Calculations.Calculation import Calculation
from Data.Manual.ExtractedDocumentation import keywords_simple_input
from Classes.Helpers.OrcaDocumentationHandler import OrcaDocumentationHandler
import random

class CCCalculation(Calculation):
    def __init__(self, xyz, molecule_file, molecule_type, add_solvation=False,
                 use_densities=False):
        super().__init__(xyz, molecule_file, molecule_type, add_solvation)
        self.functional = self.choose_functional()
        self.use_densities = use_densities

    def choose_functional(self):
        functional = OrcaDocumentationHandler.choose_random_keyword(keywords_simple_input.ci_type + "\n" 
                                          + keywords_simple_input.local_correlation_mcdi_methods 
                                          + keywords_simple_input.autoci_methods) if self.hf_type != 'rohf' else random.choice(['dlpno-ccsd', 'dlpno-ccsd(t)', 'dlpno-ccsd(t1)'])
        return functional
    
    def process_keywords(self):
        self.keywords.extend(['tightscf',
            self.basisSetHandler.basis_set,
                              self.functional,
                              self.hf_type,
                              "uno" if self.molecule_type == 'MoleculesRadical' else None,
                              self.choose_accuracy_control() if 'pno' in self.functional else None,
                              ])
        self.keywords = list(filter(lambda x: x is not None, self.keywords)) # Remove all None, these were not defined in this calculation    
        self.add_aux_basis_sets_to_keywords()

    def process_input_blocks(self):
        self.input_blocks.append("%scf ConvForced true end") # Coupled cluster is post hf method so need converged wavefunction
        self.input_blocks.append(self.create_mdci_input_block())
        

    def choose_accuracy_control(self):
        #  OrcaDocumentationHandler.choose_random_keyword(keywords_simple_input.accuracy_control)
        return 'tightpno'
    
    def add_aux_basis_sets_to_keywords(self):
        # cc always needs auxC
        c_basis_set, is_new_aux = self.basisSetHandler.get_aux_basis_set("c")
        if is_new_aux: self.keywords.append(c_basis_set)
        if 'f12' in self.functional:  
            f12_basis_set, is_new_aux = self.basisSetHandler.get_f12_basis_set()
            if is_new_aux: self.keywords.append(f12_basis_set)

    def create_mdci_input_block(self):
        input_block = "%mdci"
        input_block += ("\nlocRandom 0")
        input_block += (f"\ndensity {random.choice(['linearized', 'unrelaxed', 'orbopt'] if not 'ccsd(t)' in self.functional else ['linearalized', 'orbopt'])}") if self.use_densities else ""
        input_block += ("\nUseQROs true") if self.molecule_type == 'MoleculesRadical' else ''
        input_block += "\nend"
        return input_block