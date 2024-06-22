from Classes.ORCAGenerators.ORCAGenerator import ORCAGenerator
from Classes.Calculations.SinglePointCalculations.DFTCalculation import DFTCalculation
from Classes.Calculations.SinglePointCalculations.HFCalculation import HFCalculation
from Classes.Calculations.SinglePointCalculations.CCCalculation import CCCalculation
from Classes.Calculations.SpecializedCalculations.GeometryOptimization import HFGeometryOptimization
from Classes.Calculations.SpecializedCalculations.GeometryOptimization import DFTGeometryOptimization
from Classes.Calculations.SpecializedCalculations.GeometryOptimization import CCGeometryOptimization
from Classes.Calculations.SpecializedCalculations.ExcitedStatesCalculation import DFTExcitedStatesCalculation
from Classes.Calculations.SpecializedCalculations.ExcitedStatesCalculation import HFExcitedStatesCalculation
from Classes.Calculations.SpecializedCalculations.ExcitedStatesCalculation import CCExcitedStatesCalculation
from Classes.Calculations.SpecializedCalculations.FrequencyCalculation import HFFrequencyCalculation
from Classes.Calculations.SpecializedCalculations.FrequencyCalculation import DFTFrequencyCalculation
from Classes.Calculations.SpecializedCalculations.FrequencyCalculation import CCFrequencyCalculation
from Classes.Helpers.OrcaInputFileManipulator import OrcaInputFileManipulator
from Classes.Helpers.OrcaRunner import OrcaRunner
import random
import os

class RuleBasedORCAGenerator(ORCAGenerator):
    def __init__(self, save_folder, input_file_prefix="rule_based", output_folder="Orca Output"):
        super().__init__(save_folder, input_file_prefix, output_folder)

    def generate_input_file(self, accept_warnings, calculation_type='dft', add_solvation=False):
        calculation = None 
        xyz, molecule_file, molecule_type = OrcaInputFileManipulator.get_random_xyz(max_atoms=3)
        # We always define the calculation type, the default is a single point (if no calculation type is defined)    
        if calculation_type == "dft":
            print("Generating Single Point Density Functional Theory Calculation...")
            calculation = DFTCalculation(xyz=xyz,
                                        molecule_file=molecule_file, 
                                        molecule_type=molecule_type,
                                        use_ri_approximation=random.choice([True,False]),
                                        use_dispersion=random.choice([True, False]),
                                        use_nl=random.choice([True, False]),
                                        add_solvation=add_solvation)

        elif calculation_type == 'hf':
            print("Generating Single Point Hartree Fock Calculation...")
            calculation = HFCalculation(xyz=xyz,
                                        molecule_file=molecule_file,
                                        molecule_type=molecule_type,
                                        use_mp2=random.choice([True, False]),
                                        use_ri=random.choice([True, False]),
                                        add_solvation=add_solvation
                                        )
        
        elif calculation_type == 'cc':
            print("Generating Single Point Coupled Cluster Calculation...")
            calculation = CCCalculation(xyz=xyz,
                                        molecule_file=molecule_file,
                                        molecule_type=molecule_type,
                                        add_solvation=add_solvation,
                                        use_densities=random.choice([True, False])
                                        )
        
        elif calculation_type == 'dft_opt':
            print("Generating a DFT Geometry Optimization...")
            calculation = DFTGeometryOptimization(xyz=xyz,
                                                molecule_file=molecule_file,
                                                molecule_type=molecule_type,
                                                use_ri_approximation=random.choice([True,False]),
                                                use_dispersion=random.choice([True,False]),
                                                use_nl=random.choice([True, False]),
                                                do_relaxed_scan=True,
                                                calculate_hessian=random.choice([True, False]),
                                                use_constraints=random.choice([True, False]),
                                                add_solvation=add_solvation)
            
        elif calculation_type == 'hf_opt':
            print("Generating an HF Geometry Optimization...")
            calculation = HFGeometryOptimization(xyz=xyz,
                                                molecule_file=molecule_file,
                                                molecule_type=molecule_type,
                                                use_mp2=random.choice([True, False]),
                                                use_ri=random.choice([True, False]),
                                                do_relaxed_scan=random.choice([True, False]),
                                                calculate_hessian=random.choice([True, False]),
                                                use_constraints=random.choice([True, False]),
                                                add_solvation=add_solvation
                                                )
        elif calculation_type == 'cc_opt':
            print("Generating a CC Geometry Optimization...")
            calculation = CCGeometryOptimization(xyz=xyz,
                                                molecule_file=molecule_file,
                                                molecule_type=molecule_type,
                                                add_solvation=add_solvation,
                                                do_relaxed_scan=random.choice([True, False]),
                                                calculate_hessian=False,
                                                use_constraints=random.choice([True, False])
                                                )
        elif calculation_type == 'dft_es':
            print("Generating a DFT Excited States Calculation...")
            calculation = DFTExcitedStatesCalculation(xyz=xyz,
                                        molecule_file=molecule_file, 
                                        molecule_type=molecule_type,
                                        add_solvation=add_solvation,
                                        use_ri_approximation=random.choice([True,False]),
                                        print_population=random.choice([True, False]),
                                        use_densities=random.choice([True, False]),
                                        use_dcorr=random.choice([True,False]),
                                        use_scs=random.choice([True, False]),
                                        use_tda=random.choice([True, False]),
                                        mode=random.choice(['stda', 'stddft', False]),
                                        do_soc=random.choice([True, False]),
                                        use_triplets=random.choice([True, False]),
                                        use_nacme=random.choice([True, False]),
                                        use_spin_flip=False)
        
        elif calculation_type == 'hf_es':
            print("Generating an HF Excited States Calculation...")
            calculation = HFExcitedStatesCalculation(
                                    xyz=xyz,
                                    molecule_file=molecule_file,
                                    molecule_type=molecule_type,
                                    add_solvation=add_solvation,
                                    use_mp2=random.choice([True, False]),
                                    use_ri=random.choice([True, False]),
                                    print_population=random.choice([True, False]),
                                    use_densities=random.choice([True, False]),
                                    do_soc=random.choice([True, False]),
                                    use_triplets=random.choice([True, False]),
                                    use_nacme=random.choice([True, False]),
                                    use_spin_flip=False)
            
        elif calculation_type == 'cc_es':
            print("Generating a CC Excited States Calculation...")
            calculation = CCExcitedStatesCalculation(
                                    xyz=xyz,
                                    molecule_file=molecule_file,
                                    molecule_type=molecule_type,
                                    add_solvation=add_solvation,
                                    use_triplets=random.choice([True, False]),
                                    do_db_filter=random.choice([True,False]),
                                    use_QROs=random.choice([True,False])
                                    )
                
        elif calculation_type == 'dft_freq':
            print("Generating a DFT Frequency Calculation...")
            calculation = DFTFrequencyCalculation(xyz=xyz,
                                                molecule_file=molecule_file,
                                                molecule_type=molecule_type,
                                                add_solvation=add_solvation,
                                                use_geom=random.choice([True, False]),
                                                use_ri_approximation=random.choice([True,False]),
                                                use_dispersion=random.choice([True,False]),
                                                use_nl=random.choice([True, False]),
                                                do_relaxed_scan=random.choice([True, False]),
                                                calculate_hessian=random.choice([True, False]),
                                                use_constraints=random.choice([True, False]),
                                                use_cd=random.choice([True,False]))
        elif calculation_type == 'hf_freq':
            print("Generating an HF Frequency Calculation...")
            calculation = HFFrequencyCalculation(xyz=xyz,
                                                molecule_file=molecule_file,
                                                molecule_type=molecule_type,
                                                add_solvation=add_solvation,
                                                use_geom=random.choice([True, False]),
                                                use_mp2=random.choice([True, False]),
                                                use_ri=random.choice([True, False]),
                                                do_relaxed_scan=random.choice([True, False]),
                                                calculate_hessian=random.choice([True, False]),
                                                use_constraints=random.choice([True, False]),
                                                use_cd=random.choice([True,False]))
        elif calculation_type == 'cc_freq':
            print("Generating a CC Frequency Calculation...")
            calculation = CCFrequencyCalculation(xyz=xyz,
                                                molecule_file=molecule_file,
                                                molecule_type=molecule_type,
                                                use_geom=random.choice([True, False]),
                                                add_solvation=add_solvation,
                                                do_relaxed_scan=random.choice([True, False]),
                                                calculate_hessian=False,
                                                use_constraints=random.choice([True, False]))
        
        calculation.process_keywords()
        calculation.process_input_blocks()
        input_file = calculation.generate_input_file()
        input_file = self.add_parallelization(input_file=input_file, 
                                                n_pal=6)
        
        if OrcaInputFileManipulator.remove_xyz(OrcaInputFileManipulator.remove_smiles_comment(input_file)) not in self.generated_input_files:

            input_file_name, input_file_path = self.save_inp_to_file(input_file)

            completed = OrcaRunner.run_orca(
                self.save_folder, input_file_name, self.output_folder, r"C:\Users\Pieter\Orca\orca.exe")

            if completed != 0:
                os.remove(input_file_path)
                return False, input_file
            else:
                if not accept_warnings and len(self.get_warnings(input_file_name=input_file_name)) > 0:
                    return False, None
                print(f"Input file saved to {input_file_path}")
                
            return True, input_file
        return False, None

    def get_supported_calculations():
        return ['dft', 'hf', 'cc', 'dft_opt', 'hf_opt', 'cc_opt', 
                'dft_es', 'hf_es', 'cc_es', 'dft_freq', 'hf_freq', 'cc_freq']