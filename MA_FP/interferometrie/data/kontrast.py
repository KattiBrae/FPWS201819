def Kontrast(phi, delta, a):
    return a*np.abs(np.sin(2*np.radians(phi)-delta))

def Brechung(M,lambda_vac,L):
	return (M*lambda_vac)/L+1

if __name__=="__main__":
    import pandas as pd
    import numpy as np
    import sympy
    import matplotlib as mpl
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    from matplotlib import transforms
    from matplotlib import rc
    from scipy.optimize import curve_fit
    from pylab import figure, axes, pie, title, show
    from numpy import NaN, Inf, arange, isscalar, asarray, array
    from scipy.stats import linregress
    import sys
    import scipy.signal as sig
    from scipy.stats import norm
    import scipy.constants as const
    import uncertainties
    import uncertainties.unumpy as unp
    from uncertainties import ufloat
    from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
    from math import exp, log, sin, atan
    import uncertainties.unumpy as unp
    


    plt.rcParams['figure.figsize'] = (10, 7)
    plt.rcParams['font.size'] = 16
    plt.rcParams['lines.linewidth'] = 2

    x, a, b = np.genfromtxt('kontrast.txt', unpack=True, skip_header = 2)
    y = []
    y = (a-b)/(a+b)

    x_plot = np.linspace(0, 180, 10000)
    params, covariance_matrix = curve_fit(Kontrast, x, y)


    plt.plot(x, y, 'x', color='C0', markersize=8, markeredgewidth=2, label='Daten')
    plt.plot(x_plot, Kontrast(x_plot, *params), color='C1', label='Fit')
    plt.legend(fancybox=True, ncol=1)
    plt.xlabel('$\phi$ in Grad', labelpad=2)
    plt.ylabel('Kontrast', labelpad=8)

    plt.grid(alpha=0.3)

    plt.savefig('kontrast.pdf')

    uncertainties = np.sqrt(np.diag(covariance_matrix))
    A = unp.uarray(params[0], uncertainties[0])
    delta = unp.uarray(params[1], uncertainties[1])

    print('A = ', A)
    print('Delta = ', delta)
    print('--- done ---')

#-----Brechungsindex-----#
#----------Glas----------#
M = np.array([39,36,37,36,37,36,37,38,38,41])
Lambda = 632.99e-9
Theta = np.radians(11)
Theta_0 = np.radians(10)
T = 1e-3

n = (1 - Lambda * M / (2 * T * Theta_0 * Theta))**-1
n_mean = ufloat(np.mean(n), np.std(n)/ np.sqrt(len(n)))
#np.savetxt("data/Brechungsindex_Glas.txt", np.array([M, n]).T, header = "#Nulldurchgänge Brechungsindex")

print('n_Glas:',n_mean)
print('--- done ---')
#------Luft------#
lambdavac = 632.99 *10**-6
L = unp.uarray(0.1,0.0001) #in mm
T = 0.001 # in m

p, m1, m2, m3 = np.genfromtxt('Druck.txt',unpack=True, skip_header = 2)

n_m1 = Brechung(m1, lambdavac, L)
for i in range(len(n_m1)):
    print('n_m1 = ',n_m1[i])
n_m1 = sum(n_m1)/len(n_m1)
print('n_m1_med = ',n_m1)
print('\n')


n_m2 = Brechung(m2, lambdavac, L)
for i in range(len(n_m2)):
    print('n_m2 = ',n_m2[i])
n_m2 = sum(n_m2)/len(n_m2)
print('n_m2_med = ',n_m2)
print('\n')


n_m3 = Brechung(m3, lambdavac, L)
for i in range(len(n_m3)):
    print('n_m3 = ',n_m3[i])
n_m3 = sum(n_m3)/len(n_m3)
print('n_m3_med = ',n_m3)
print('\n')

n_ges= (n_m1+n_m2+n_m3)/3
print('n_ges = ', n_ges)
print('--- done ---')