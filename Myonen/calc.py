import numpy as np
import scipy as sp
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show, array
NN=1397196-4719
print(NN)
#N=np.sqrt() print(N)
e=1392477
t=1397196
f=100*(e)/t
print(f)
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


print('ab hier mit poisson mit angempasstem komma')
#e-4
B=5.194416685028387
print(B)
dB=np.sqrt(B)
print(dB)
