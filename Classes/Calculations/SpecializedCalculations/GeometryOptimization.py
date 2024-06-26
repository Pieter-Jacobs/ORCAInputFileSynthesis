from Classes.Calculations.SinglePointCalculations.DFTCalculation import DFTCalculation
from Classes.Calculations.SinglePointCalculations.HFCalculation import HFCalculation
from Classes.Calculations.SinglePointCalculations.CCCalculation import CCCalculation
from Classes.Helpers.ORCADocumentationHandler import ORCADocumentationHandler
from Classes.Helpers.ORCAInputFileManipulator import ORCAInputFileManipulator
from Data.ExtractedDocumentation import keywords_simple_input
from molmod import bond_length, Molecule, bend_angle, dihed_angle
import random


class CCGeometryOptimization(CCCalculation):
    """Initializes a Coupled Cluster Geometry Optimization.

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
    """

    def __init__(self, xyz, molecule_file, molecule_type, add_solvation=False, use_densities=False,
                 do_relaxed_scan=False, calculate_hessian=False, use_constraints=False):
        super().__init__(xyz, molecule_file, molecule_type, add_solvation, use_densities)
        self.geom = GeometryOptimization(xyz=xyz,
                                         do_relaxed_scan=do_relaxed_scan,
                                         calculate_hessian=calculate_hessian,
                                         use_constraints=use_constraints,
                                         basisSetHandler=self.basisSetHandler)

    def process_keywords(self):
        """Implements all necessary keywords for a CC Geometry Optimization"""
        super().process_keywords()
        self.keywords.extend([self.geom.optimization_type,
                              self.geom.geom_convergence,
                              'noautostart',
                              'numgrad'])  # angrad is not supported for mdci

        # Relaxed scan has a specific keyword for combining with optts
        if self.geom.geom_convergence == 'optts' and self.geom.do_relaxed_scan:
            self.keywords.append("scants")
            self.keywords.remove('optts')

    def process_input_blocks(self):
        """Implements all necessary input blocks for a CC Geometry Optimization"""

        super().process_input_blocks()
        self.input_blocks.append(self.create_geom_input_block())

    def create_geom_input_block(self):
        """Creates the input block that tunes the settings for a geometry optimization"""
        input_block = "%geom"
        input_block += '\n' + \
            self.geom.get_relaxed_scan_settings() if self.geom.do_relaxed_scan else ''
        input_block += '\n' + self.geom.get_hessian_calculation_settings() + \
            '\nNumHess true' if self.geom.calculate_hessian else ''
        input_block += '\n' + \
            self.geom.get_constraint_settings() if self.geom.use_constraints else ''
        input_block += '\nend'
        return input_block if len(input_block.splitlines()) > 2 else ""


class HFGeometryOptimization(HFCalculation):
    """Initializes a Hartree Fock Geometry Optimization.

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
    """

    def __init__(self, xyz, molecule_file, molecule_type, add_solvation=False,
                 use_mp2=False, use_ri=False,
                 do_relaxed_scan=False, calculate_hessian=False, use_constraints=False):
        super().__init__(xyz, molecule_file, molecule_type, add_solvation, use_mp2, use_ri)
        self.geom = GeometryOptimization(xyz=xyz,
                                         do_relaxed_scan=do_relaxed_scan,
                                         calculate_hessian=calculate_hessian,
                                         use_constraints=use_constraints,
                                         basisSetHandler=self.basisSetHandler)

    def process_keywords(self):
        """Implements all necessary keywords for an HF Geometry Optimization"""

        super().process_keywords()
        self.keywords.extend([self.geom.optimization_type,
                              self.geom.geom_convergence,
                              'noautostart'])

        # Relaxed scan has a specific keyword for combining with optts
        if self.geom.geom_convergence == 'optts' and self.geom.do_relaxed_scan:
            self.keywords.append("scants")
            self.keywords.remove('optts')

    def process_input_blocks(self):
        """Implements all necessary input blocks for an HF Geometry Optimization"""

        super().process_input_blocks()
        self.input_blocks.append(self.create_geom_input_block())

    def create_geom_input_block(self):
        """Creates the input block that tunes the settings for a geometry optimization"""

        input_block = "%geom"
        input_block += '\n' + \
            self.geom.get_relaxed_scan_settings() if self.geom.do_relaxed_scan else ''
        input_block += '\n' + self.geom.get_hessian_calculation_settings() if self.geom.calculate_hessian and (
            self.mp2_method is not None or self.mp2_ri_method is not None) else ''
        input_block += '\n' + \
            self.geom.get_constraint_settings() if self.geom.use_constraints else ''
        input_block += '\nend'
        return input_block if len(input_block.splitlines()) > 2 else ""


class DFTGeometryOptimization(DFTCalculation):
    """Initializes a Density Functional Theory based Geometry Optimization.

    Parameters:
    - xyz: coordinate-block of the used molecule.
    - molecule_file: file containing molecule data.
    - molecule_type: Molecule or MoleculeRadical, used to determine what type of molecule is used
    - use_geom: boolean indicating whether to include a geometry optimization
    - add_solvation: boolean indicating whether to add a random solvation model.
    - use_ri_approximation: boolean indicating whether to add a random RI approximation.
    - use_dispersion: boolean indicating whether to add a random dispersion method.
    - use_nl: boolean indicating whether to add non-local correction
    - do_relaxed_scan: boolean indicating whether to perform a relaxed scan in the geometry optimization
    - calculate_hessian: boolean indicating whether to recalculate the Hessian.
    - use_constraints: boolean indicating whether to constrain the geometry optimization.
    """

    def __init__(self, xyz, molecule_file, molecule_type, add_solvation=False,
                 use_ri_approximation=True, use_dispersion=False, use_nl=False,
                 do_relaxed_scan=False, calculate_hessian=False, use_constraints=False):
        super().__init__(xyz, molecule_file, molecule_type,
                         add_solvation, use_ri_approximation, use_dispersion, use_nl)
        self.geom = GeometryOptimization(xyz=xyz,
                                         do_relaxed_scan=do_relaxed_scan,
                                         calculate_hessian=calculate_hessian,
                                         use_constraints=use_constraints,
                                         basisSetHandler=self.basisSetHandler)

    def process_keywords(self):
        """Implements all necessary keywords for a DFT Geometry Optimization"""

        super().process_keywords()
        self.keywords.extend([self.geom.optimization_type,
                              self.geom.geom_convergence,
                              'noautostart'])
        # Relaxed scan has a specific keyword for combining it with optts
        if self.geom.geom_convergence == 'optts' and self.geom.do_relaxed_scan:
            self.keywords.append("scants")
            self.keywords.remove('optts')

    def process_input_blocks(self):
        """Implements all necessary input blocks for a DFT Geometry Optimization"""

        super().process_input_blocks()
        self.input_blocks.append(self.create_geom_input_block())

    def choose_ri_approximation(self):
        """Chooses an RI approximation based on the functional and the hf type"""
        ri_approximation = None
        if self.functional_type == 'non-hybrid':
            ri_approximation = "ri"
        elif self.functional_is_range_seperated():  # geom needs rijcosx for range seperated
            ri_approximation = 'rijcosx'
        else:
            # Rijk is not implemented for rohf
            ri_approximation = random.choice(
                ["rijk", "rijcosx", 'rijonx']) if self.hf_type != 'rohf' else random.choice(["rijcosx", 'rijonx'])
        return ri_approximation

    def create_geom_input_block(self):
        """Creates the input block that tunes the settings for a geometry optimization"""

        input_block = "%geom"
        input_block += '\n' + \
            self.geom.get_relaxed_scan_settings() if self.geom.do_relaxed_scan else ''
        input_block += '\n' + self.geom.get_hessian_calculation_settings(
        ) if self.geom.calculate_hessian and self.functional_uses_mp2() else ''
        input_block += '\n' + \
            self.geom.get_constraint_settings() if self.geom.use_constraints else ''
        input_block += '\nend'
        return input_block if len(input_block.splitlines()) > 2 else ""


class GeometryOptimization:
    """Base class used to build upon for specific single point calculations. As the geometry optimization is similar for all of them, 
    we used this extra class for the shared functionality."""

    def __init__(self, xyz, do_relaxed_scan, calculate_hessian, use_constraints, basisSetHandler):
        self.do_relaxed_scan = do_relaxed_scan
        self.calculate_hessian = calculate_hessian
        self.use_constraints = use_constraints
        self.basisSetHandler = basisSetHandler
        self.optimization_type = self.choose_optimization_type()
        self.geom_convergence = self.choose_geometry_convergence()
        self.molecule = ORCAInputFileManipulator.extract_molecule(xyz=xyz,
                                                                  n_atoms=len(self.basisSetHandler.elements))

    def choose_optimization_type(self):
        """Randomly chooses an optimization type."""
        optimization_types = ['opt', 'gdiis-opt', 'copt', 'gdiis-copt']
        # Cartesian optimization not possible with a relaxed scan:
        if self.do_relaxed_scan or self.use_constraints or self.calculate_hessian:
            optimization_types = ['opt', 'gdiis-opt']
        return random.choice(optimization_types)

    def choose_geometry_convergence(self):
        """Randomly chooses a convergence type."""
        geom_convergence = ORCADocumentationHandler.choose_random_keyword(
            keywords_simple_input.geometry_convergence)
        return geom_convergence

    def get_hessian_calculation_settings(self):
        return "Calc_Hess true\nRecalc_Hess 1"

    def get_relaxed_scan_settings(self):
        """Getter for the settings needed to perform a relaxed surface scan."""
        bond_lengths = self.calculate_bond_lengths()
        scan_lengths = random.choice(['B %d %d = %.2f, %.2f, 5' % (
            distance[0][0], distance[0][1], distance[1], distance[1] * 2) for distance in bond_lengths])
        return f"Scan\n{scan_lengths}\nend"

    def get_constraint_settings(self):
        """Getter for the settings needed for constraining the optimization."""

        distances, angles, dihedral_angles = self.generate_constraints()
        distance_constraints_block = ['{B %d %d %.2f C}' % (
            distance[0][0], distance[0][1], distance[1]) for distance in distances]
        angle_constraints_block = ['{A %d %d %d %.2f C}' % (
            angle[0][0], angle[0][1], angle[0][2], angle[1]) for angle in angles]
        dihedral_angle_constraints_block = ['{A %d %d %d %d %.2f C}' % (
            angle[0][0], angle[0][1], angle[0][2], angle[0][3], angle[1]) for angle in dihedral_angles]
        return f"Constraints\n{"\n".join(distance_constraints_block)}\nend"

    def generate_constraints(self):
        """Calculate the possible constraint settings based on the provided molecule."""
        distance_constraints = self.calculate_bond_lengths()
        self.molecule.set_default_graph()
        angle_constraints = self.calculate_bond_angles()
        dihedral_angle_constraints = self.calculate_dihedral_angles()
        return distance_constraints, angle_constraints, dihedral_angle_constraints

    def calculate_bond_lengths(self):
        return [((i, j), 0.529177249 * bond_length([self.molecule.coordinates[i], self.molecule.coordinates[j]])[0])
                for i in range(len(self.basisSetHandler.elements)) for j in range(i+1, len(self.basisSetHandler.elements))]

    def calculate_bond_angles(self):
        """Calculates the bond angels for the given molecule."""

        angle_constraints = []

        # 1) Build a list of atom indexes involved in angles.
        angles = []

        for i0 in range(self.molecule.size):
            # For each atom we will find all bending angles centered at the current
            # atom. For this we construct (an ordered!) list of all bonded neighbors.
            n = list(self.molecule.graph.neighbors[i0])
            # The second loop iterates over all neighbors. The enumerate function is
            # used to assign a counter value to the variable index.
            for index, i1 in enumerate(n):
                # The third loop iterates over all other neighbors that came before i1.
                for i2 in n[:index]:
                    # Each triple is stored as an item in the list angles.
                    angles.append((i0, i1, i2))

        # 2) Iterate over all angles, compute and print.
        for i0, i1, i2 in angles:
            # Notice again the [0] at the end.
            angle = ((i0, i1, i2),  0.529177249 *
                     bend_angle(self.molecule.coordinates[[i0, i1, i2]])[0])
            angle_constraints.append(angle)
        return angle_constraints

    def calculate_dihedral_angles(self):
        """Calculates the dihedral angels for the given molecule."""
        dihedrals = []
        dihedral_constraints = []

        for i0 in range(self.molecule.size):
            n = list(self.molecule.graph.neighbors[i0])
            # Iterate over all pairs of bonded neighbors
            for i1_index, i1 in enumerate(n):
                for i2_index in range(i1_index + 1, len(n)):
                    i2 = n[i2_index]

                    # Iterate over all neighbors of i1 that come before i2
                    for i3 in n[:i1_index]:
                        # For each combination of four atoms, store them as a tuple in the list dihedrals
                        dihedrals.append((i0, i1, i2, i3))

        for i0, i1, i2, i3 in dihedrals:
            dihedral_constraints.append(
                ((i0, i1, i2, i3),  0.529177249 * dihed_angle(self.molecule.coordinates[i0, i1, i2, i3][0])))
        return dihedral_constraints
