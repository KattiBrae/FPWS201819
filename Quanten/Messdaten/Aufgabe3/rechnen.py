"""
Bandlücken
Anfang  Ende
D10
"""
#x=10,10,10
y1=-(1840-3360)
y2=-(4300-6740)
y3=-(7400-10100)
#print(y1,y2,y3)
"""
D13
"""
#c= 13, 13, 13
y4=-(2150-3280)
y5=-(4670-6660)
y6=-(7660-9980)
"""
D16
"""
#v=16, 16, 16
y7=-(2470-3260)
y8=-(5170-6570)
y9=-(8020-9840)

x=10,13,16

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
plt.xlabel('Blendenbreit')
plt.ylabel(r'Breiter der Bandlücke $\Delta$ f')
plt.savefig("Bandlücken.pdf")
print('Fertig')
