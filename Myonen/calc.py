import numpy as np
import scipy as sp
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show, array

#N=np.sqrt() print(N)

#N=np.sqrt() print(N)
#N=np.sqrt() print(N)

N=1.8888408187545629e-06
dN=1.59801780233e-08

P=2.71828182845905**(-N)*N
dP=sp.sqrt( (1.0*2.71828182845905**(-N)*N + 2.71828182845905**(-N))**2 * dN**2 )

C=509
#print(P)
#print(dP)

#
#P = N*np.e**(-N)
#print(P)
#
#print(P.diff(N))
#e=1.8932e-06
#t=2.199e-06
#f=(e-t)/t*100
#print(f)

U=P*N/C
print(U)
dUP=sp.sqrt( (N/C)**2*dP**2 + (P/C)**2*dN**2)
print(dUP)
