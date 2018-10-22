
import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show
plt.rcParams['figure.figsize'] = (20, 10)
plt.rcParams['font.size'] = 16
plt.rcParams['lines.linewidth'] = 2

print('Myonen')
y, x = np.loadtxt('myonen.txt', unpack=True,delimiter=',')

#x, y = np.loadtxt('tab2.txt', unpack=True,delimiter=',')
T=np.sqrt(y)

plt.errorbar(x, y, yerr=T, fmt="none", capsize=5, capthick=2, ms=9, markerfacecolor="red")
plt.plot(x, y, "x", label="Messwerte")

def f(x,a,b,c):
    return a*np.exp(-x*b)+c
popt, pcov = curve_fit(f, x, y)

#print('#a','b#')
print(popt)
#print('#Fehler#')
print(np.sqrt(np.diag(pcov)))

x_new = np.linspace(x[0], x[-1], 5000)



plt.figure(1)
#plt.plot(x,y,'x')
plt.plot(x_new,f(x_new,*popt),'-', label='Ausgleichsrechnung ' r'$\propto e^{t}$')
plt.xlabel(r'Lebensdauer $t/ 10^{-9} s$')
plt.ylabel('Häufigkeit')
plt.grid()
plt.legend()
#plt.show()

#a=2.67613625 +- 0.604222979537
#b=1054.98042467 +-  162.497735677

plt.savefig('figmyonen.pdf')
print ('Fertig')
