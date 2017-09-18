from ase.io import read
from espresso import espresso
from ase.optimize import QuasiNewton

#f = open('WCl_adsorption/W_geometry_optimization_500_441/energy.txt', 'w')
#f.write('starting')  # python will convert \n to os.linesep

W_slab=read('WCl_adsorption/W_111.traj')
W_slab.calc=espresso(pw=450,
                       dw=4500,
                       kpts=(5,7,1),
                       xc='PBE',
                       outdir='WCl_adsorption/W_geometry_optimization_450_571/E_W_slab',#espresso outdirectory saved
                                            #here                                    
                       convergence={'energy':1e-6,
                                    'mixing':0.05,
                                    'mixing_mode':'local-TF',
                                    'maxsteps':1000,
                                    'diag':'cg'})

relax_W_slab=QuasiNewton(W_slab,
                           logfile='WCl_adsorption/W_geometry_optimization_450_571/opt.log',
                           trajectory='WCl_adsorption/W_geometry_optimization_450_571/opt.traj',
                           restart='WCl_adsorption/W_geometry_optimization_450_571/opt.pckl') #ase output
relax_W_slab.run(fmax=0.05)

E_W_slab=W_slab.get_potential_energy()
#f.write(E_W_slab)
#f.write('\n END')
#f.close()  # you can omit in most cases as the destructor will call it
print(E_W_slab)
