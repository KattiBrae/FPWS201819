import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Graphik1')
print('Steigung','Y-Achsenabschnitt')
R, y = np.loadtxt('erstemode.txt', unpack=True,delimiter=',')

def f(R,a,b,c,d,o):
    return (a*8*(R-b)**2)/o**2*np.exp((-2*d*(R-b)**2)/o**2)+c


#def f(y,j,z,m):
#    return np.cos(l*j)*(2*(2*np.pi/(R*m)))**2/(1+(2*z/R)**2)**((1+l)/2)*1*np.exp(-(2*np.pi/(R*m))**2/(1+(2*z/R)**2))*np.exp(    -1*(   (1+2*z/R)*np.pi*R/m + (2*np.pi/(R*m))**2*(2*z/R)/(1+(2*z/R)**2)    - (l+2*p+1)(np.pi/2-np.arctan((1-2*z/R)/(1+2*z/R)  )   )   ))
#rho=(2*np.pi/(R*m))
#Z=2*z/R

popt, pcov = curve_fit(f,R,y, p0=[25,0.003,10,1000,0.5])
print(popt)
print(np.diag(pcov))
R_new = np.linspace(R[0], R[-1], 5000)


#Laguerre(01)=1
#Laguerre(11)=-g+2
#g=(2*rho)**2/(1+Z**2)

plt.figure(1)
plt.plot(R,y,'x')
plt.plot(R_new,f(R_new,*popt),'-', label=r'Fit $\propto x^2 \exp{(-x^2)}$')
plt.xlabel('x/m')
plt.ylabel('I/nA')
plt.grid()
plt.legend()




plt.savefig('erstemode.pdf')
print ('Fertig')
