import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Graphik1')
print('Steigung','Y-Achsenabschnitt')
x, y = np.loadtxt('A1L1x75mmF6000-9000S10.dat', unpack=True,delimiter=' ')
w=x
b= 2*np.pi*10000
a=2*np.pi*20
#def f(x,a,b):
#    return (2*b)/((b**2-w**2)**2+(2*a*w))
#Werte, Fehler = curve_fit(f, w, y)
#print(Werte)
#print(np.diag(Fehler**2)**(1/4))
#
#
#w_new = np.linspace(w[0], w[-1], 500)

plt.figure(1)
plt.plot((2*b)/((b**2-w**2)**2+(2*a*w)))

##plt.plot(w_new,f(w_new,*Werte),'-', label='Fitfunktion $\Delta f \sim 1/d$')
#plt.plot(w,y,'x')
#plt.xlabel('Länge d / mm')
#plt.ylabel('Frequenz $\Delta$ f')
#plt.grid()
#plt.legend()
#
plt.savefig('vergleich.pdf')
#print ('Fertig')
