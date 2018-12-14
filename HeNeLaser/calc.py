import numpy as np
import scipy as sp
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show, array

b=1.04714595e+04
db=2.25989252e+02

omega= np.sqrt(2/b)
#omega=13.8201127485
print(omega)

diffomega=np.sqrt(2)*(-1/2)*b**(-3/2)

domega=np.sqrt( (np.sqrt(2)*(-1/2)*b**(-3/2))**2*db**2 )
print(domega)
