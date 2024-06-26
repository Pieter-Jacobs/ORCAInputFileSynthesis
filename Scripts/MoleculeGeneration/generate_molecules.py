import numpy as np
import random as rd
import argparse as ap
import rdkit.Chem as rdc
import rdkit.Chem.AllChem as rdca
import selfies as sf
from rdkit.Chem.Descriptors import NumRadicalElectrons
import rdkit.Chem as chem
import os

def random_selfies(samples, length, size_limit, alphabet):
    """
    Generate random SELFIES strings, decode them to SMILES,
    filter by the maximum number of atoms, and return a list of canonical SMILES.
    
    Args:
    - samples (int): Number of random SELFIES generated.
    - length (int): Number of SELFIES characters in each random string.
    - size_limit (int): Maximum number of atoms allowed in generated molecules.
    - alphabet (list): List of SELFIES characters to use.

    Returns:
    - smiles_list (list): List of unique canonical SMILES strings.
    """
    random_selfies = ["".join(rd.choices(alphabet, k=length)) for _ in range(samples)]
    smiles_list = [sf.decoder(si) for si in random_selfies if rdc.MolFromSmiles(sf.decoder(si)).GetNumAtoms(onlyExplicit=False) <= size_limit]
    smiles_list = [rdc.MolToSmiles(rdc.MolFromSmiles(si)) for si in smiles_list]
    return smiles_list

def abstract_hydrogen(smiles):
    """
    Abstract a hydrogen atom from the given SMILES string to create a radical form,
    if possible using predefined SMARTS patterns.

    Args:
    - smiles (str): Input SMILES string.

    Returns:
    - str: Modified SMILES string with abstracted hydrogen or the original if no abstraction is possible.
    """
    if '[H]' in rdc.MolToSmiles(rdc.AddHs(rdc.MolFromSmiles(smiles))):
        smarts_list = [r'[*&H4:1]>>[*&H3:1]', r'[*&H3:1]>>[*&H2:1]',
                       r'[*&H2:1]>>[*&H1:1]', r'[*&H1:1]>>[*&H0:1]']
        rd.shuffle(smarts_list)
        for sma in smarts_list:
            reaction = rdca.ReactionFromSmarts(sma)
            product_mol = reaction.RunReactants([rdc.MolFromSmiles(smiles)])
            if len(product_mol) != 0:
                return rdc.MolToSmiles(product_mol[0][0], kekuleSmiles=True)
        return smiles
    else:
        return smiles

class molecule:
    def __init__(self, smiles):
        """
        Initialize a molecule object from a given SMILES string.
        
        Args:
        - smiles (str): Input SMILES string.
        """
        self.smiles = smiles
        self.generate_coordinates()  # Generate XYZ coordinates upon initialization
        return

    def generate_coordinates_rdkit(self):
        """
        Convert the SMILES representation of the molecule to XYZ coordinates using RDKit.
        """
        try:
            self.mol = rdc.MolFromSmiles(self.smiles)
            self.mol = rdc.AddHs(self.mol)
            rdca.EmbedMolecule(self.mol)
            rdca.MMFFOptimizeMolecule(self.mol)
            rdc.rdMolTransforms.CanonicalizeMol(self.mol, normalizeCovar=True, ignoreHs=False)
            block = rdc.MolToMolBlock(self.mol)
            blocklines = block.split("\n")
            self.xyz = []
            self.atoms = []
            for line in blocklines[4:]:
                if len(line.split()) == 4:
                    break
                self.atoms.append(line.split()[3])
                self.xyz.append([float(line.split()[0]), float(line.split()[1]), float(line.split()[2])])
            self.xyz = np.array(self.xyz)
            self.atom_count = len(self.atoms)
        except:
            print(f"ERROR: Could not generate coordinates for molecule with SMILES: {self.smiles}")
            self.xyz = []

    def generate_coordinates(self):
        """
        Generate XYZ coordinates for the molecule and convert them to a formatted text representation.
        """
        self.generate_coordinates_rdkit()
        self.xyz_file = self.convert_xyz()
        return

    def convert_xyz(self):
        """
        Convert XYZ coordinates of the molecule to a formatted text block.
        
        Returns:
        - str: Formatted text block representing XYZ coordinates.
        """
        if list(self.xyz):
            text = ''
            for line in range(self.atom_count):
                text += self.atoms[line]
                text += format(format(self.xyz[line][0], '.9f'), '>14s')
                text += format(format(self.xyz[line][1], '.9f'), '>14s')
                text += format(format(self.xyz[line][2], '.9f'), '>14s')
                text += "\n"
        else:
            text = ""
        return text

if __name__ == "__main__":
    # Parse command line arguments
    parser = ap.ArgumentParser()
    parser.add_argument("--samples", type=int, default=100,
                        help="Number of random SELFIES generated.")
    parser.add_argument("--length", type=int, default=10,
                        help="Number of SELFIES characters in each random SELFIES.")
    parser.add_argument("--size_limit", type=int, default=4,
                        help="Maximum number of atoms in generated molecules.")
    parser.add_argument("--abstract_hydrogen", type=bool, default=True,
                        help="Abstract a hydrogen from the generated molecules to create radicals.")
    args = parser.parse_args()

    # Set constraints and alphabet for SELFIES generation
    sf.set_semantic_constraints()
    alphabet = list(sf.get_semantic_robust_alphabet())
    alphabet = [ai for ai in alphabet if ("+" not in ai) and ("-" not in ai)]  # Remove charged atoms
    alphabet = [ai for ai in alphabet if ai not in ['[=B]', '[#B]', '[=P]', '[#P]', '[#S]', '[Br]', '[I]']]  # Remove unusual atom types

    # Generate random molecules based on SELFIES
    smiles_list = random_selfies(args.samples, args.length, args.size_limit, alphabet=alphabet)
    smiles_list = list(set(smiles_list))  # Ensure uniqueness

    # Optional: Abstract hydrogen to create radicals
    if args.abstract_hydrogen == True:
        try:
            smiles_list = [abstract_hydrogen(si) for si in smiles_list]
        except:
            pass

    # Generate Cartesian coordinates for each molecule
    molecules_list = [molecule(si) for si in smiles_list]
    print("Unique molecules: {}".format(len(smiles_list)))

    # Save XYZ coordinates to files
    for mi in molecules_list:
        saved_new = False
        file_path = f"Data{os.sep}MoleculesRadical{os.sep}{mi.smiles}.txt" if NumRadicalElectrons(chem.MolFromSmiles(sf.decoder(sf.encoder(mi.smiles)))) != 0 else f"Data{os.sep}Molecules{os.sep}{mi.smiles}.txt"
        try:
            if not os.path.exists(file_path):
                with open(file_path, 'w') as file:
                    file.write("*xyz 0 2 \n" if NumRadicalElectrons(chem.MolFromSmiles(sf.decoder(sf.encoder(mi.smiles)))) != 0 else "*xyz 0 1 \n")
                    file.write(mi.xyz_file)
                    file.write("*")
                saved_new = True
        except Exception as err:
            print(err)
