from Data.periodic_table import periodic_table
from Classes.Helpers.ORCADocumentationHandler import ORCADocumentationHandler
import re
import basis_set_exchange as bse
import random
from Data.ExtractedDocumentation import basis_sets
from Classes.Helpers.ORCAInputFileManipulator import ORCAInputFileManipulator

class BasisSetHandler():
    
    def __init__(self, xyz):
        self.elements = ORCAInputFileManipulator.extract_elements(xyz)
        self.possible_basis_sets = self.get_possible_basis_sets([name.lower() for name in bse.get_all_basis_names() if name.lower()
                                                                 in list(ORCADocumentationHandler.get_basis_set_documentation().keys())])
        self.basis_set = self.sort_basis_sets_by_size(self.possible_basis_sets)[0]
        self.added_bs_roles = set() # keep account of roles, so they dont get added twice

    def sort_basis_sets_by_size(self, basis_sets):
        def count_basis_functions(basis_set_name):
            basis_set_info = bse.get_basis(basis_set_name, elements=self.elements)
            num_basis_functions = 0
            for element in list(basis_set_info['elements'].keys()):
                for shell in basis_set_info['elements'][element]['electron_shells']:
                    num_basis_functions += len(shell['coefficients'])
            return num_basis_functions
        return sorted(basis_sets, key=count_basis_functions)

    def get_possible_basis_sets(self, basis_set_names):
        if all(isinstance(item, str) for item in self.elements):
            self.elements = [periodic_table[element] for element in self.elements]

        possible_basis_sets = []
        for name in basis_set_names:
            try:
                basis_set_info = bse.get_basis(name, elements=self.elements)
                possible_basis_sets.extend(basis_set_info["names"])
            except Exception as e: 
                pass
        return list(set(possible_basis_sets))

    def get_smallest_possible_basis_set(self):
        def count_basis_functions(basis_set_info):
            num_basis_functions = 0
            for element in list(basis_set_info['elements'].keys()):
                for shell in basis_set_info['elements'][element]['electron_shells']:
                    num_basis_functions += len(shell['coefficients'])
            return num_basis_functions
        
        least_basis_functions = float('inf')
        smallest_possible_basis_set = None
        for name in self.possible_basis_sets:
            try:
                basis_set_info = bse.get_basis(name, elements=self.elements)
                basis_functions = count_basis_functions(basis_set_info)
                if basis_functions < least_basis_functions: 
                    least_basis_functions = basis_functions
                    smallest_possible_basis_set = basis_set_info['names']
            except Exception as e: 
                pass
        return smallest_possible_basis_set[0]

    def get_aux_basis_set(self, role):
        orca_basis_sets = list(ORCADocumentationHandler.get_basis_set_documentation().keys())

        fitted_basis_set = ""
        if role == "j":
            if "def2" in self.basis_set: 
                fitted_basis_set = f"def2/j"
            elif "sarc" in self.basis_set:
                fitted_basis_set = f"sarc/j"
            elif "x2c" in self.basis_set:  
                fitted_basis_set = f"x2c/j"

        elif role == "jk":
            if "def2" in self.basis_set: 
                fitted_basis_set = f"def2/jk"
            elif re.search(r"aug-cc-pV[T|Q|5]Z", self.basis_set):
                fitted_basis_set = f"{re.search(r"aug-cc-pV[T|Q|5]Z", self.basis_set).group(0)}/jk"
            elif re.search(r"cc-pV[T|Q|5]Z", self.basis_set):
                fitted_basis_set = f"{re.search(r"cc-pV[T|Q|5]Z", self.basis_set).group(0)}/jk"

        elif role == "c":
            fitted_basis_set = self.basis_set + "/c"
        
        if fitted_basis_set not in orca_basis_sets:
            fitted_basis_set = "autoaux"
        
        is_new_aux = not (role in self.added_bs_roles)
        self.added_bs_roles.add(role)

        return fitted_basis_set, is_new_aux


    def get_f12_basis_set(self):
        f12_documentation = ORCADocumentationHandler.process_documentation(basis_sets.basis_set_auxilary_cabs)
        f12_basis_sets = self.get_possible_basis_sets(list(f12_documentation.keys()))
        if len(f12_basis_sets) > 0: 
            f12_basis_set = random.choice(f12_basis_sets)
        else:
            f12_basis_set = ORCADocumentationHandler.choose_random_keyword(f12_documentation)
        is_new_aux = not ('f12' in self.added_bs_roles)
        self.added_bs_roles.add('f12')
        return f12_basis_set.lower(), is_new_aux