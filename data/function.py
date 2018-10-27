import numpy as np
#
############################
# ARGUMENTS
# k0, k1, k2 are model parameters, to be identified
# lamda is a numpy array containing the levels of tissue elongation at which the stress is to be known
# NOTE: lamda from experiments is the first column in the Test.dat files, while second column is stress
############################
#
def PK1(k0,k1,k2,lamda):
    return (lamda**3.-1.)/((9.*lamda**4.))*(9.*lamda*k0+2.*k1*(lamda-1.)**2.*(lamda+2.)*np.exp(k2*(lamda**3.-3.*lamda+2.)**2./(9.*lamda**2.)))