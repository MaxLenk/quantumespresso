from ase.io import read
from espresso import espresso
from ase.optimize import QuasiNewton

#f = open('WCl_adsorption/W_geometry_optimization_500_441/energy.txt', 'w')
#f.write('starting')  # python will convert \n to os.linesep

Pd_slab_path = 'Pd_111.traj'
output_directory = 'Pd_geometry_optimization_450_571/'

Pd_slab=read('Pd_slab_path')
Pd_slab.calc=espresso(pw=450,
                       dw=4500,
                       kpts=(5,7,1),
                       xc='PBE',
                       outdir= output_directory + 'E_Pd_slab',#espresso outdirectory saved
                                            #here                                    
                       convergence={'energy':1e-6,
                                    'mixing':0.05,
                                    'mixing_mode':'local-TF',
                                    'maxsteps':1000,
                                    'diag':'cg'})

relax_Pd_slab=QuasiNewton(Pd_slab,
                           logfile=output_directory + 'opt.log',
                           trajectory=output_directory + 'opt.traj',
                           restart=output_directory + 'opt.pckl') #ase output
relax_Pd_slab.run(fmax=0.05)

E_Pd_slab=Pd_slab.get_potential_energy()
#f.write(E_W_slab)
#f.write('\n END')
#f.close()  # you can omit in most cases as the destructor will call it
print(E_Pd_slab)
