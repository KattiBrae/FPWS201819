import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show


f = np.loadtxt('maxa.txt', unpack=True)
print(f)
c = 343.28
l = c / f
print(l)
k=(2*np.pi)/l
print(k)
w = 2*np.pi *f


print('Graphik1')
print('Steigung','Y-Achsenabschnitt')


def g(k,a,b):
    return a*k**2
Werte, Fehler = curve_fit(g, k, f)
print(Werte)
print(np.diag(Fehler**2)**(1/4))


k_new = np.linspace(k[0], k[-1], 500)

h = 6.62607004e-34
m = 9.10938356*10**(-31)
E = (h**2*k**2)/(2*m)
print(E)
plt.figure(1)
plt.plot(k_new,g(k_new,*Werte),'-')#, label='Fitfunktion $\Delta f \sim 1/d$')
#plt.plot(k,E)
plt.plot(k,f,'x', label="Messwerte")
plt.ylabel(r'$f$ (k)')
plt.xlabel(r'k')
plt.grid()
plt.legend()

plt.savefig('f(k).pdf')
print ('Fertig')
