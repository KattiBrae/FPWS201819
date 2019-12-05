import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
import uncertainties
import scipy.constants as const
import functions as func

from matplotlib.pyplot import (Axes as ax)
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

A_0 = unp.uarray(330,1)*10**3 #becquerel
tau = unp.uarray(432.6,0.6)*365*24*60*60 #s
t = unp.uarray(7.897,0.013)*10**8 #s

A = func.activity(A_0, tau, t)
A2 = 15.13
print("A_theo = ", A)
print("A_exp = ", A2)
#c) Thickness 

def linear(x, a, b):
    return a*x+b

x_plot = np.linspace(90, 550, 1000)

p_with, U_with = np.genfromtxt('../content/data/tables/Txt/creichweite.txt',unpack=True)
p_without, U_without = np.genfromtxt('../content/data/tables/Txt/reichweite_ohnefolie2.txt',unpack=True)

params_w, covariance_matrix_w = curve_fit(linear, p_with[2:], U_with[2:])
params_wo, covariance_matrix_wo = curve_fit(linear, p_without[2:], U_without[2:])

plt.plot(p_with, U_with, 'kx', label=r"Wertepaare mit Folie")
plt.plot(p_without, U_without, 'bx', label=r"Wertepaare ohne Folie")
plt.plot(x_plot, linear(x_plot, *params_w), "-", label = r"Ausgleichsgerade mit Folie")
plt.plot(x_plot, linear(x_plot, *params_wo), "-", label = r"Ausgleichsgerade ohne Folie")

plt.xlabel('p / mbar')
plt.ylabel('U / V')
plt.legend(loc='best')
plt.savefig('../content/data/plots/gerade.pdf')
E_a = 5.4865 *10**6 * const.e
kappa, b_wo = func.avg_loss(E_a, params_wo, covariance_matrix_wo)
b_w = func.avg_loss(E_a, params_w, covariance_matrix_w)[1]

dE= kappa*(b_wo-b_w)
print("dE = ", dE/(10**6 * const.e))
E_a = 5.486 *10**6 * const.e
m_a = const.value(u"alpha particle mass")
print(m_a)
m_e = const.value(u"electron mass")
z = 2
Z = 79
I = 10 * Z * const.e
n = 19.32/197*const.N_A*1000*1000
v2 = E_a/m_a*(1+b_w/b_wo)
print('v2', unp.sqrt(v2))
d = dE/unp.log(2*m_e*v2/I)*m_e*v2*4*np.pi*const.epsilon_0**2/(const.e**4*z**2*Z*n)
print('d:', d)

#Diff WQ
dO = np.pi/4/(4.1)**2
angle, hits, time  = np.genfromtxt('../content/data/tables/Txt/dstreuwinkel.txt',unpack=True, skip_header = 3)
hits = unp.uarray(hits, np.sqrt(hits))
theta=angle *np.pi/180

dsdO_e = (hits/time)/(A2*dO*n*2*10**(-6) )
dsdO_t=1/(4*np.pi*const.epsilon_0)**2*((Z*z*const.e**2)/(4*E_a))**2*1/(np.sin(theta*0.5))**4  

func.diffWQ_table(angle, hits, time, dsdO_e, dsdO_t)

plt.cla()
plt.clf()
#theta = np.flip(theta)
name = 'Rutherford'
#plt.ylim(-5, 500)
plt.plot(theta, dsdO_t*10**24, 'mx', label='Wertepaare Theorie')
plt.plot(theta, noms(dsdO_e*10**24), 'bx', label = 'Wertepaare Experimentell')
plt.errorbar(theta, noms(dsdO_e*10**24), yerr=10*stds(dsdO_e*10**24), fmt="none", capsize=3, capthick=1, ms=9, color="red", label = 'Unsicherheit mal 10')
plt.yscale("log")
plt.legend(loc='best')
#func.Plot(x=theta,y=dsdO_e*10**24,xname=r'$\theta$',yname=r'Test',markername='Wertepaare Experiment',linear=False,save=False,Plot=True)
#ST.set_ylim(0, 100)
plt.savefig('../content/data/plots/'+name+'.pdf')

plt.cla()
plt.clf()
name = 'Rutherford2'
plt.plot(theta, dsdO_t*10**24, 'mx', label='Wertepaare Theorie')
#Plot(x=theta[2:],y=dsdO[2:]*10**24,xname=r'$\theta$',yname=r'$\frac{\mathrm{d}\sigma}{\mathrm{d}\Omega}/10^{-24}\s{\meter^2}$',markername='Wertepaare Experiment',linear=False,save=False,Plot=plot)
plt.savefig('../content/data/plots/'+name+'.pdf')


#Mehrfachstreuung
mu, Hits, time = np.genfromtxt('../content/data/tables/Txt/efoliendicke.txt',unpack=True, skip_header = 2)
N=unp.uarray(Hits,np.sqrt(Hits))
I=N/time

dsdO2m=I[0]/(A2*n*2*10**(-6)*dO)
dsdO4m=I[1]/(A2*n*4*10**(-6)*dO)
print("dsd02m : ", dsdO2m)
print("dsd04m : ", dsdO4m)