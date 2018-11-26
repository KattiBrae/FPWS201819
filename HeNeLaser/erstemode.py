import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Graphik1')
print('Steigung','Y-Achsenabschnitt')
R, y = np.loadtxt('erstemode.txt', unpack=True,delimiter=',')


def f(R,phi,w,l,b):
    return sympy.cos(l*phi)(4*2*np.pi)/(R*w)/((1+(2*z/R)**2)**((1+l)/2))
popt, pcov = curve_fit(f, R, y)
print(popt)
print(np.diag(pcov))
R_new = np.linspace(x[0], x[-1], 500)



plt.figure(1)
plt.plot(R,y,'x')
plt.plot(R_new,f(R_new,*popt),'-', label='Lineare Regression')
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')
plt.grid()
plt.legend()




plt.savefig('erstemode.pdf')
print ('Fertig')
