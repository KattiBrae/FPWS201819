
import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Fe')
print('Steigung','Y-Achsenabschnitt')
x, y = np.loadtxt('fe1.txt', unpack=True,delimiter=',')
T=np.sqrt(y)
plt.plot(x, y, "kx", label="Messwerte")
plt.errorbar(x, y, yerr=T, fmt="none", capsize=3, capthick=1, ms=9, markerfacecolor="red")


def f(x,a,b):
    return a*x+b
popt, pcov = curve_fit(f, x, y)
print(popt)
print(pcov)

x_new = np.linspace(x[0], x[-1], 500)

# 2 pi re (0.3990002807 + 0.49349505 - 0.37903182)


plt.figure(1)
plt.plot(x,y,'x')
plt.plot(x_new,f(x_new,*popt),'-', label='Lineare Regression Eisen')
plt.xlabel('d/m')
plt.ylabel('$\ln(N/t-N_{U1}/t_{U1})$')
plt.grid()
plt.legend()




plt.savefig('fe.pdf')
print ('Fertig')
