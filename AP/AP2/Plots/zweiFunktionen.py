import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Graphik1')

x, y = np.loadtxt('tab1.txt', unpack=True,delimiter=',')

def f(x,a,b):
    return a*x+b
popt, pcov = curve_fit(f, x, y)
print(popt)
print(pcov)

x_new = np.linspace(x[0], x[-1], 500)


print('Graphik2')

z, u = np.loadtxt('tab2.txt', unpack=True,delimiter=',')

def q(z,e,w):
    return e*z**2+w
popt2, pcov2 = curve_fit(q, z, u)
print(popt2)
print(pcov2)

z_new = np.linspace(z[0], z[-1], 500)



plt.figure(1)
plt.plot(x,y,'x')
plt.plot(z,u,'x')
plt.plot(x_new,f(x_new,*popt),'-', label='Messung1')
plt.plot(z_new,q(z_new,*popt2),'-',label='Messung2')

plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')
plt.grid()
plt.legend()




plt.savefig('zweiFunktionen.pdf')
print ('Fertig')
