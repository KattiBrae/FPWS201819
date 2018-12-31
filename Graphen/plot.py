
import numpy as np
import sympy as s
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show
#Bildgröße(Breite,Höhe)
plt.rcParams['figure.figsize'] = (10, 8)
#Schriftgröße
plt.rcParams['font.size'] = 16
#Liniendicke
plt.rcParams['lines.linewidth'] = 2

print('Graphik1')
x, y = np.loadtxt('tab1.txt', unpack=True, delimiter='&')
# Wir importieren die Tabelle als x und y werte
def f(x,a,b):
    return a*x+b
Werte, Fehler = curve_fit(f, x, y)
print(Werte)#a.b. a ist hier die Steigung und B der Y-Achsen Abschnitt.
print(Fehler)
print(np.diag((Fehler**2)**(1/4)))#Fehler a.b.
# Es handelt sich bei dem Fehler um das sigam^2 daher muss die Wurzel gezogen werden.
# das np.diag reduziert die Fehlermatrix auf die für uns wichtigen Einträge.
x_new = np.linspace(x[0], x[-1], 500)

#Fehlerbalken
T=np.sqrt(y)

plt.errorbar(x, y, yerr=T, fmt="none", capsize=5, capthick=2, ms=9, markerfacecolor="red")


#c, v = np.loadtxt('tab2.txt', unpack=True,delimiter=',')
#def f(c,n,m):
#    return n*c+m
#popt, pcov = curve_fit(f, c, v)
#print(popt)
#print(np.diag(pcov**(1/2)))
#c_new = np.linspace(c[0], c[1], 500)


plt.figure(1)
plt.plot(x,y,'x', label='Messwerte')
#plt.plot(c,v,'x')
plt.plot(x_new,f(x_new,*Werte),'-', label='Regression')
#plt.plot(c_new,f(c_new,*popt),'-', label='Regression')
plt.xlabel('r /m')
plt.ylabel('d /m')
plt.grid()
plt.legend()
#plt.show()


plt.savefig('Graphik1.pdf')
print ('Fertig')
