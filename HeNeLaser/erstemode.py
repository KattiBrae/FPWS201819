import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Graphik1')
print('Steigung','Y-Achsenabschnitt')
R, y = np.loadtxt('erstemode.txt', unpack=True,delimiter=',')

def f(R,y,a,omega):
    return (a*8*R**2)/omega**2*np.exp((-2*R**2)/omega**2)


#def f(y,j,z,m):
#    return np.cos(l*j)*(2*(2*np.pi/(R*m)))**2/(1+(2*z/R)**2)**((1+l)/2)*1*np.exp(-(2*np.pi/(R*m))**2/(1+(2*z/R)**2))*np.exp(    -1*(   (1+2*z/R)*np.pi*R/m + (2*np.pi/(R*m))**2*(2*z/R)/(1+(2*z/R)**2)    - (l+2*p+1)(np.pi/2-np.arctan((1-2*z/R)/(1+2*z/R)  )   )   ))
#rho=(2*np.pi/(R*m))
#Z=2*z/R

popt, pcov = curve_fit(f,R,y,p0=[2,0.001])
print(popt)
print(np.diag(pcov))
R_new = np.linspace(R[0], R[-1], 500)


#Laguerre(01)=1
#Laguerre(11)=-g+2
#g=(2*rho)**2/(1+Z**2)

plt.figure(1)
plt.plot(R,y,'x')
plt.plot(R_new,f(R_new,*popt),'-', label='WHAAAT')
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')
plt.grid()
plt.legend()




plt.savefig('erstemode.pdf')
print ('Fertig')
