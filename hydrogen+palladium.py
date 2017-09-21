from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import QuasiNewton
from ase.build import surface, fcc111, add_adsorbate
from ase.spacegroup import crystal
from ase.visualize import view
from ase.io import write
from ase.io import read

h = 1.85
d = 1.10

Pd_slab_path = 'Pd_111.traj'
H2_slab_path = 'ads_H2.traj'

#slab = fcc111('Cu', size=(4, 4, 2), vacuum=10.0)
Pd_slab = read(Pd_slab_path)
H2_molecule = read(H2_slab_path)

H2_molecule.set_calculator(EMT())
Pd_slab.set_calculator(EMT())

add_adsorbate(Pd_slab, H2_molecule, h, position=(2, 1))
#add_adsorbate(Pd_slab, H2_molecule, h, position=(1, 0), offset=2)

constraint = FixAtoms(mask=[a.symbol != 'H' for a in Pd_slab])
Pd_slab.set_constraint(constraint)
dyn = QuasiNewton(Pd_slab, trajectory='PdH2_adsorbed.traj')
dyn.run(fmax=0.05)

#write('PdH2_adsorbed.traj',Pd_slab)

#slab.set_calculator(EMT())
#e_slab = slab.get_potential_energy()

#molecule = Atoms('2N', positions=[(0., 0., 0.), (0., 0., d)])
#molecule.set_calculator(EMT())
#e_N2 = molecule.get_potential_energy()

#add_adsorbate(slab, molecule, h, 'ontop')
#constraint = FixAtoms(mask=[a.symbol != 'N' for a in slab])
#slab.set_constraint(constraint)
#dyn = QuasiNewton(slab, trajectory='N2Cu.traj')
#dyn.run(fmax=0.05)

#print('Adsorption energy:', e_slab + e_N2 - slab.get_potential_energy())
from ase.visualize import view
view(Pd_slab)
