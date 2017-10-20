from ase.spacegroup import crystal
from ase.visualize import view
from ase.build import surface
from ase.build import bulk
from ase.io import write

#build the Pt crystal structure
a=3.859 #angstrom
#Pd=crystal(['Pd'],basis=[(0,0,0)],spacegroup=225,cellpar=[a,a,a,90,90,90])
Pd_bulk = bulk('Pd','fcc',a,cubic=True)

#build the (111) surface slab
Pd_bulk_surface=surface(Pd_bulk,(1,1,1),2)
Pd_bulk_surface.center(vacuum=10,axis=2)

#repeat slab
Pd_111_repeat=Pd_bulk_surface.repeat((2,1,1))
#(1,2,1) corresponds to repeat how many times in x,y,z direction

#save .traj file
write('PdH2_adsorption/Pd_bulk_surface.traj',Pd_bulk_surface)
write('PdH2_adsorption/POSCAR',Pd_111_repeat) #in case the .traj file cannot be read
view(Pd_111_repeat)
