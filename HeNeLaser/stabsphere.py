
import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Graphik1')
print('Steigung','Y-Achsenabschnitt')
x, y = np.loadtxt('stabsphere.txt', unpack=True,delimiter=',')
y=-y
r1=1.4
r2=1.4
def f(x,a,b,c,e):
#    return 1/(r1*r2)*a*(r2-c*(x+b))*(r1-d*(x+b))+e
    return a*(x+b)**2/(r1*r2)+c*(x+b)/(r1*r2)+e/(r1*r2)
popt, pcov = curve_fit(f, x, y)
print(popt)
print(np.sqrt(np.diag(pcov)))

x_new = np.linspace(x[0], x[-1], 500)



plt.figure(1)
plt.plot(x,y,'x')
plt.plot(x_new,f(x_new,*popt),'-', label='Regression $\propto L^2$')
plt.xlabel('L/m')
plt.ylabel('I/$10^{-3}$A')
plt.grid()
plt.legend()




plt.savefig('stabsphere.pdf')
print ('Fertig')
