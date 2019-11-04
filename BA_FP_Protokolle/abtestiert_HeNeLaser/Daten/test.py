import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Graphik1')
print('Steigung','Y-Achsenabschnitt')
#x, y = np.loadtxt('erstemode.txt', unpack=True,delimiter=',')

def f(x,y):
    return x




#def f(x,phi,w,l,b):
#    return sympy.cos(l*phi)(4*2*np.pi)/(x*w)/((1+(2*z/x)**2)**((1+l)/2))
#popt, pcov = curve_fit(f, x, y)
#print(popt)
#print(np.diag(pcov))
#x_new = np.linspace(x[0], x[-1], 500)



plt.figure(1)
plt.plot(f)
#plt.plot(x,y,'x')
#plt.plot(x_new,f(x_new,*popt),'-', label='Lineare Regression')
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')
plt.grid()
plt.legend()




plt.savefig('erstemode.pdf')
print ('Fertig')
