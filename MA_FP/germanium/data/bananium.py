import numpy as np
import sympy
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib import transforms
from matplotlib import rc
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show
from numpy import NaN, Inf, arange, isscalar, asarray, array
import sys

plt.rcParams['figure.figsize'] = (15, 10)
plt.rcParams['font.size'] = 16
plt.rcParams['lines.linewidth'] = 2


counts = np.loadtxt('bananium.txt', unpack=True,delimiter=' ')
channel = np.arange(0, len(counts), 1 )

error=np.sqrt(counts)
plt.errorbar(channel, counts, yerr=error, fmt="none", capsize=5, capthick=1, ms=5, markerfacecolor='C2', label='Unsicherheit')


#def f(channel,a,b,c):
#    return a*np.exp(-b*channel)+c
#params, var = curve_fit(f, channel, counts)
#fehler = np.sqrt(np.diag(var))
#print('parameter, fehler')
#print(params, fehler)
#x_new = np.linspace(channel[0], channel[-1], 5000)
#plt.plot(x_new,f(x_new,*popt),'-', label='Ausgleichsrechnung ' r'$\propto e^{-\lambda t}$')


plt.plot(channel, counts, 'x', markersize='6', color='red', label='Daten')

plt.legend(fontsize=11, fancybox=True, loc='upper right', ncol=1)                                  # schiebt die Legende in die obere linke Ecke
plt.xlabel('Channel', labelpad=2)                                                            # Label x-Achse
plt.ylabel('Häufigkeit', labelpad=8)                     # Label Oberflächenspannung
#plt.yscale('log')

plt.grid()                                                                                          # Gitternetz
plt.savefig('spektrum_bananium.pdf')
