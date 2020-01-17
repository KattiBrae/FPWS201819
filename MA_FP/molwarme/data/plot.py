# coding=utf-8
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat, unumpy
from uncertainties.unumpy import nominal_values as noms
from uncertainties.unumpy import std_devs as err
import scipy.integrate as int
import scipy.constants as con
from scipy.constants import physical_constants as pcon

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

mcu = 342
Mcu = 63.546
k = 140
V = 7.092*10**(-6)
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
cv = cp - (9 * (f(T2, m, b)*10**(-5))**2 * k * V * T2)

cp1 = noms(cp)
cv1 = noms(cv)

plt.errorbar(noms(T1),noms(cp), xerr=err(T1), yerr=err(cp),fmt='bx',label='Werte für $C_{\mathrm{P}}$')
plt.errorbar(noms(T1),noms(cv), xerr=err(T1), yerr=err(cv),fmt='mx',label='Werte für $C_{\mathrm{V}}$')
plt.legend(loc='best')
plt.tight_layout()
plt.grid()
plt.xlabel(r"$T$ in $\mathrm{K}$")
plt.ylabel(r"$C_{\mathrm{V}}$ in $\mathrm{JK}^{-1}\mathrm{mol}^{-1}$")
plt.tight_layout()
plt.savefig("plots/plot_Cv.pdf")
plt.close()