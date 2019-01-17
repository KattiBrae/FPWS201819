
import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

x, y = np.loadtxt('tabelle.txt', unpack=True,delimiter=' ')
print(y)

c = 343.28
l = c / y
#print(l)
k=(2*np.pi)/l
print(k)
w = 2*np.pi *y

def f(k,a,b):
    return a*k+b
Werte, Fehler = curve_fit(f, k, y)
print(Werte)
print(np.diag(Fehler**2)**(1/4))


k_new = np.linspace(k[0], k[-1], 500)
plt.figure(3)
plt.plot(k,y,'x', label="Messwerte", color="red")
plt.plot(k_new,f(k_new,*Werte),'-', color="red", label='Fitfunktion')
plt.grid()
plt.ylabel(r'Frequenz / Hz')
plt.xlabel(r'k')
plt.legend()
#plt.show()
plt.savefig("A7.pdf")
