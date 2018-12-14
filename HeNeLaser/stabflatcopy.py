
import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Zweite Messung')
print('Steigung','Y-Achsenabschnitt')
x, y = np.loadtxt('stabflat1.txt', unpack=True,delimiter=',')
y=-y
x=x*1e-02

def f(x,a,b):
    return a*x+b
popt, pcov = curve_fit(f, x, y)
print(popt)
print(np.sqrt(np.diag(pcov)))


x_new = np.linspace(x[0], x[-1], 5000)

#V, u = np.loadtxt('tabkalibrierung.txt', unpack=True,delimiter=',')

#T=np.sqrt(v)
#plt.errorbar(u, v, yerr=T, fmt="none", capsize=5, capthick=2, ms=9, markerfacecolor="red")

print('Erste Messung')
p, q = np.loadtxt('stabflat2.txt', unpack=True,delimiter=',')
q=-q
p=p*1e-02

def g(p,c,d):
    return c*p+d
qopt, qcov = curve_fit(g, p, q)
print(qopt)
print(np.sqrt(np.diag(qcov)))


p_new = np.linspace(p[0], p[-1], 5000)


plt.figure(1)
plt.plot(x,y,'x')
plt.plot(p,q,'x')
plt.plot(x_new,f(x_new,*popt),'-', label='Lineare Regression')
plt.plot(p_new,g(p_new,*qopt),'-', label='Lineare Regression')


plt.xlabel('Channel')
plt.ylabel(r'$\Delta t/ 10^{-6} s$')
plt.grid()
plt.legend()

#a=2.67613625 +- 0.604222979537
#b=1054.98042467 +-  162.497735677

plt.savefig('figkalibrierung.pdf')
print ('Fertig')
