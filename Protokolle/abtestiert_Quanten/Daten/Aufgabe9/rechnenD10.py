"""
D10
Bandlücken
Ende  Anfang
E3
"""
#x=10,10,10
y1=(3290-1750)
y2=(6710-4300)
y3=(10080-7400)
#print(y1,y2,y3)
"""
E4
"""
#c= 13, 13, 13
y4=(3330-1760)
y5=(6730-4310)
y6=(10100-7390)
"""
E6
"""
#v=16, 16, 16
y7=(3350-1780)
y8=(6740-4310)
y9=(10110-7390)

x=3,4,6

import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, scatter, show
import numpy as np
import sympy
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show
#x, y = np.loadtxt(Tabelle, unpack=True,delimiter=' ')

s = y1, y4, y7
plot(x, s, "x", label="Messwerte")
def f(x,a,b):
    return a*x+b
Werte, Fehler = curve_fit(f, x, s)
print(Werte)
print(np.diag(Fehler**2)**(1/4))
x_new = np.linspace(x[0], x[-1], 500)
plt.plot(x_new,f(x_new,*Werte),'-')

d = y2, y5, y8
plot(x, d, "x")
def f(x,a,b):
    return a*x+b
Werte, Fehler = curve_fit(f, x, d)
print(Werte)
print(np.diag(Fehler**2)**(1/4))
x_new = np.linspace(x[0], x[-1], 500)
plt.plot(x_new,f(x_new,*Werte),'-')

e = y3, y6, y9
plot(x, e, "x")
def f(x,a,b):
    return a*x+b
Werte, Fehler = curve_fit(f, x, e)
print(Werte)
print(np.diag(Fehler**2)**(1/4))
x_new = np.linspace(x[0], x[-1], 500)
plt.plot(x_new,f(x_new,*Werte),'-')#, label='Ausgleichsgerade')
plt.grid()
plt.legend()
plt.xlabel('Anzahl Einheitszellen')
plt.ylabel(r'Breite der Bandlücke $\Delta$ f')
plt.savefig("BandlückenD10.pdf")
print('Fertig')
