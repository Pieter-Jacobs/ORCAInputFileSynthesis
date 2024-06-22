# import packages
import numpy as np
import random as rd
import argparse as ap
import rdkit.Chem as rdc
import rdkit.Chem.AllChem as rdca
import selfies as sf
from rdkit.Chem.Descriptors import NumRadicalElectrons
import rdkit.Chem as chem 
import os

# define utility functions
# taken from selfies package
def random_selfies(samples, length, size_limit, alphabet):
    random_selfies = ["".join(rd.choices(alphabet, k=length)) for _ in range(samples)]
    smiles_list = [sf.decoder(si) for si in random_selfies if rdc.MolFromSmiles(sf.decoder(si)).GetNumAtoms(onlyExplicit=False) <= size_limit]
    smiles_list = [rdc.MolToSmiles(rdc.MolFromSmiles(si)) for si in smiles_list] # get canonical smiles via roundtrip
    return smiles_list

# abstract hydrogen
def abstract_hydrogen(smiles):
    if '[H]' in rdc.MolToSmiles(rdc.AddHs(rdc.MolFromSmiles(smiles))):
        smarts_list = [r'[*&H4:1]>>[*&H3:1]', r'[*&H3:1]>>[*&H2:1]', r'[*&H2:1]>>[*&H1:1]', r'[*&H1:1]>>[*&H0:1]']
        rd.shuffle([r'[*&H4:1]>>[*&H3:1]', r'[*&H3:1]>>[*&H2:1]', r'[*&H2:1]>>[*&H1:1]', r'[*&H1:1]>>[*&H0:1]'])
        for sma in smarts_list:
            reaction = rdca.ReactionFromSmarts(sma)
            product_mol = reaction.RunReactants([rdc.MolFromSmiles(smiles)])
            if len(product_mol) != 0:
                return rdc.MolToSmiles(product_mol[0][0], kekuleSmiles=True)
            else:
                continue
            return smiles
    else:
        return smiles

# taken from tartarus package
class molecule:
    def __init__(self, smiles):
        self.smiles = smiles
        self.generate_coordinates()
        return
    
    def generate_coordinates_rdkit(self):
        """
        convert smiles to xyz coordinates using rdkit
        Authors: Pascal Friederich, Robert Pollice
        """
        try:
            self.mol = rdc.MolFromSmiles(self.smiles)
        except:
            print("ERROR: could not convert %s to rdkit molecule."%(self.smiles))
            self.xyz=[]
        try:
            self.mol = rdc.AddHs(self.mol)
        except:
            print("ERROR: could not add hydrogen to rdkit molecule of %s."%(self.smiles))
            self.xyz=[]
        try:
            rdca.EmbedMolecule(self.mol)
        except:
            print("ERROR: could not calculate 3D coordinates from rdkit molecule %s."%(self.smiles))
            self.xyz=[]
        try:
            rdca.MMFFOptimizeMolecule(self.mol)
        except:
            print("ERROR: could not optimize 3D coordinates for rdkit molecule %s."%(self.smiles))
            self.xyz=[]
        try:
            rdc.rdMolTransforms.CanonicalizeMol(self.mol, normalizeCovar=True, ignoreHs=False)
        except:
            print("ERROR: could not canonicalize 3D coordinates for rdkit molecule %s."%(self.smiles))
            self.xyz=[]
        try:
            block=rdc.MolToMolBlock(self.mol)
            blocklines=block.split("\n")
            self.xyz=[]
            self.atoms=[]
            for line in blocklines[4:]:
                if len(line.split())==4:
                    break
                self.atoms.append(line.split()[3])
                self.xyz.append([float(line.split()[0]),float(line.split()[1]),float(line.split()[2])])
            self.xyz=np.array(self.xyz)
            self.atom_count = len(self.atoms)
        except:
            print("ERROR: could not read xyz coordinates from rdkit molecule %s."%(self.smiles))
            self.xyz=[]
        
        return

    def generate_coordinates(self):
        # Generate XYZ from SMILES
        self.generate_coordinates_rdkit()
        self.xyz_file = self.convert_xyz()
        return

    def convert_xyz(self):
        if list(self.xyz): 
            text = ''
            for line in range(self.atom_count):
                text += self.atoms[line]
                text += format(format(self.xyz[line][0], '.9f'), '>14s')
                text += format(format(self.xyz[line][1], '.9f'), '>14s')
                text += format(format(self.xyz[line][2], '.9f'), '>14s')
                text += "\n"
        else:
            text =""
        return text


if __name__ == "__main__":
    count = 0
    while count < 1000:
        # parse command line input
        parser = ap.Arg_umentParser()
        parser.add_argument("--samples", type=int, default=100, help="Number of random SELFIES generated.")
        parser.add_argument("--length", type=int, default=10, help="Number of SELFIES characters in random SELFIES.")
        parser.add_argument("--size_limit", type=int, default=4, help="Maximum number of atoms in generated molecules.")
        parser.add_argument("--abstract_hydrogen", type=bool, default=True, help="Abstract a hydrogen from the generated molecules to create radicals.")
        args = parser.parse_args()
        
        # reset to defaults constraints
        sf.set_semantic_constraints()
        alphabet = list(sf.get_semantic_robust_alphabet())
        alphabet = [ai for ai in alphabet if ("+" not in ai) and ("-" not in ai)] # remove charged atoms
        alphabet = [ai for ai in alphabet if ai not in ['[=B]', '[#B]', '[=P]', '[#P]', '[#S]', '[Br]', '[I]']] # remove unusual atom types and very heavy atoms
   
        # create random molecules
        smiles_list = random_selfies(args.samples, args.length, args.size_limit, alphabet=alphabet)
        smiles_list = list(set(smiles_list))
        
        # optional hydrogen abstraction
        if args.abstract_hydrogen == True:
            try:
                smiles_list = [abstract_hydrogen(si) for si in smiles_list]
            except:
                pass
        
        # generate Cartesian coordinates
        molecules_list = [molecule(si) for si in smiles_list]
        print("Unique molecules: {}".format(len(smiles_list)))

        # Save xyzs to folder
        for mi in molecules_list:
            saved_new = False
            file_path = f"Data{os.sep}MoleculesRadical{os.sep}{mi.smiles}.txt"
            try: 
                molecule_smiles = sf.decoder(sf.encoder(mi.smiles))
                molecule_mol = chem.MolFromSmiles(molecule_smiles)
                n_unpaired_electrons = NumRadicalElectrons(molecule_mol) 
                if not os.path.exists(file_path) and n_unpaired_electrons != 0: 
                    with open(file_path, 'w') as file:
                        file.write("*xyz 0 2 \n")
                        file.write(mi.xyz_file)
                        file.write("*")
                    saved_new = True
                count += saved_new
            except Exception as err:
                print(err)