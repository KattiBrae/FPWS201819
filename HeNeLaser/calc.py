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


print('Abweichung minima')
#  &\sigma_{\text{max, Fit}} &=&& \SI{50.97 \pm 0.38}{°} 17.71630370806357,   && \SI{230.97 \pm 0.38}{°} 5.641425293328138 \\
#  &\sigma_{\text{max, Wert}} &=&& \SI{ 60 }{°},                          && \SI{ 244 }{°} \\
#  &\sigma_{\text{min, Fit}} &=&& \SI{140.97 \pm 0.38}{°} 3.5681350641980574,  && \SI{320.97 \pm 0.38}{°} 2.1902358475869934 \\
#  &\sigma_{\text{min, Wert}} &=&& \SI{ 146 }{°},                         && \SI{ 328 }{°}. \\
e=146
t=320.97
f=100*(e-t)/t
print(f)
