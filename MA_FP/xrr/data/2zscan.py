def plot(x, y, filename):
    fig, ax = plt.subplots()



    ax.plot(x, y, '-', linewidth=0.0000000000000001, color='C0', drawstyle='steps', markersize=8, markeredgewidth=2, label='Daten %s' %filename)


    plt.grid(alpha=0.3)
    ax.legend(fancybox=True, ncol=1)
    ax.set_xlabel('x-Label', labelpad=2)
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

    filename = 'zweiterzscan'

    x, y = np.loadtxt('1304_zscan3_iguess_or2.txt', unpack=True,delimiter=' , ')

    plot(x, y, filename)

    print('--- done ---')
