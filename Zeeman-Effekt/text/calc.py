import numpy as np
import scipy as sp
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show, array

h=6.62606876e-34
c=299792458
mu=-9.27400899e-24
#I=5
a= 61.23769853
da= 0.50050078
b= 11.74020588
db= 4.6951124
#B=a*I+b
#B=0.593498341915
#DB=0.00668220012246

B=0.31792869853
DB=0.00532039530657

#B=0.960924533095
#DB=0.00906790786751

#gaussB= np.sqrt( ( I*da )**2 + (1*db)**2 )
#print(B)
#print(gaussB)

#dlam normal:
#dlam=1.11801268255e-11
#Dlam=0.0261742187244e-11

#dlam anormal1 zirkular:
dlam= 4.45250571816e-12
Dlam= 0.215951778182e-12

#dlam anormal2 linear:
#dlam= 4.56570632339e-12
#Dlam= 0.415188327987e-12

lam=643.8e-9
#lam=480.0e-09
dE=-(h*c)/(lam**2)

g = 1/(mu * B)*( (h * c)/(lam**2) ) * dlam
print(g)
#mdlam = -(h c)/(mu B dlam**2)
#mB = -(h c)/(mu dlam B**2)

gauss= np.sqrt( ( 2 * (h * c * dlam)/(mu * B * lam**2) * Dlam )**2 + ( (h * c * dlam)/(mu * lam**2 * B**2) * DB )**2 )
print(gauss)



#zirkular g_ij= -15131113.258429853 +- 776339.447163
