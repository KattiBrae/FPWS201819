def lighten_color(color, amount=0.5):
    import matplotlib.colors as mc
    import colorsys
    try:
        c = mc.cnames[color]
    except:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    return colorsys.hls_to_rgb(c[0], 1 - amount * (1 - c[1]), c[2])
def mitte_der_Sprungstelle(y):
    max_y = max(y)
    min_y = min(y)
#    peakfinder = sig.find_peaks(y, prominence = 0.07)
    mitte = (max_y - min_y)/2+min_y
    return (mitte)
def max_min_x(x,y):
    max_y = max(y)
    min_y = min(y)
    for i in range(len(y)):
        if (y[i] == max_y):
            max_x = x[i]
        elif (y[i] == min_y):
            min_x = x[i]
        else:
            pass
    return (max_x, min_x)
def diff_max_min_x(max_x, min_x):
    return (min_x-max_x)

def plotallgraphs(x, y):
    fig, ax = plt.subplots()
    lightC0 = lighten_color('C0', 0.2)
    lightC1 = lighten_color('C1', 0.6)
    start = 22
    stopp = 29
    max_x, min_x = max_min_x(x,y)
    diff_in_x = diff_max_min_x(max_min_x(x,y))

    ax.fill_between(x, 0, y, color=lightC0, step='mid')#, alpha=0.4)
    ax.plot(x, y, 'x', color='C0', markersize=6, markeredgewidth=1.5, label='1. Z-Scan')

#    hier jetzt vertikale linie, oder fill between, die die horizontale differenz aufzeigt!
    ax.fill_between(x=, 0, color=lightC1, )#, alpha=0.4)

    ax.annotate(s='Strahlbreite: ' + r'%.4f' %(diff_in_x) + 'mm', xy=(0.25, 5e05), fontsize=9, color='C1',  rotation=0)



    plt.grid(alpha=0.3)
    ax.legend(fancybox=True, ncol=1)
    ax.set_xlabel('Höhe z / mm', labelpad=2)
    ax.set_ylabel('Intensität', labelpad=8)

    plt.savefig('plot_zscan.pdf')


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
    plt.rcParams['font.size'] = 12
    plt.rcParams['lines.linewidth'] = 1

    x, y = np.loadtxt('1242_zscan1.txt', unpack=True,delimiter=' , ')

    plotallgraphs(x, y)



    print('--- done ---')
