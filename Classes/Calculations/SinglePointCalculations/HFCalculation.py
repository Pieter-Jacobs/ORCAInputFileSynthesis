from Classes.Calculations.Calculation import Calculation
from Classes.Helpers.ORCADocumentationHandler import ORCADocumentationHandler
from Data.ExtractedDocumentation import keywords_simple_input
import random

class HFCalculation(Calculation):
    def __init__(self, xyz, molecule_file, molecule_type, add_solvation=False,
                 use_mp2=False, use_ri=False):
        self.mp2_ri_method = self.choose_mp2_ri_method() if use_mp2 and use_ri else None
        self.mp2_method = self.choose_mp2_method() if use_mp2 and not use_ri else None
        super().__init__(xyz=xyz, 
                         molecule_file=molecule_file, 
                         molecule_type=molecule_type,
                         add_solvation=add_solvation)
        self.ri_approximation = self.choose_ri_approximation(use_mp2=use_mp2) if use_ri else None
        if use_mp2 is None and use_ri is None:
            self.keywords.append('nori')

    def process_keywords(self):
        mp2_method = self.mp2_method if self.mp2_method is not None else self.mp2_ri_method 
        self.keywords.extend([self.basisSetHandler.basis_set,
                              self.hf_type,
                              self.mp2_method,
                              self.ri_approximation,
                              self.choose_scf_convergence() if mp2_method is not None else None,
                              self.choose_accuracy_control() if mp2_method is not None and 'dlpno' in mp2_method else None
                              ])
        self.keywords = list(filter(lambda x: x is not None, self.keywords)) # Remove all None, these were not defined in this calculation    
        self.add_aux_basis_sets_to_keywords()
        
    def process_input_blocks(self):
        mp2_method = self.mp2_method if self.mp2_method is not None else self.mp2_ri_method
        if self.hf_type == 'rohf' and self.ri_approximation is not None:
            self.input_blocks.append('%scf MaxIter 500 end')
        if mp2_method is not None: # We are using mp2
            self.input_blocks.append("%scf ConvForced true end")
            if self.hf_type == 'rhf' and not 'f12' in mp2_method:
                    self.input_blocks.append(f"%mp2 Density {random.choice(['unrelaxed', 'relaxed'])} end")
            # We need Augmented Forter boys for ccsd dlpno calculations
            if 'ccsd' in mp2_method and 'dlpno' in mp2_method:
                self.input_blocks.append("%mdci LocRandom 0 end")

    def choose_mp2_ri_method(self):
        mp2_methods = list(ORCADocumentationHandler.process_documentation(keywords_simple_input.basic_mp2_methods + "\n" + keywords_simple_input.local_correlation_mp2_methods).keys())
        mp2_ri_method = random.choice([method for method in mp2_methods if 'ri' in method])
        return mp2_ri_method

    def choose_mp2_method(self):
        mp2_methods = list(ORCADocumentationHandler.process_documentation(keywords_simple_input.basic_mp2_methods + "\n" + keywords_simple_input.local_correlation_mp2_methods).keys())
        mp2_method = random.choice([method for method in mp2_methods if not 'ri' in method])
        return mp2_method

    def choose_ri_approximation(self, use_mp2):
        ri_approximation = None
        if self.hf_type == 'rohf':
            ri_approximation = 'rijonx'
        else:
            if use_mp2: # If we are using both ri and mp2
                if 'oo-' in self.mp2_ri_method:
                    return 'rijcosx'
                else: 
                    return random.choice(['rijcosx', 'rijonx'])
            else: 
                ri_approximation = ORCADocumentationHandler.choose_random_keyword(keywords_simple_input.ri_computation_for_hf_and_dft)
        return ri_approximation
    
    def choose_scf_convergence(self):
        return ORCADocumentationHandler.choose_random_keyword(keywords_simple_input.scf_convergence_thesholds)

    def choose_accuracy_control(self):
        return ORCADocumentationHandler.choose_random_keyword(keywords_simple_input.accuracy_control)

    def add_aux_basis_sets_to_keywords(self):
        if self.ri_approximation is not None:
            c_basis_set, is_new_aux = self.basisSetHandler.get_aux_basis_set("c") # Ri always needs a c basis set
            if is_new_aux: self.keywords.append(c_basis_set)
            if "jk" in self.ri_approximation:
                jk_basis_set, is_new_aux = self.basisSetHandler.get_aux_basis_set("jk")
                if is_new_aux: self.keywords.append(jk_basis_set)
            if self.mp2_ri_method is not None and 'f12' in self.mp2_ri_method: # if using mp2 and f12 in the method
                f12_basis_set, is_new_aux = self.basisSetHandler.get_f12_basis_set()
                if is_new_aux: self.keywords.append(f12_basis_set)
        elif self.mp2_method is not None:
            if 'dlpno' in self.mp2_method: # dlpno in a non-ri also requires AuxC
                c_basis_set, is_new_aux = self.basisSetHandler.get_aux_basis_set("c")
                if is_new_aux: self.keywords.append(c_basis_set)
            if 'f12' in self.mp2_method: # if using mp2 and f12 in the method
                f12_basis_set, is_new_aux = self.basisSetHandler.get_f12_basis_set()
                if is_new_aux: self.keywords.append(f12_basis_set)

    def determine_hf_type(self):
        hf_type = super().determine_hf_type()
        if hf_type == 'rohf' and (self.mp2_method is not None or self.mp2_ri_method is not None): # MP2 gradient not implemented for rohf
            hf_type = 'uhf'
        return hf_type