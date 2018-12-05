import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Graphik1')
print('Steigung','Y-Achsenabschnitt')
m, n = np.loadtxt('polarisation.txt', unpack=True,delimiter=',')
x, y = np.loadtxt('polarisation1.txt', unpack=True,delimiter=',')


def f(x,a,b,c,d):
    return a*np.sin(b*x+c)+d
popt, pcov = curve_fit(f, x, y, p0=[10,0.05,3,8])
print(popt)
print(np.diag(pcov))

x_new = np.linspace(0, x[-1], 500)



plt.figure(1)
plt.plot(m,n,'x')
#plt.plot(x,y,'x')
plt.plot(x_new,f(x_new,*popt),'-', label='Fit $\propto \cos{(\sigma)}$')
plt.xlabel(r'$\sigma$/°')
plt.ylabel('I/$\mu$A')
plt.grid()
plt.legend()




plt.savefig('polarisation.pdf')
print ('Fertig')
