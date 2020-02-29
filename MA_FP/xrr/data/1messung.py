def cutDataArrayBetweenTwoValues(countingup, beingcut, uG, oG): # cuts off data from array before start and after stop of measurement // schneidet am Array die Werte vor und nach der Messung ab
        ############################## takeListsMakeArrays calling cutDataArrayBetweenTwoValues
    A = []                                                                              # hier wird abgespeichert
    for i in countingup:                                                          # für alle Indices in der Liste date
        if i >= uG and i <= oG:                      # wenn der Wert von date beim Index kleiner ist als der start oder größer ist als der stop
            A.append(i)                                                              # speichere den Wert von dem Datensatz in A
        else:
            pass

    return (A)

def plot(x, y, filename):
    fig, ax = plt.subplots()
    l=1.54e-10
    q = 4 * np.pi /l *np.sin(x*np.pi/180)

    plt.yscale('log')

### Messdaten
    ax.plot(q, y, '-', color='C8', markersize=8, markeredgewidth=2, label='Unkorrigierte Daten')

### Diffuse Messung
    a, b = np.loadtxt('1501_diffus.txt', unpack=True,delimiter=' , ')
    a = 4 * np.pi /l *np.sin(a*np.pi/180)
    ax.plot(a, b, '-', color='C1', markersize=8, markeredgewidth=2, label='Diffuse Messung')

### Daten um diffuse Messsung korrigiert
    z = []
    for i in range(len(y)):
        tmp = y[i]-b[i]
        z.append(tmp)
    ax.plot(a, z, '-', color='C0', markersize=8, markeredgewidth=2, label='Daten um diffuse Messung korrigiert')


### Korrigierte Daten korrigiert um Geometriefaktor
    alpha = 0.5
    m = []
    for i in range(len(x)):
        if (x[i] <= 0.5729673448571527):
            tmp = y[i] / ((np.sin(x[i]))/(np.sin(alpha)))
            m.append(tmp)
        else:
            tmp = y[i]
            m.append(tmp)
    ax.plot(q, m, '-', color='C3', markersize=8, markeredgewidth=2, label='Daten um Geometriefaktor korrigiert')

### Reflektivität idealglatte OF
#    def glatt(x,max,alpha):
#        return (max-l*(x-alpha))/(max+l*(x-alpha))
#    ax.plot(q, glatt(x,max(m),alpha), '-',color='C4', markersize=8, markeredgewidth=2, label='Idealglatt')

### Peaks
    # logarithmiere die Daten und finde die Minima
    logm = []
    for i in range(len(m)):
        if (m[i] != 0):
            tmp = np.log10(m[i])
            logm.append(tmp)
        else:
            logm.append(0)
#    ax.plot(q, logm, '-',color='blue', markersize=8, markeredgewidth=2) # logarithmieren funzt!
    neglogm = []
    for i in range(len(logm)):
        tmp = -logm[i]
        neglogm.append(tmp)
#    ax.plot(q, neglogm, '-',color='blue', markersize=8, markeredgewidth=2) # umdrehen funzt!
    peakfinder = sig.find_peaks(neglogm, prominence = 0.07)
#    print(peakfinder)

    peak_array = [ 66,  76,  86,  96, 106, 116, 127, 137, 147, 158, 169, 179,
       190, 200, 211, 221, 232, 241,# 245, 252, 263, 266, 275, 278, 283,
#       285, 292, 294, 299, 304, 306, 312, 314, 316, 320, 326, 328, 331,
#       335, 338, 340, 344, 346, 349, 352, 355, 359, 363, 365, 368, 370,
#       372, 375, 377, 380, 382, 385, 390, 393, 396, 398, 402, 404, 408,
#       413, 415, 421, 423, 426, 429, 433, 435, 438, 442, 445, 448, 453,
#       455, 459, 462, 465, 469, 472, 478, 483, 489, 494, 7
       ]

    peak_x = []
    peak_y = []
    for i in peak_array:
        peak_x.append(q[i])
        peak_y.append(m[i])

    abstandderpeaks = []
    for i in peak_array:
        if (i<241):
            tmp = q[i+1]-q[i]
            abstandderpeaks.append(tmp)
        else:
            pass
    mittelwert = np.mean(abstandderpeaks)
    fehler = np.std(abstandderpeaks)
    schichtdicke = 2*np.pi/ufloat(mittelwert, fehler)
    print('Mittelwert der Abstände: ' + str(mittelwert) + ' ; \t Schichtdicke (Kehrwert): ' + str(schichtdicke))

    ax.plot(peak_x, peak_y, 'x', color='C2', markersize=8, markeredgewidth=1.5, label='Verwendete Minima, Schichtdicke: ' + str(schichtdicke) + 'm') # umdrehen funzt!

### Kritischer Winkel Totalreflexion
    u = 39 # Ende des Plateaus
    print('Kritischer Winkel ' + str(x[u]))
    ax.plot(q[u], m[u], 'x', color='black', markersize=8, markeredgewidth=1, label='Kritischer Winkel Totalreflexion: ' + str(x[u]) + '°')


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
    plt.rcParams['font.size'] = 12
    plt.rcParams['lines.linewidth'] = 1

    filename = 'Messung'

    x, y = np.loadtxt('1416_messung_iguess.txt', unpack=True,delimiter=' , ')
    plot(x, y, filename)

    print('--- done ---')
