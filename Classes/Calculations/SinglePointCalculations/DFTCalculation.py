from Classes.Calculations.Calculation import Calculation
from Data.ExtractedDocumentation import keywords_density_functionals, keywords_simple_input
from Classes.Helpers.ORCADocumentationHandler import ORCADocumentationHandler
import random

class DFTCalculation(Calculation):
    def __init__(self, xyz, molecule_file, molecule_type, add_solvation=False,
                  use_ri_approximation = True, use_dispersion = False, use_nl = False):     
        self.functional, self.functional_type = self.choose_functional(molecule_type=molecule_type)
        self.functional_description = ORCADocumentationHandler.get_density_functional_documentation()[self.functional]  
        super().__init__(xyz=xyz, molecule_file=molecule_file, molecule_type=molecule_type, add_solvation=add_solvation)
        self.ri_approximation = self.choose_ri_approximation() if use_ri_approximation else None
        self.dispersion_correction = self.choose_dispersion_correction() if use_dispersion and not 'b97m' in self.functional else ""
        self.nl_correction = self.choose_non_local_correction() if use_nl and not 'b97m' in self.functional and (
            not ("d3" in self.functional or "d4" in self.functional) and not ('d3' in self.dispersion_correction 
            or 'd4' in self.dispersion_correction)) else None  # nl does not work with d3 or d4
        self.grid_type = self.choose_grid_type()

    def process_keywords(self):
        self.keywords.extend(['tightscf', 
                              self.basisSetHandler.basis_set, 
                              self.functional, 
                              self.ri_approximation, 
                              self.grid_type, 
                              self.hf_type if self.functional_type != 'non-hybrid' else None,
                              'numgrad' if not self.functional_has_gradient() else None,
                              self.dispersion_correction if self.dispersion_correction != '' else None,
                              self.nl_correction])
        self.keywords = list(filter(lambda x: x is not None, self.keywords)) # Remove all None, these were not defined in this calculation    
        self.add_aux_basis_sets_to_keywords()

    def process_input_blocks(self):
        # Using meta-gg of libxc needs autotrah off, as it already uses dft-nl correction by default
        if 'b97m' in self.functional:
            self.input_blocks.append("%scf AutoTRAH false end")
            
        # Parameterize nl
        if self.nl_correction is not None:
            self.input_blocks.append("%method NLb 5.0 end")
            self.input_blocks.append("%scf AutoTRAH false end")

        # Parameterize dispersion
        if self.dispersion_correction is not None:
            if self.dispersion_correction == 'd3zero':
                self.input_blocks.append("%method\n   D3S6 1.0000\n   D3RS6 1.2170\n   D3S8 0.7220\n   D3ALPHA6 14.0\nend")
            elif 'd3' in self.dispersion_correction:
                self.input_blocks.append("%method\n   D3s6 0.61\n   D3s8 0\n   D3a1 0\n   D3a2 6.2\nend")
            elif 'd4' in self.dispersion_correction:
                self.input_blocks.append("%method\n   D4s6 0.61\n   D4s8 0\n   D4a1 0\n   D4a2 6.2\nend")

        if self.functional_uses_mp2():
            self.input_blocks.append(f"%mp2 Density {random.choice(['unrelaxed', 'relaxed'])} end")
    
    def choose_functional(self, functional_type = None, molecule_type = None):
        functional = None
        if functional_type is None: # If no functional type is defined, we randomly choose one
            functional_type = random.choice(["non-hybrid", "hybrid", "double-hybrid"])
        
        if functional_type == 'non-hybrid':
            functional = self.get_random_non_hybrid_functional()
        elif functional_type == 'hybrid':
            functional = self.get_random_hybrid_functional()
        elif functional_type == 'double-hybrid':
            functional = self.get_random_double_hybrid_functional()
        # Dlpno only implemented for rhf, so keep calling function until we get a non dlpno 
        if self.functional_uses_dlpno(functional=functional) and molecule_type == 'MoleculesRadical':
            functional, functional_type = self.choose_functional(functional_type=functional_type)
        return functional, functional_type
    
    def choose_ri_approximation(self):
        ri_approximation = None
        if self.functional_type == 'non-hybrid':
            ri_approximation = "ri"
        else:
            # Rijk is not implemented for rohf
            ri_approximation = random.choice(["rijk", "rijcosx", 'rijonx']) if self.hf_type != 'rohf' else (
                random.choice(["rijcosx", 'rijonx']) if not self.functional_is_range_seperated() else 'rijcosx')
            
        return ri_approximation
    
    def choose_grid_type(self):
        # Frequency calcs need defgrid3
        grid_type = ORCADocumentationHandler.choose_random_keyword(keywords_simple_input.dft_grid_keywords) if not 'm06' in self.functional else 'defgrid3'
        grid_type = 'defgrid3' if grid_type == 'nocosx' and 'rijcosx' in self.keywords else grid_type
        return grid_type

    def get_random_non_hybrid_functional(self):
        non_hybrids = (list(ORCADocumentationHandler.process_documentation(keywords_density_functionals.dft_meta_gga).keys()))
        return random.choice(non_hybrids)
    
    def get_random_hybrid_functional(self):
        hybrids = list(ORCADocumentationHandler.process_documentation(keywords_density_functionals.dft_local_and_gradient_corrected + "\n"
                                           + keywords_density_functionals.dft_hybrid_functionals + "\n" 
                                           + keywords_density_functionals.dft_meta_gga_hybrid + "\n"
                                           + keywords_density_functionals.dft_range_seperated_hybrid + "\n").keys())
        return random.choice(hybrids)
    
    def get_random_double_hybrid_functional(self):
        return ORCADocumentationHandler.choose_random_keyword(keywords_density_functionals.dft_global_range_separated_double_hybrid_spin_component_spin_opposite_scaling + "\n"
                            + keywords_density_functionals.dft_range_seperated_double_hybrid + "\n"
                            + keywords_density_functionals.dft_range_seperated_double_hybrid_with_dlpno + "\n"
                            + keywords_density_functionals.dft_range_seperated_double_hybrid_with_ri + "\n"
                            + keywords_density_functionals.dft_global_range_separated_double_hybrid_spin_component_spin_opposite_scaling_with_dlpno + "\n" 
                            + keywords_density_functionals.dft_global_range_separated_double_hybrid_spin_component_spin_opposite_scaling_with_ri + "\n"
                            + keywords_density_functionals.dft_perturbatively_corrected_double_hybrid + "\n"
                            + keywords_density_functionals.dft_perturbatively_corrected_double_hybrid_with_ri + "\n"
                            + keywords_density_functionals.dft_perturbatively_corrected_double_hybrid_with_dlpno)
    

    def determine_hf_type(self):
        hf_type = super().determine_hf_type()

        # Gradient not implemented for rohf
        if hf_type == 'rohf' and (self.functional_uses_mp2() or self.functional_uses_ri() or self.functional_is_range_seperated()):
            hf_type = 'uhf'
        return hf_type

    def choose_non_local_correction(self):
        nl_correction = ORCADocumentationHandler.choose_random_keyword(keywords_density_functionals.dft_non_local_correlation)
        return nl_correction

    def choose_dispersion_correction(self):
        dispersion_correction = ORCADocumentationHandler.choose_random_keyword(keywords_density_functionals.dft_dispersion_correction) if 'm06' not in self.functional else 'd3zero'
        return dispersion_correction
  
    def functional_is_range_seperated(self):
        return self.functional in list(ORCADocumentationHandler.process_documentation(keywords_density_functionals.dft_range_seperated_hybrid + 
                                           "\n" + keywords_density_functionals.dft_range_seperated_double_hybrid + 
                                           "\n" + keywords_density_functionals.dft_range_seperated_double_hybrid_with_dlpno
                                           + "\n" + keywords_density_functionals.dft_range_seperated_double_hybrid_with_ri 
                                           + "\n" + keywords_density_functionals.dft_global_range_separated_double_hybrid_spin_component_spin_opposite_scaling
                                           + "\n" + keywords_density_functionals.dft_global_range_separated_double_hybrid_spin_component_spin_opposite_scaling_with_dlpno
                                           + "\n" + keywords_density_functionals.dft_global_range_separated_double_hybrid_spin_component_spin_opposite_scaling_with_ri)
                                           .keys())
    
    def functional_uses_mp2(self):
        return ("dlpno" in self.functional or "mp2" in self.functional or 'lyp' in self.functional or 
                "MP2" in self.functional_description or "DLPNO" in self.functional_description)

    def functional_uses_dlpno(self, functional=None):
        if functional is not None:
           return ("dlpno" in functional or "DLPNO" in ORCADocumentationHandler.get_density_functional_documentation()[functional]) 
        return ("dlpno" in self.functional or "DLPNO" in self.functional_description)
    
    def functional_uses_ri(self):
        return ("ri" in self.functional or "RI" in self.functional_description)
    
    def functional_has_gradient(self):
        return not ('PWPB95' in self.functional or 'PW6B95' in self.functional or 'DSD-PBEB95' in self.functional)
    
    def add_aux_basis_sets_to_keywords(self):
        # If we use RI and a hybrid functional, we need an aux basis set
        if self.ri_approximation is not None and self.functional_type != 'non-hybrid':  
            if self.ri_approximation == 'rijk':
                jk_basis_set, is_new_aux = self.basisSetHandler.get_aux_basis_set("jk")
                if is_new_aux: self.keywords.append(jk_basis_set)
            else: 
                j_basis_set, is_new_aux = self.basisSetHandler.get_aux_basis_set("j")
                if is_new_aux: self.keywords.append(j_basis_set)

        # If we use ri or dlpno, we need a c basis set
        if (self.functional_uses_mp2() or self.functional_uses_ri()):
            c_basis_set, is_new_aux = self.basisSetHandler.get_aux_basis_set("c")
            if is_new_aux: self.keywords.append(c_basis_set)
