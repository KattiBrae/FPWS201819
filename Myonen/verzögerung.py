
import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Graphik1')
print('Steigung','Y-Achsenabschnitt')
x, y = np.loadtxt('Verzögerungfit.txt', unpack=True,delimiter=',')

def f(x,a,b,c):
    return a*(x+b)**4+c
popt, pcov = curve_fit(f, x, y)
print(popt)
print(np.sqrt(np.diag(pcov)))

x_new = np.linspace(x[0], x[-1], 500)

u, v = np.loadtxt('Verzögerung.txt', unpack=True,delimiter=',')

u_new = np.linspace(u[0], u[-1], 500)

T=np.sqrt(v)

plt.errorbar(u, v, yerr=T, fmt="none", capsize=5, capthick=2, ms=9, markerfacecolor="red")

#s=0.02234091
#r=0.03080493+0*s
#plt.plot(s,label=r'Halbwertsbreite')


plt.figure(1)
plt.plot(x,y,'x')
plt.plot(u,v,'x')
plt.plot(x_new,f(x_new,*popt),'-', label='Lineare Regression')
plt.xlabel('Verzögerungszeit ' r'$T_{VZ}/ 10^{-9} s$ durch die Kabel')
plt.ylabel('Zählrate ' r'N/$\frac{1}{s}$ mit Messzeit $t=10s$')
plt.grid()
plt.legend()




plt.savefig('figverzögerung.pdf')
print ('Fertig')
