def lighten_color(color, amount=0.5):
    import matplotlib.colors as mc
    import colorsys
    try:
        c = mc.cnames[color]
    except:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    return colorsys.hls_to_rgb(c[0], 1 - amount * (1 - c[1]), c[2])
def plotallgraphs(x, y):
    fig, ax = plt.subplots()
    lightC0 = lighten_color('C0', 1)
    lightC1 = lighten_color('C1', 1)

    links = 14
    rechts = 39

    ax.fill_between(x, 0, y, color=lightC0, step='mid', alpha=0.3)     # Daten blau hinterlegt
#    ax.plot(x+(x[1]-x[0])/2, y, '-', drawstyle='steps', color=lightC0, linewidth=0.1, alpha=0.4)    # Umrandung der hinterlegten Daten
    ax.plot(x, y, 'x', color='C0', markersize=6, markeredgewidth=1.5, label='1. rocking-Scan')    # Daten als blaue Kreuze
#    ax.axvline(x[links], color=lightC1, alpha=0.3), ax.axvline(x[rechts], color=lightC1, alpha=0.3)
    ax.annotate(s='Geometriewinkel: \n' + r'%.2f' %(x[links]) + '°', xy=(x[links], y[links]), xytext=(x[links]-0.5, y[links]+0.25), arrowprops={'arrowstyle': '->', 'color':lightC1}, va='center', ha='left', color='C1',  rotation=0)
    ax.annotate(s='Geometriewinkel: \n' + r'%.2f' %(x[rechts]) + '°', xy=(x[rechts], y[rechts]), xytext=(x[rechts]+0.5, y[rechts]+0.25), arrowprops={'arrowstyle': '->', 'color':lightC1}, va='center', ha='right', color='C1',  rotation=0)

#    plt.yscale('log')
    plt.grid(alpha=0.3)
    ax.legend(fancybox=True, ncol=1)
    ax.set_xlabel('Winkel ' + r'$\alpha_i$', labelpad=2)
    ax.set_ylabel('Reflektivität', labelpad=8)
    fig.tight_layout()
    plt.savefig('done_plot_rockingscan.pdf')

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

    x, y = np.loadtxt('1219_rock1.txt', unpack=True,delimiter=' , ')

### Normierung
    y = y/995661
    plotallgraphs(x, y)

    print('--- done ---')
