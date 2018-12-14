import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('2. Messung')
print('Steigung','Y-Achsenabschnitt')
x, y = np.loadtxt('stabflat1.txt', unpack=True,delimiter=',')
y=-y
x=x*1e-02

def f(x,a,b):
    return a*x+b
popt, pcov = curve_fit(f, x, y)
print(popt)
print(np.sqrt(np.diag(pcov)))


print('1. Messung')

m, n = np.loadtxt('stabflat2.txt', unpack=True,delimiter=',')
n=-n
m=m*1e-02
def g(m,c,d):
    return c*m+d
qopt, qcov = curve_fit(g, m, n)
print(qopt)
print(np.sqrt(np.diag(qcov)))


x_new = np.linspace(x[0], m[-1], 500)
m_new = np.linspace(x[0], m[-1], 500)


plt.figure(1)
plt.plot(x,y,'x', label='Zweite Messung')
plt.plot(m,n,'x', label='Erste Messung')
plt.plot(x_new,f(x_new,*popt),'-', label='Lineare Regression 2. Messung')
plt.plot(m_new,g(m_new,*qopt),'-', label='Lineare Regression 1. Messung')
plt.xlabel('x/m')
plt.ylabel('I/$10^{-6}$A')
plt.grid()
plt.legend()




plt.savefig('stabflat.pdf')
print ('Fertig')
