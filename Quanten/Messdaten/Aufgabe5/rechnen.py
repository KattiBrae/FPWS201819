import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

x, y = np.loadtxt('tabelle.txt', unpack=True,delimiter=' ')

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

#h = 6.62607004e-34
#m = 9.10938356*10**(-31)
#E = (h**2*k**2)/(2*m)
#print(E)
plt.figure(3)
plt.plot(k_new,f(k_new,*Werte),'-')#, label='Fitfunktion $\Delta f \sim 1/d$')
#plt.plot(k,E)
plt.plot(k,y,'x', label="Messwerte")
plt.ylabel(r'Frequenz / Hz')
plt.xlabel(r'k')
plt.grid()
plt.legend()

plt.savefig('bla.pdf')
print ('Fertig')

#ergebnisse für k
"""
[   1.09820298    3.84371042    6.7722517    13.17843574   19.58461978   25.99080382   32.21395403   38.07103659   43.37901765

   60.9502653   63.51273892   68.45465232   73.94566721   79.61971594   84.927697   89.8696104    93.34725317

   121.35142912  123.18176741  126.65941018  131.05222209  135.81110166  140.20391358  144.23065783

   180.83742378  182.66776208  185.59630335  189.44001378  193.64979186  197.67653611  201.15417888]

"""
