def lighten_color(color, amount=0.5):
    import matplotlib.colors as mc
    import colorsys
    try:
        c = mc.cnames[color]
    except:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    return colorsys.hls_to_rgb(c[0], 1 - amount * (1 - c[1]), c[2])
def max_min_xy(x,y):
    max_y = max(y)
    for i in range(len(y)):
        if (y[i] == max_y):
            max_x = x[i]
            min_x = x[i+5]
            min_y = y[i+5]
        else:
            pass
    return (max_y, min_y, max_x, min_x)
def diff_max_min_x(max_x, min_x):
    return (min_x-max_x)
def plotallgraphs(x, y):
    fig, ax = plt.subplots()
    ax2 = ax.twinx()

    lightC0 = lighten_color('C0', 1)
    lightC1 = lighten_color('C1', 1)

    max_y, min_y, max_x, min_x = max_min_xy(x,y)
    diff_in_x = diff_max_min_x(max_x, min_x)

    ax.fill_between(x, 0, y, color=lightC0, step='mid', alpha=0.3)     # Daten blau hinterlegt
    ax.plot(x+(x[1]-x[0])/2, y, '-', drawstyle='steps', color=lightC0, linewidth=0.1, alpha=0.4)    # Umrandung der hinterlegten Daten
    ax2.axvspan(max_x, min_x, 0, 1, color=lightC1, alpha=0.25)    # Strahlbreite orange hinterlegt
    lns1 = ax2.plot([max_x, min_x], [0.5, 0.5], '-', linewidth=1, color='C1', label='Strahlbreite')    # Strahlbreite als Balken
    lns2 = ax.plot(x, y, 'x', color='C0', markersize=6, markeredgewidth=1.5, label='1. z-Scan')    # Daten als blaue Kreuze
    ax2.annotate(s='Strahlbreite: \n' + r'%.2f' %(diff_in_x) + 'mm = ' + r'%.2f $\cdot 10^{-3}$ m' %(diff_in_x), xy=(0.18, 0.5), va='center', color='C1',  rotation=0)
    ax2.annotate(s=' ', xy=(max_x-1.35e-02, 0.5), xytext=(min_x+2.9e-02, 0.5), ha='center', va='center', arrowprops={'arrowstyle': '<->', 'color':'C1'}, color='C1',  rotation=0)
    ax.annotate(xy=(max_x+0.01, max_y-10000), xytext=(max_x+0.25, max_y-250000), va='center', arrowprops={'arrowstyle': '->', 'color':'C2'}, color='C2', s='Globale max. Intensität\nder Justage: \n995661 counts (Daten) \n' + r'$\rightarrow$' + ' für die Normierung' , rotation=0)

### Normierte Achse Reflektivität
    ax2.plot(x, y/995661, linestyle='-', linewidth=0, color='C0')    # Daten als blaue Kreuze


    plt.grid(alpha=0.3)
    ax.legend(fancybox=True, ncol=1)
    ax.set_xlabel('Höhe z / mm', labelpad=2)
    ax.set_ylabel('Intensität', labelpad=8)
    ax2.set_ylabel('Reflektivität', labelpad=12)  # zweite y-Achse

    lns = lns1 + lns2
    labs = [l.get_label() for l in lns]
    ax.legend(lns, labs, loc=0)

    fig.tight_layout()

    plt.savefig('done_plot_zscan.pdf')


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

    x, y = np.loadtxt('1242_zscan1.txt', unpack=True,delimiter=' , ')

    plotallgraphs(x, y)



    print('--- done ---')
