import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show
from numpy import NaN, Inf, arange, isscalar, asarray, array
import sys

x1=-(2310-3270)
x2=-(4940-6610)
x3=-(7870-9910)
y=(x1,x2,x3)
x=(1,2,3)

def f(x,a,b):
    return(a*x+b)
Wert, Fehler = curve_fit(f,x,y)
print(Wert)
print(np.sqrt(np.diag(Fehler)))
x_new = np.linspace(x[0], x[-1], 50)

plt.plot(x_new, f(x_new,*Wert))
plt.plot(x,y,"x",color="red",label="Messwerte")
plt.grid()
plt.legend()
plt.xlabel("Nummer")
plt.ylabel(r"Bandlücken $\Delta$ f")
plt.savefig("test.pdf")
