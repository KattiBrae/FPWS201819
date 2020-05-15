def lighten_color(color, amount=0.5):
    import matplotlib.colors as mc
    import colorsys
    try:
        c = mc.cnames[color]
    except:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    return colorsys.hls_to_rgb(c[0], 1 - amount * (1 - c[1]), c[2])
def gaussfit(x, y, peaks_x, width, amp, off, left, right):
    fig, ax = plt.subplots()
    ax2 = ax.twinx()

    lightC0 = lighten_color('C0', 1)
    lightC1 = lighten_color('C1', 1)

    tmp_x = x
    tmp_y = y
    mean = np.mean(tmp_x)
    sigma = np.std(tmp_x)

    def gauss(x,a,mu,std,c):
        return a/np.sqrt((2*const.pi*std**2)) * np.exp(-(x-mu)**2/(2*std**2))+c

    params,var = curve_fit(gauss,x,y,p0=[amp,mean,sigma,off], maxfev=1000000000)
    fehler = np.sqrt(np.diag(var))
    print('----------------------------')
    print('Params: ')
    print(params)
    print('Fehler: ')
    print(fehler)
    print('----------------------------')

### Plot Halbwertsbreite
    mean=params[1]
    std=params[2]

    counthwb = gauss(mean,*params)
#    print('Mean: ' + str(mean))
#    print('Bla: ' + str(counthwb))

    FWHM = 2*np.sqrt(2*np.log(2))*std
    FWHM_x = [mean-FWHM/2, mean+FWHM/2]
    FWHM_y = [counthwb/2, counthwb/2]

    print('----------------------------')
    print('FWHM Fit: ' + str(FWHM))
    print('----------------------------')

### Plot Daten
    ax.fill_between(x, 0, y, color=lightC0, step='mid', alpha=0.3)     # Daten blau hinterlegt
    ax.plot(x+(x[1]-x[0])/2, y, '-', drawstyle='steps', color=lightC0, linewidth=0.1, alpha=0.4)    # Umrandung der hinterlegten Daten
    lns1 = ax.plot(x, y, 'x', color='C0', markersize=6, markeredgewidth=1.5, label='1. Detektor-Scan')    # Daten als blaue Kreuze

#### Plot Halbwertsbreite
    ax.plot(FWHM_x, FWHM_y, '-', color='C2')
#    ax.annotate((xy)=(mean -0.5, gauss(mean, *params)/2 ) , fontsize= 12, color='C2', s='Halbwertsbreite: 0.10° \nKleinwinkelnäherung ' + r'$sin(\alpha_i)\approx \alpha_i$' +'', rotation=0)
    ax.annotate((xy)=(mean -0.5, gauss(mean, *params)/2 ) , fontsize= 12, color='C2', s='Halbwertsbreite: 0.10°', rotation=0)

#### Plot Fit
    x_new = np.linspace(tmp_x[0], tmp_x[-1], 5000, endpoint=True)
    lns2 = ax.plot(x_new,gauss(x_new,*params),'-', color='C1', label='Normalverteilung')
    ax.annotate((xy)=(mean - 0.5, gauss(mean, *params)-40000) , fontsize= 12, color='C1', s='Max. Intensität: \n950367 counts (Fit)' , rotation=0)
    ax.annotate((xy)=(mean - 0.5, gauss(mean, *params)-140000) , fontsize= 12, color='C0', s='Max. Intensität: \n959913 counts (Daten)' , rotation=0)

### Normierte Achse Reflektivität
    ax2.plot(x, y/959913, linestyle='-', linewidth=0, color='C0')    # Daten als blaue Kreuze

    plt.grid(alpha=0.3)
    ax.set_xlabel('Winkel ' +r'$\alpha_i$', labelpad=2)
    ax.set_ylabel('Intensität', labelpad=8)
    ax2.set_ylabel('Reflektivität', labelpad=12)  # zweite y-Achse

    lns = lns1 + lns2
    labs = [l.get_label() for l in lns]
    ax.legend(lns, labs, loc=0)

    fig.tight_layout()

    plt.savefig('done_plot_detektorscan.pdf')



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

    x, y = np.loadtxt('1239_detektorscan1.txt', unpack=True,delimiter=' , ')

    gaussfit(x, y, 0, 0.3, 1000000, 0, 0, 0)

    print('--- done ---')
