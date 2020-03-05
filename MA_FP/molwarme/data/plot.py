# coding=utf-8
#!/usr/bin/env python3
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat, unumpy
import uncertainties.unumpy as unp
from uncertainties.unumpy import nominal_values as noms
from uncertainties.unumpy import std_devs as err
import scipy.integrate as int
import scipy.constants as con
from scipy.constants import physical_constants as pcon

def print_arr(func, name):
    for i in range(len(func)):
        print(name, ' = ', func[i])

T, alpha = np.genfromtxt('data_alpha.txt', unpack = True, skip_header = 2)

def f(x, m, b):
    return m*1/x+b

params, cov = curve_fit(f, T, alpha)

m = params[0]
b = params[1]

dm = np.sqrt(cov[0][0])
db = np.sqrt(cov[1][1])

x = np.linspace(70, 300, 1000)

plt.plot(1/T, alpha, 'rx', label='Messwerte')
plt.plot(1/x, f(x, m, b), 'k-', label='Regressionsgerade')
plt.grid()
plt.xlabel(r"$T^{-1}$ in $\mathrm{K}^{-1}$")
plt.ylabel(r"$\alpha\cdot 10^{-6}$ in $\mathrm{K}^{-1}$")
plt.legend(loc='best')
plt.tight_layout()
plt.savefig("plots/plot_alpha.pdf")
plt.close()

m = ufloat(m, dm)
b = ufloat(b, db)

print('m = ', m)
print('b = ', b)

mcu = 0.342 #in kg
Mcu = 0.063546 #in kg/mol
rho = 8920 #in kg/m³
V0 = Mcu/rho # in m³/mol
K = 1.278 * 10**11 #in N/m²
vl = 4700 # in m/s
vtr = 2260 #in m/s

temp, R1, R2, U, I, I2 = np.genfromtxt('data.txt', unpack = True, skip_header = 2)
t = unumpy.uarray(temp, 1)
U = unumpy.uarray(U, 0.01)
I = unumpy.uarray(I, 0.1)
R1 = unumpy.uarray(R1, 0.1)
R2 = unumpy.uarray(R2, 0.1)


def t(R):
    return 0.00134*R**2 + 2.296*R + 30.13

T1 = t(R1)
T2 = t(R2)

def delta(temp):
    delta = [None] * len(temp)
    for i in range(len(temp)):
        if i == 0:
            delta[i] = temp[i]
        else:
            delta[i] = temp[i] - temp[i-1]
    return delta

dt = delta(temp)
dT = delta(T1)

cp= (Mcu/mcu) * (U * I/1000.0 * dt)/dT
cv = cp - (9 * (f(T2, m, b)*10**(-6))**2 * K * V0 * T2)

#print_arr(cp, 'C_p')
cp1 = noms(cp)
cv1 = noms(cv)

plt.errorbar(noms(T1),noms(cp), xerr=err(T1), yerr=err(cp),fmt='bx', linewidth=1, label='Werte für $C_{\mathrm{P}}$')
plt.errorbar(noms(T1),noms(cv), xerr=err(T1), yerr=err(cv),fmt='mx', linewidth=1 , label='Werte für $C_{\mathrm{V}}$')
plt.legend(loc='best')
plt.tight_layout()
plt.grid()
#plt.xlim(70, 100)
plt.xlabel(r"$T$ in $\mathrm{K}$")
plt.ylabel(r"$C_{\mathrm{V}}$ in $\mathrm{JK}^{-1}\mathrm{mol}^{-1}$")
plt.tight_layout()
plt.savefig("plots/plot_Cv.pdf")
plt.close()

TT = (T2[1:])
Cvv = (cv[1:])
Td = unp.uarray(np.zeros(20),0)
Cvd = unp.uarray(np.zeros(20),0)
for i in range(len(TT)):
	if TT[i]<170:
		Td[i] = TT[i]
		Cvd[i] = Cvv[i]		
#Td und Cvd sind die in Frage kommenden Werte, deb die dazugehörigen Debye Funktionswerte die ich per Hand rausgesucht habe. con.R ist die allgemeine Gaskonstante
#print_arr(Td, "Temp")
deb = np.array([3.5,3.2,2.9,2.7,2.9,2.7,2.7,2.7,2.7,2.7,3.0,2.7,2.5,3.0,2.5,2.5,2.3,2.3,2.3,2.3])

#theta_D ist thD

thD = Td * deb
print("\n")
print_arr(Cvd, "CV")
print("\n")
print_arr(thD, "thD")

MthD = ufloat(np.mean(noms(thD)),np.std(noms(thD))/np.sqrt(len(noms(thD))))
print(MthD)