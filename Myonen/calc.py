import numpy as np
import scipy as sp
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show, array

#N=np.sqrt() print(N)


#NS=1397196
#TS=10e-6
#TG=73966
#C=508
#
#N=NS*TS/TG
#dN=sp.sqrt(NS)*TS/TG
#
N=0.00018889706081172433
#dN=1.5980727043e-07
#N = sympy.var('N')

#P=N*np.e**(-N)
#dP=np.sqrt( (-1.0*2.71828182845905**(-N)*N + 2.71828182845905**(-N))**2 * dN**2 )

P=0.000188861382082
#dP=1.59746904735e-07

#U=P*NS/C
#dUP=U.diff(P)
#print(dUP)
#dUNS=U.diff(NS)

U=0.5194416685028387
#dP=P.diff(N)
#print(dP)


print('ab hier neu mit Poisson')
print('dN')
dN=np.sqrt(N)
print(dN)
print('dP')
dP=np.sqrt(P)
print(dP)
print('dU')
dU=np.sqrt(U)
print(dU)
