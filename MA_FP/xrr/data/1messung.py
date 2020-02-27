def plot(x, y, filename):
    fig, ax = plt.subplots()
    l=1.54e-10
    q = 4 * np.pi /l *np.sin(x*np.pi/180)

    plt.yscale('log')

### Messdaten
    ax.plot(q, y, '-', linewidth=0.7, color='C0', markersize=8, markeredgewidth=2, label='Unkorrigierte Daten')

### Diffuse Messung
    a, b = np.loadtxt('1501_diffus.txt', unpack=True,delimiter=' , ')
    a = 4 * np.pi /l *np.sin(a*np.pi/180)
    ax.plot(a, b, '-', linewidth=0.7, color='C1', markersize=8, markeredgewidth=2, label='diffuse Messung')

### Daten um diffuse Messsung korrigiert
    z = []
    for i in range(len(y)):
        tmp = y[i]-b[i]
        z.append(tmp)
    ax.plot(a, z, '-', linewidth=0.7, color='C2', markersize=8, markeredgewidth=2, label='Korrigierte Daten (diffus)')


### Korrigierte Daten korrigiert um Geometriefaktor
    alpha = 0.5729673448571527
    m = []
    for i in range(len(x)):
        if (x[i] <= 0.5729673448571527):
            tmp = y[i] * (np.sin(x[i]))/(np.sin(alpha))
            m.append(tmp)
        else:
            tmp = y[i]
            m.append(tmp)
    ax.plot(q, m, '-', linewidth=0.7, color='C3', markersize=8, markeredgewidth=2, label='Korrigiert um Geometriefaktor')

### Reflektivität idealglatte OF
#    def glatt(x,max,alpha):
#        return (max-l*(x-alpha))/(max+l*(x-alpha))
#    ax.plot(q, glatt(x,max(m),alpha), '-', linewidth=0.7, color='C4', markersize=8, markeredgewidth=2, label='Idealglatt')


    plt.grid(alpha=0.3)
    ax.legend(fancybox=True, ncol=1)
    ax.set_xlabel('q in ' +r'$\frac{1}{m}$', labelpad=2)
    ax.set_ylabel('Intensität', labelpad=8)

    plt.savefig('plot_%s.pdf' %filename)


if __name__=="__main__":
    import numpy as np
    import sympy as sp
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    from matplotlib import transforms
    from matplotlib import rc
    from scipy.optimize import curve_fit
    from pylab import figure, axes, pie, title, show
    from numpy import NaN, Inf, arange, isscalar, asarray, array
    import sys
    import scipy.signal as sig
    import uncertainties
    import uncertainties.unumpy as unp
    from uncertainties import ufloat
    from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
    from math import exp, log, sin, atan
    import scipy.constants as const
    from scipy.stats import norm

    plt.rcParams['figure.figsize'] = (10, 7)
    plt.rcParams['font.size'] = 16
    plt.rcParams['lines.linewidth'] = 2

    filename = 'Messung'

    x, y = np.loadtxt('1416_messung_iguess.txt', unpack=True,delimiter=' , ')
    plot(x, y, filename)

    print('--- done ---')
