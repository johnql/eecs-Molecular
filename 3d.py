# -*- coding: utf-8 -*-
import ase


import pandas as pd

struct_file = pd.read_csv('../champs-scalar-coupling/structures.csv')
import random

# Select a molecule
random_molecule = random.choice(struct_file['molecule_name'].unique())
molecule = struct_file[struct_file['molecule_name'] == random_molecule]
display(molecule)

# Get atomic coordinates
atoms = molecule.iloc[:, 3:].values
print(atoms)

# Get atomic symbols
symbols = molecule.iloc[:, 2].values
print(symbols)

from ase import Atoms
import ase.visualize

system = Atoms(positions=atoms, symbols=symbols)

ase.visualize.view(system, viewer="x3d")