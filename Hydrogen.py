from ase.build import molecule
from ase.io import write
from ase.build import surface
from ase.spacegroup import crystal
from ase.visualize import view

atoms=molecule('H2')
atoms.center(10)

#write the .traj file
write('ads_H2.traj',atoms)
#write the POSCAR file incase the .traj file cannot be read
write('POSCAR',atoms)
view(atoms)
