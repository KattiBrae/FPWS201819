import numpy as np
import sympy
import math
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Graphik1')
print('Steigung','Y-Achsenabschnitt')
x, y = np.loadtxt('grundmode.txt', unpack=True,delimiter=',')


def f(x,a,b,c,d):
#    return a*x+b
    return a*np.exp(b*(x-c)**2)+d
popt, pcov = curve_fit(f, x, y, p0=[1.7,0.001,2,0.017])
print(popt)
print(np.diag(pcov))

x_new = np.linspace(x[0], x[-1], 500)



plt.figure(1)
plt.plot(x,y,'x')
plt.plot(x_new,f(x_new,*popt),'-', label='Regression' r'$\propto e^{x^2}$')
plt.xlabel('x/mm')
plt.ylabel('I/$\mu$ A')
plt.grid()
plt.legend()




plt.savefig('grundmode.pdf')
print ('Fertig')
