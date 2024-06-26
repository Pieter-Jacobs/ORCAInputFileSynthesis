from Classes.Calculations.SpecializedCalculations.GeometryOptimization import DFTGeometryOptimization
from Classes.Calculations.SpecializedCalculations.GeometryOptimization import HFGeometryOptimization
from Classes.Calculations.SpecializedCalculations.GeometryOptimization import CCGeometryOptimization
from Classes.Calculations.SinglePointCalculations.CCCalculation import CCCalculation
from Classes.Calculations.SinglePointCalculations.DFTCalculation import DFTCalculation
from Classes.Calculations.SinglePointCalculations.HFCalculation import HFCalculation
import random


class CCFrequencyCalculation:
    """Initializes a Coupled Cluster Frequency calculation.

    Parameters:
    - xyz: coordinate-block of the used molecule.
    - molecule_file: file containing molecule data.
    - molecule_type: Molecule or MoleculeRadical, used to determine what type of molecule is used
    - use_geom: boolean indicating whether to include a geometry optimization
    - add_solvation: boolean indicating whether to add a random solvation model.
    - use_densities: boolean indicating whether to randomly alter the normally used densities.
    - do_relaxed_scan: boolean indicating whether to perform a relaxed scan in the possible geometry optimization
    - calculate_hessian: boolean indicating whether to recalculate the Hessian.
    - use_constraints: boolean indicating whether to constrain the possible geometry optimization.
    - use_cd: boolean indicating whether to use Central Differences in gradient calculation

    """

    def __init__(self, xyz, molecule_file, molecule_type, use_geom, add_solvation=False, use_densities=False, do_relaxed_scan=False, calculate_hessian=False, use_constraints=False,
                 use_cd=False):
        if use_geom:
            self.base_class = CCGeometryOptimization(xyz, molecule_file, molecule_type, add_solvation,
                                                     use_densities, do_relaxed_scan, calculate_hessian, use_constraints)
            self.base_class.geom.geom_convergence = 'tightopt'
        else:
            self.base_class = CCCalculation(xyz=xyz, molecule_file=molecule_file,
                                            molecule_type=molecule_type, add_solvation=add_solvation, use_densities=use_densities)
        self.freq_gradient = self.get_frequency_gradient()
        self.use_cd = use_cd

    def get_frequency_gradient(self):
        """Determines what type of gradient to use"""
        if (self.base_class.hf_type == 'rohf'):
            return 'numfreq'
        return 'anfreq'

    def process_keywords(self):
        """Implements all necessary keywords for a CC frequency calculation"""

        self.base_class.process_keywords()
        if self.freq_gradient == 'numfreq':
            self.base_class.keywords.append("engrad")
        self.base_class.keywords.append(self.freq_gradient)
        self.base_class.keywords.append('defgrid3')

        j_basis_set, is_new_aux = self.base_class.basisSetHandler.get_aux_basis_set(
            'j')
        if is_new_aux:
            self.base_class.keywords.append(j_basis_set)

    def process_input_blocks(self):
        """Implements all necessary input blocks for a CC frequency calculation"""

        self.base_class.process_input_blocks()
        self.base_class.input_blocks.append(self.create_freq_input_block())

    def generate_input_file(self):
        """Wrapper used to be able to call the geometry optimization calculation"""
        return self.base_class.generate_input_file()

    def create_freq_input_block(self):
        """Creates a frequency input block for CC"""
        input_block = "%freq"
        input_block += ('\nHess2ElFlags 1,2,2,1')
        input_block += '\nCentralDiff false' if not self.use_cd and self.freq_gradient == 'numfreq' else ''
        input_block += "\nend"
        return input_block


class HFFrequencyCalculation:
    """Initializes a Hartree Fock frequency calculation.

    Parameters:
    - xyz: coordinate-block of the used molecule.
    - molecule_file: file containing molecule data.
    - molecule_type: Molecule or MoleculeRadical, used to determine what type of molecule is used
    - use_geom: boolean indicating whether to include a geometry optimization
    - add_solvation: boolean indicating whether to add a random solvation model.
    - use_ri: boolean indicating whether to add a random RI approximation.
    - use_mp2: boolean indicating whether to add MP2 theory.
    - do_relaxed_scan: boolean indicating whether to perform a relaxed scan in the possible geometry optimization
    - calculate_hessian: boolean indicating whether to recalculate the Hessian.
    - use_constraints: boolean indicating whether to constrain the possible geometry optimization.
    - use_cd: boolean indicating whether to use Central Differences in gradient calculation

    """

    def __init__(self, xyz, molecule_file, molecule_type, use_geom, add_solvation=False,
                 use_mp2=False, use_ri=False,
                 do_relaxed_scan=False, calculate_hessian=False, use_constraints=False,
                 use_cd=False):
        if use_geom:
            self.base_class = HFGeometryOptimization(xyz=xyz, molecule_file=molecule_file, molecule_type=molecule_type,
                                                     add_solvation=add_solvation, use_mp2=use_mp2, use_ri=use_ri,
                                                     do_relaxed_scan=do_relaxed_scan, calculate_hessian=calculate_hessian,
                                                     use_constraints=use_constraints)
            self.base_class.geom.geom_convergence = 'tightopt'
        else:
            self.base_class = HFCalculation(xyz=xyz, molecule_file=molecule_file, molecule_type=molecule_type,
                                            add_solvation=add_solvation, use_mp2=use_mp2, use_ri=use_ri)

        self.freq_gradient = self.get_frequency_gradient()
        self.use_cd = use_cd

    def process_keywords(self):
        """Implements all necessary keywords for an HF frequency calculation"""

        self.base_class.process_keywords()
        self.base_class.keywords.append(self.freq_gradient)
        self.base_class.keywords.append('defgrid3')
        if self.freq_gradient == 'numfreq':
            self.base_class.keywords.append("engrad")
        j_basis_set, is_new_aux = self.base_class.basisSetHandler.get_aux_basis_set(
            'j')
        if is_new_aux:
            self.base_class.keywords.append(j_basis_set)

    def process_input_blocks(self):
        """Implements all necessary input blocks for an HF frequency calculation"""

        self.base_class.process_input_blocks()
        self.base_class.input_blocks.append(self.create_freq_input_block())

    def get_frequency_gradient(self):
        """Determines whether to use a numerical or analytical gradient"""

        if (self.base_class.hf_type == 'rohf' or
            self.base_class.ri_approximation == 'ri-jk'
            or self.base_class.ri_approximation == 'rijk'
                or self.base_class.mp2_method is not None or self.base_class.mp2_ri_method is not None):
            return 'numfreq'
        return 'anfreq'

    def create_freq_input_block(self):
        """Creates a frequency input block for HF"""

        input_block = "%freq"
        input_block += ('\nHess2ElFlags 1,2,2,1' if self.base_class.ri_approximation ==
                        'rijcosx' else '\nHess2ElFlags 1,1,1,1') if self.freq_gradient == 'anfreq' else ''
        input_block += '\nCentralDiff false' if not self.use_cd and self.freq_gradient == 'numfreq' else ''
        input_block += "\nend"
        return input_block if len(input_block.splitlines()) > 2 else ""

    def generate_input_file(self):
        """Wrapper used to be able to call the geometry optimization calculation"""
        return self.base_class.generate_input_file()


class DFTFrequencyCalculation:
    """Initializes a Density Functional Theory based Frequency calculation.

    Parameters:
    - xyz: coordinate-block of the used molecule.
    - molecule_file: file containing molecule data.
    - molecule_type: Molecule or MoleculeRadical, used to determine what type of molecule is used
    - use_geom: boolean indicating whether to include a geometry optimization
    - add_solvation: boolean indicating whether to add a random solvation model.
    - use_ri_approximation: boolean indicating whether to add a random RI approximation.
    - use_dispersion: boolean indicating whether to add a random dispersion method.
    - use_nl: boolean indicating whether to add non-local correction
    - do_relaxed_scan: boolean indicating whether to perform a relaxed scan in the possible geometry optimization
    - calculate_hessian: boolean indicating whether to recalculate the Hessian.
    - use_constraints: boolean indicating whether to constrain the possible geometry optimization.
    - use_cd: boolean indicating whether to use Central Differences in gradient calculation

    """

    def __init__(self, xyz, molecule_file, molecule_type, use_geom, add_solvation=False,
                 use_ri_approximation=True, use_dispersion=False, use_nl=False,
                 do_relaxed_scan=False, calculate_hessian=False, use_constraints=False,
                 use_cd=False):
        if use_geom:
            self.base_class = DFTGeometryOptimization(xyz=xyz, molecule_file=molecule_file, molecule_type=molecule_type,
                                                      add_solvation=add_solvation, use_ri_approximation=use_ri_approximation,
                                                      use_dispersion=use_dispersion, use_nl=use_nl, do_relaxed_scan=do_relaxed_scan,
                                                      calculate_hessian=calculate_hessian, use_constraints=use_constraints)
            self.base_class.geom.geom_convergence = 'tightopt'
        else:
            self.base_class = DFTCalculation(xyz=xyz, molecule_file=molecule_file, molecule_type=molecule_type, add_solvation=add_solvation,
                                             use_ri_approximation=use_ri_approximation, use_dispersion=use_dispersion, use_nl=use_nl)

        self.freq_gradient = self.get_frequency_gradient()
        self.use_cd = use_cd
        self.base_class.grid_type = 'defgrid3'
        self.base_class.ri_approximation = self.choose_ri_approximation(
        ) if use_ri_approximation else None

    def process_keywords(self):
        """Implements all necessary keywords for a DFT frequency calculation"""

        self.base_class.process_keywords()
        self.base_class.keywords.append(self.freq_gradient)
        if self.freq_gradient == 'numfreq':
            self.base_class.keywords.append("engrad")
        j_basis_set, is_new_aux = self.base_class.basisSetHandler.get_aux_basis_set(
            'j')
        if is_new_aux:
            self.base_class.keywords.append(j_basis_set)

    def process_input_blocks(self):
        """Implements all necessary input blocks for a DFT frequency calculation"""

        self.base_class.process_input_blocks()
        self.base_class.input_blocks.append(self.create_freq_input_block())

    def get_frequency_gradient(self):
        """Determines whether to use a numerical or analytical gradient"""
        if (self.base_class.hf_type == 'rohf' or
            self.base_class.ri_approximation == 'ri-jk'
            or self.base_class.ri_approximation == 'rijk'
            or self.base_class.functional_uses_mp2()
                or self.base_class.nl_correction is not None):
            return 'numfreq'
        return 'anfreq'

    def choose_ri_approximation(self):
        """Chooses an RI approximation"""
        ri_approximation = None
        if self.base_class.functional_type == 'non-hybrid':
            ri_approximation = "ri"
        elif self.base_class.functional_is_range_seperated():  # geom needs rijcosx for range seperated functionals
            ri_approximation = 'rijcosx'
        else:
            # Rijk is not implemented for rohf
            ri_approximation = random.choice(["rijcosx", 'rijonx'])
        return ri_approximation

    def create_freq_input_block(self):
        """Creates a frequency input block for DFT"""
        input_block = "%freq"
        input_block += ('\nHess2ElFlags 1,2,2,1' if self.base_class.ri_approximation ==
                        'rijcosx' else '\nHess2ElFlags 1,1,1,1') if self.freq_gradient == 'anfreq' else ''
        input_block += '\nCentralDiff false' if not self.use_cd and self.freq_gradient == 'numfreq' else ''
        input_block += "\nend"
        return input_block if len(input_block.splitlines()) > 2 else ""

    def generate_input_file(self):
        """Wrapper used to be able to call the geometry optimization calculation"""
        return self.base_class.generate_input_file()
