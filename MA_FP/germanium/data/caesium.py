def vollesspektrum(x, y):
    fig, ax = plt.subplots()

    ax.fill_between(x, 0, y, step='mid')#, alpha=0.4)
    ax.plot(x, y, '-', linewidth=0.0000000000000001, color='C0', drawstyle='steps', markersize=8, markeredgewidth=2, label='Daten')

    plt.grid(alpha=0.3)
    ax.legend(fancybox=True, ncol=1)
    ax.set_xlabel('Channel', labelpad=2)
    ax.set_ylabel('Häufigkeit', labelpad=8)

    plt.savefig('caesium_vollesspektrum.pdf')

def vollesspektrumlog(x, y):
    fig, ax = plt.subplots()
    dy = np.sqrt(y)


#    ax.errorbar(x, y, yerr=dy, fmt="none", capsize=2, capthick=1, color='C1', label='Unsicherheit')
    ax.fill_between(x, 0, y, step='mid')#, alpha=0.4)
    ax.plot(x, y, '-', linewidth=0.0000000000000001, color='C0', drawstyle='steps', markersize=8, markeredgewidth=2, label='Daten')

#    ax.fill_between(x, y-dy, y+dy, linewidth=3, color='C2', alpha=0.4, label='Unsicherheit')

    plt.yscale('log')

    plt.grid(alpha=0.3)
    ax.legend(fancybox=True, ncol=1)
    ax.set_xlabel('Channel', labelpad=2)
    ax.set_ylabel('Häufigkeit', labelpad=8)

    plt.savefig('caesium_vollesspektrumlog.pdf')

def channel(x, y, peaks_x, peakno, width, left, right):
    tmp_x = []
    for j in range(len(peaks_x)):
        if (j == peakno):
            for i in range(len(y)):
                if (x[i] >= peaks_x[j]-width+left) and (x[i] <= peaks_x[j]+width+right):
                    tmp_x.append(x[i])
                else:
                    pass
    mean = np.mean(tmp_x)
    sigma = np.std(tmp_x)
    print('----------------------------')
    print('Mittelwert über np.mean')
    print('Mean: ' + str(mean))
    print('Std: ' + str(sigma))
    print('----------------------------')

    return (tmp_x, mean, sigma)

def counts(x, y, peaks_x, peakno, width, left, right):
    tmp_y = []
    for j in range(len(peaks_x)):
        if (j == peakno):
            for i in range(len(y)):
                if (x[i] >= peaks_x[j]-width+left) and (x[i] <= peaks_x[j]+width+right):
                    tmp_y.append(y[i])
                else:
                    pass
    total = sum(tmp_y)
    return (tmp_y, total)

def gaussfit(x, y, peaks_x, peakno, width, amp, off, left, right):
    fig, ax = plt.subplots()

    tmp_x, mean, sigma = channel(x, y, peaks_x, peakno, width, left, right)
    tmp_y, total = counts(x, y, peaks_x, peakno, width, left, right)

    def gauss(x,a,mu,std,c):
        return a/np.sqrt((2*const.pi*std**2)) * np.exp(-(x-mu)**2/(2*std**2))+c

    params,var = curve_fit(gauss,x,y,p0=[amp,mean,sigma,off], maxfev=5000)
    fehler = np.sqrt(np.diag(var))

    print('----------------------------')
    print('Parameter und Fehler aus dem Fit')
    print('Amp, Mean, Std, Off')
    print(params)
    print(fehler)
    print('----------------------------')

    print('----------------------------')
    print('Peakinhalt über Summe der Counts')
    print('Inhalt: ' + str(total-off))        # Peak-Inhalt
    print('Fehler Inhalt: ' + str(np.sqrt(total-off)))   # Fehler Peak-Inhalt
    print('----------------------------')

    mean=params[1]
    std=params[2]

    meanint = int(round(mean))
    mean = meanint

    FWHM = 2*np.sqrt(2*np.log(2))*std
    FWHMint = int(round(FWHM))
    FWHM = FWHMint

    FWHM_x = [mean-FWHM/2 +0.5, mean+FWHM/2 +0.5]
#    FWHM_y = [gauss(mean, *params)/2, gauss(mean, *params)/2]
    FWHM_y = [y[meanint]/2, y[meanint]/2]

    FWTM = 2*np.sqrt(2*np.log(10))*std
    FWTMint = int(round(FWTM))
    FWTM = FWTMint

    FWTM_x = [mean-FWTM/2 , mean+FWTM/2]
#    FWTM_y = [gauss(mean, *params)/10, gauss(mean, *params)/10]
    FWTM_y = [y[meanint]/10, y[meanint]/10]

    print('----------------------------')
    print('FWHM: ' + str(FWHM))
    print('FWTM: ' + str(FWTM))
    print('----------------------------')

#### Plot Halbwertsbreite, Zehntelwertsbreite
    ax.plot(FWHM_x, FWHM_y, '-', color='C3')
    ax.annotate((xy)=(mean+FWHM/2 + 0.5, gauss(mean, *params)/2) , fontsize= 12, color='C3', s='Halbwertsbreite: \n 10 Channel', rotation=0)
#    ax.axvspan(mean-FWHM/2, mean+FWHM/2, facecolor='C2', alpha=0.1)
    ax.plot(FWTM_x, FWTM_y, '-', color='C3')
    ax.annotate((xy)=(mean+FWTM/10 + 6.5, gauss(mean, *params)/10 + 50) , fontsize=12, color='C3', s='Zehntelwertsbreite: \n 19 Channel', rotation=0)

#### Plot Daten
    ax.fill_between(tmp_x, 0, tmp_y, step='mid', alpha=0.4)
    ax.plot(tmp_x, tmp_y, 'x', color='C0', drawstyle='steps', markersize=8, markeredgewidth=2, label='Daten')

#### Plot Fit
    x_new = np.linspace(tmp_x[0], tmp_x[-1], 5000, endpoint=True)
    ax.plot(x_new,gauss(x_new,*params),'-', color='C1', label='Normalverteilung')


    plt.grid(alpha=0.3)
    ax.legend(fancybox=True, ncol=1)
    ax.set_xlabel('Channel', labelpad=2)
    ax.set_ylabel('Häufigkeit', labelpad=8)

    plt.savefig('caesium_photopeak.pdf')


def kontinuum(x, y, peaks_x, peakno, width, amp, off, left, right):
    fig, ax = plt.subplots()

    tmp_x, mean, sigma = channel(x, y, peaks_x, peakno, width, left, right)
    tmp_y, total = counts(x, y, peaks_x, peakno, width, left, right)

    ax.fill_between(tmp_x, 0, tmp_y, step='mid')#, alpha=0.4)
    ax.plot(tmp_x, tmp_y, '-', linewidth=0.0000000000000001, color='C0', drawstyle='steps', markersize=8, markeredgewidth=2, label='Daten')


    plt.grid(alpha=0.3)
    ax.legend(fancybox=True, ncol=1)
    ax.set_xlabel('Channel', labelpad=2)
    ax.set_ylabel('Häufigkeit', labelpad=8)



#suche jetzt daten zwischen ca. 2000 und 2500 und fitte von links und rechts je eine grade, schnittpunkt ist dann das Ende der Kante

    plt.savefig('caesium_kontinuum.pdf')


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


    y = np.loadtxt('caesium.txt', unpack=True,delimiter=' ')
    x = np.arange(0, len(y), 1 )

#    peaks = sig.find_peaks(y, prominence = 50)
#    print(peaks)

    peaks_x = [ 3197 ]
    peakno = np.arange(0, len(peaks_x), 1 )

    peaks_counts = []
    for i in range(len(x)):
        for j in range(len(peaks_x)):
            if ( i == peaks_x[j]):
                peaks_counts.append(y[i])
            else:
                pass

    vollesspektrum(x, y)
    vollesspektrumlog(x, y)

    gaussfit(x, y, peaks_x, 0, 15, 0, 10, 0, -2)

    peaks_x_halbe = [ int(round(3197/2)) ]
    kontinuum(x, y, peaks_x_halbe, 0, 1580, 0, 10, 0, 0)


    print('--- done ---')
