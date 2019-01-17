
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
plt.plot(k_new,f(k_new,*Werte),'-', color="red")#, label='Fitfunktion $\Delta f \sim 1/d$')
print("######")
x1=1.09820298 ,201.15417888
y1=2370,2370
y2=3330,3330
y3=5100,5100
y4=6630,6630
y5=8040,8040
y6=9880,9880
#y7=11120,11120

def h(x1,a,b):
    return a*x1+b
Werte, Fehler = curve_fit(h, x1, y1)
print(Werte)
print(np.diag(Fehler**2)**(1/4))
x1_new = np.linspace(x1[0], x1[-1], 50, endpoint=True)
plt.plot(x1_new,h(x1_new,*Werte),'-',linewidth=1, linestyle="--", color='blue')

def j(x1,a,b):
    return a*x1+b
Werte, Fehler = curve_fit(j, x1, y2)
print(Werte)
print(np.diag(Fehler**2)**(1/4))
x1_new = np.linspace(x1[0], x1[-1], 500, endpoint=True)
plt.plot(x1_new,j(x1_new,*Werte),'-',linewidth=1, linestyle="--", color='blue')

def g(x1,a,b):
    return a*x1+b
Werte, Fehler = curve_fit(g, x1, y2)
Werte, Fehler = curve_fit(g, x1, y3)
print(Werte)
print(np.diag(Fehler**2)**(1/4))
x1_new = np.linspace(x1[0], x1[-1], 500)
plt.plot(x1_new,g(x1_new,*Werte),'-',linewidth=1, linestyle="--", color='blue')

Werte, Fehler = curve_fit(g, x1, y4)
print(Werte)
print(np.diag(Fehler**2)**(1/4))
x1_new = np.linspace(x1[0], x1[-1], 500)
plt.plot(x1_new,g(x1_new,*Werte),'-',linewidth=1, linestyle="--", color='blue')

Werte, Fehler = curve_fit(g, x1, y5)
print(Werte)
print(np.diag(Fehler**2)**(1/4))
x1_new = np.linspace(x1[0], x1[-1], 500)
plt.plot(x1_new,g(x1_new,*Werte),'-',linewidth=1, linestyle="--", color='blue')

Werte, Fehler = curve_fit(g, x1, y6)
print(Werte)
print(np.diag(Fehler**2)**(1/4))
x1_new = np.linspace(x1[0], x1[-1], 500)
plt.plot(x1_new,g(x1_new,*Werte),'-',linewidth=1, linestyle="--", color='blue')

#Werte, Fehler = curve_fit(g, x1, y7)
#print(Werte)
#print(np.diag(Fehler**2)**(1/4))
#x1_new = np.linspace(x1[0], x1[-1], 500)
#plt.plot(x1_new,g(x1_new,*Werte),'-',linewidth=1.5, linestyle="--", color='blue')

#plt.plot(k,E)
print(h)
plt.fill_between(x1, y1, y2, color='blue', alpha=.1)
plt.fill_between(x1, y3, y4, color='blue', alpha=.1)
plt.fill_between(x1, y5, y6, color='blue', alpha=.1)
plt.plot(k,y,'x', label="Messwerte", color="red")
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

"""
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
