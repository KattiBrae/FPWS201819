"""
L=8
D=16
"""
v=8,8,8
y7=-(2490-3170)
y8=-(5170-6520)
y9=-(8080-9820)
"""
L=10
D =16
Anfang  Ende
"""
x=10,10,10
y1=-(2480-3230)
y2=-(5170-6550)
y3=-(8080-9830)
"""
L=12
D=16
"""
c=12,12,12
y4=-(2470-3260)
y5=-(5170-6580)
y6=-(8020-9840)

x=8,10,12




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


"""


import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, scatter, show
import numpy as np
#x, y = np.loadtxt(Tabelle, unpack=True,delimiter=' ')
s = y1, y2, y3
plot(x, s, "x", label="Messwerte")
d = y4, y5, y6
plot(c, d, "x")
f = y7, y8, y9
plot(v, f, "x")
plt.grid()
plt.legend()
plt.xlabel('Rohrlänge')
plt.ylabel(r'Breiter der Bandlücke $\Delta$ f')
plt.savefig("Bandlücke.pdf")
print('Fertig')
"""
