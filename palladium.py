
from ase.spacegroup import crystal
from ase.visualize import view
from ase.build import surface
from ase.io import write

#build the Pt crystal structure
a=3.859 #angstrom
Pd=crystal(['Pd'],basis=[(0,0,0)],spacegroup=225,cellpar=[a,a,a,90,90,90])

#build the (111) surface slab
Pd_111=surface(Pd,(1,1,1),2)
Pd_111.center(vacuum=10,axis=2)

#repeat slab
Pd_111_repeat=Pd_111.repeat((4,4,4))
#(1,2,1) corresponds to repeat how many times in x,y,z direction

#save .traj file
write('Pd_111.traj',Pd_111_repeat)
write('POSCAR',Pd_111_repeat) #in case the .traj file cannot be read
view(Pd_111_repeat)
