##########################################################################
#Importing packages
##########################################################################
import os
import numpy as np
import pandas as pd 
import multiprocessing 
from datetime import datetime
from multiprocessing import Pool
from colossus.halo import profile_dk14
from colossus.cosmology import cosmology


##########################################################################
#Loading test data
##########################################################################
X_test_actual = pd.read_csv("Data/X_test_actual.csv")


##########################################################################
#Function to compute DK14 density
##########################################################################
#----------Setting Cosmology. This is a global set up
params = {'flat': True, 'H0': 70, 'Om0': 0.286, 'Ob0': 0.046, 'sigma8': 0.82, 'ns': 0.96}
cosmo = cosmology.setCosmology('my_cosmo', params)

def diemer_14(split_chunk):
    '''
    This functions takes a chunk of data, fits the DK14 profile  to 
    compute the densities, and then returns the squared difference between 
    the DK14 predictions and the actual densities.
    #----------Argument/Input:
        split_chunk: A chunk of data set. Variables in this data set is to 
                     be used to calibrate the densities.
    #----------Output(s):
        Saves the squared difference between the DK14 predictions and the actual 
        densities into a .npy file.
    '''
    DK14_Density = []
    # #----------Setting Cosmology.
    # params = {'flat': True, 'H0': 70, 'Om0': 0.286, 'Ob0': 0.046, 'sigma8': 0.82, 'ns': 0.96}
    # cosmo = cosmology.setCosmology('my_cosmo', params)
    for i in range(len(split_chunk)):
        '''
        #-------------Paramters
        Mvir: virial mass of halo
        Rvir: virial radius
        rs: virial radius
        z_orig: redshift of the halo
        Density: The actual density of the halo
        '''
        Mvir, Rvir, rs, z_orig, r_mid, Density = split_chunk[i]
        #----------------------------DK14 density
        p_dk14_51 = profile_dk14.getDK14ProfileWithOuterTerms(M = Mvir,
                                                              c = Rvir/rs,
                                                              z = z_orig, mdef = 'vir', 
                                                              outer_term_names = ['pl'])
        rho_dk14_5 = p_dk14_51.density(r_mid*1000)*1e9
        squared_diff = (Density-np.log(rho_dk14_5))**2
        DK14_Density.append(squared_diff)
    #----------------------------Save output to .npy files
    filename = f"{datetime.today().isoformat()}.npy"
    f = open(f"DK14_mse/{filename}", "wb")
    np.save(f, DK14_Density)
    f.close()



##########################################################################
#Parallelising code
##########################################################################
mydir = "DK14_mse/"
filelist = [f for f in os.listdir(mydir) if f.endswith(".npy") ]
#----------------------------delete all files ending with .npy in this directory
for f in filelist:
    os.remove(os.path.join(mydir, f))
#----------------------------number of processors to use. We use all available processors.
processors = multiprocessing.cpu_count()
# dk14data = X_test_actual[["Mvir_Msun.h", "Rvir_Mpc.h", "rs", "z_orig", "r_mid_phys", "Density"]].iloc[0:1000, :].values#.reshape(1,-1)
dk14data = X_test_actual[["Mvir_Msun.h", "Rvir_Mpc.h", "rs", "z_orig", "r_mid_phys", "Density"]].values#.reshape(1,-1)
split_data = np.array_split(dk14data, processors)

if __name__ == '__main__':
    '''
    Each chunk of data is set to run on a different processors. 
    Each processor stores the results in a separate .npy file. 
    The files are named using time stamps.
    '''

    with Pool(processes=processors) as p:
    # with Pool() as p: #this line equally works as the line above
        p.map(func = diemer_14, iterable = split_data)






