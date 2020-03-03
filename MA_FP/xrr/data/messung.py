def lighten_color(color, amount=0.5):
    import matplotlib.colors as mc
    import colorsys
    try:
        c = mc.cnames[color]
    except:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    return colorsys.hls_to_rgb(c[0], 1 - amount * (1 - c[1]), c[2])
def von_winkel_zu_q(x):
    q = 4 * np.pi /l *np.sin(x*np.pi/180)
    return q
def lade_diffuse_messung():
    a, b = np.loadtxt('1501_diffus.txt', unpack=True,delimiter=' , ')
### Normierung
    b = b/959913
    qdiffus = von_winkel_zu_q(a)
    return qdiffus, b
def korrektur_diffuse_messung(counts, b):
    korrigierte_counts = []
    for i in range(len(counts)):
        tmp = 1e-01*(counts[i]-b[i])
        korrigierte_counts.append(tmp)
    return korrigierte_counts
def korrektur_geometriefaktor():
    alpha = 0.5
    m = []
    for i in range(len(x)):
        if (x[i] <= alpha):
            tmp = y[i] / ((np.sin(x[i]))/(np.sin(alpha)))
            m.append(tmp)
        else:
            tmp = y[i]
            m.append(tmp)
    return m
def finde_minima(m, q):
### Logarithmiere die Daten zur Basis 10
    logm = []
    for i in range(len(m)):
        if (m[i] != 0):
            tmp = np.log10(m[i])
            logm.append(tmp)
        else:
            logm.append(0)
### Negatives VZ um mit find_peaks arbeiten zu können
    neglogm = []
    for i in range(len(logm)):
        tmp = -logm[i]
        neglogm.append(tmp)
### Peaks finden
    peakfinder = sig.find_peaks(neglogm, prominence = 0.07)
### Peaks in den Einträgen:
    peak_array = [ 66,  76,  86,  96, 106, 116, 127, 137, 147, 158, 169, 179,
#       190, 200, 211, 221, 232, 241,# 245, 252, 263, 266, 275, 278, 283,
#       285, 292, 294, 299, 304, 306, 312, 314, 316, 320, 326, 328, 331,
#       335, 338, 340, 344, 346, 349, 352, 355, 359, 363, 365, 368, 370,
#       372, 375, 377, 380, 382, 385, 390, 393, 396, 398, 402, 404, 408,
#       413, 415, 421, 423, 426, 429, 433, 435, 438, 442, 445, 448, 453,
#       455, 459, 462, 465, 469, 472, 478, 483, 489, 494, 7
       ] ### Manuell eingekürzt, da Minima bei großen q sehr unscharf

    peak_x = []
    peak_y = []
    for i in peak_array:
        peak_x.append(q[i])
        peak_y.append(m[i])
    return peak_x, peak_y, peak_array

def berechne_schichtdicke(q, peak_array):
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
    return schichtdicke
def plotallgraphs(x, counts):
    fig, ax = plt.subplots()
    q = von_winkel_zu_q(x)

    a,b = lade_diffuse_messung()
    counts_korrigiert_diffus = korrektur_diffuse_messung(counts, b)
    counts_korrigiert_geometriefaktor = korrektur_geometriefaktor()
    counts_final = counts_korrigiert_geometriefaktor
    minimum_x, minimum_y, peak_array = finde_minima(counts_final, q)
    schichtdicke = berechne_schichtdicke(q, peak_array)
    lightC3 = lighten_color('C3', 0.6)
    u = 40 # Ende des Plateaus
    beg = 11    #a Anfang der sinnvollen Messdaten
    end = 300

### alles, was geplottet wird
#    ax.plot(q[:beg+1], counts[:beg+1], linestyle='dotted', linewidth=0.5, color='C0', markersize=8, markeredgewidth=2)
#    ax.plot(a[:beg+1], b[:beg+1], linestyle='dotted', linewidth=0.8, color='C0', markersize=8, markeredgewidth=2)
#    ax.plot(a[:beg+1], counts_korrigiert_diffus[:beg+1], linestyle='dotted', linewidth=0.8, color='C1', markersize=8, markeredgewidth=2)
#    ax.plot(q[:beg+1], counts_final[:beg+1], linestyle='dotted', color='C3')
    unkorr = 1e-01*counts[beg:end]
    diffusedaten = 1e-02*b[beg:end]
    korrdaten = counts_korrigiert_diffus[beg:end]

    ax.plot(q[beg:end], unkorr, linestyle=karDOTian, color='black', markersize=8, markeredgewidth=2, label='Unkorrigierte Daten', alpha=0.6)
    ax.plot(a[beg:end], diffusedaten, linestyle=karDASHian, color='black', markersize=8, markeredgewidth=2, label='Diffuse Messung', alpha=0.6)
    ax.plot(a[beg:end], korrdaten, linestyle='-', color='black', markersize=8, markeredgewidth=2, label='Daten um diffuse Messung korrigiert', alpha=0.4)
    ax.plot(q[beg:end], counts_final[beg:end], linestyle='-', color='C0', label='Daten um Geometriefaktor korrigiert')
    ax.plot(minimum_x, minimum_y, '+', color='C3', markersize=10, markeredgewidth=0.8, label='Verwendete Minima ' + r'$\rightarrow$' +' Schichtdicke: \n' + r'(%.2f' %(schichtdicke.n * 1e10) + '$\pm$' + r'%.2f)' %(schichtdicke.s * 1e10) + r'$10^{-10}$ m')
    ax.plot(q[u], counts_final[u], '+', color='black', markersize=10, markeredgewidth=0.8)

#    ax.annotate(s='Verwendete Minima zur \nBerechnung der Schichtdicke. \nSchichtdicke: ' + r'(%.2f' %(schichtdicke.n * 1e10) + '$\pm$' + r'%.2f)' %(schichtdicke.s * 1e10) + r'$10^{-10}$ m', xy=(q[peak_array[0]]+1e07, counts_final[peak_array[0]]+5e-03), xytext=(q[100]+300000000, counts_final[100]+1e-02), arrowprops={'arrowstyle': '->', 'color':lightC3}, fontsize=9, color='C3',  rotation=0)
#    ax.annotate(s=' ', xy=(q[peak_array[-1]]+1e07, counts_final[peak_array[-1]]+5e-06), xytext=(q[100]+7e08, counts_final[100]+1e-02), arrowprops={'arrowstyle': '->', 'color':lightC3}, fontsize=9, color='C3',  rotation=0)
    ax.annotate(s='Kritischer Winkel \nTotalreflexion: ' + str(x[u]) + '°', xy=(q[u], counts_final[u]), xytext=(q[u]+100000000, counts_final[u]), arrowprops={'arrowstyle': '->'}, fontsize=9, color='black', va='center')

    x1 = parratt(z2_1)
    plt.plot(qz, np.abs(x1)**2, linestyle='-', color='C1',label='Theoriekurve')
    
#    x1 = parratt(z2_2)
#    plt.plot(qz, np.abs(x1)**2, linestyle='-', color='C2',label='Theoriekurve z=%s' %z2_2)

### Plot-Basics
    plt.yscale('log')
    plt.grid(alpha=0.3)
    ax.legend(fancybox=True, ncol=1)
    ax.set_xlabel('q in ' +r'$\frac{1}{m}$', labelpad=2)
    ax.set_ylabel('Reflektivität', labelpad=8)
    fig.tight_layout()

    plt.savefig('plot_messung_allegraphen.pdf')

    print()

def parratt(z2):

#    k = (2*np.pi)/l         # Betrag Wellenvektor allg.
#    ki = k * np.sin(x)      # Brauchen wir wohl gar nicht
#    kz_1 = k * np.sqrt(abs(n_1**2 - (np.cos(x))**2))
#    kz_2 = k * np.sqrt(abs(n_2**2 - (np.cos(x))**2)) # Drei mal die gleiche Formel für verschiedene Brechungsindices 1, 2, 3
#    kz_3 = k * np.sqrt(abs(n_3**2 - (np.cos(x))**2))
#
#    r_1_2 = (kz_1-kz_2)/(kz_1+kz_2)*np.exp(-2*kz_1*kz_2*sigma_1**2)     # r was in Gleichung 10 in der Lehrstuhlversuch-Anleitung steht
#    r_2_3 = (kz_2-kz_3)/(kz_2+kz_3)*np.exp(-2*kz_2*kz_3*sigma_2**2)     #
#
#    x_2 = np.exp(2 * cm.sqrt(-1) * kz_2 * z) * r_2_3                    # Hinterer Teil der Gleichung 10
#    x_1 = (r_1_2+x_2)/(1+r_1_2*x_2)                                     # Gleichung 10 zusammengefasst
#
#    amp = 1e06
#    hoffentlichpassts = abs((np.abs(x_1))**2)
    #z-Komponenten
    kz1=k*np.sqrt((n1**2-np.cos(ai)**2))
    kz2=k*np.sqrt((n2**2-np.cos(ai)**2))
    kz3=k*np.sqrt((n3**2-np.cos(ai)**2))

    #modifizierte Fresnelkoeffizienten
    r12=(kz1-kz2)/(kz1+kz2)*np.exp(-2*kz1*kz2*sigma1**2)
    r23=(kz2-kz3)/(kz2+kz3)*np.exp(-2*kz2*kz3*sigma2**2)
    x2=np.exp(0-(kz2*z2)*2j)*r23
    x1=(r12+x2)/(1+r12*x2)

    return x1

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
    import cmath as cm

    plt.rcParams['figure.figsize'] = (10, 7)
    plt.rcParams['font.size'] = 12
    plt.rcParams['lines.linewidth'] = 1.5

    karDASHian = (0, (5, 2, 2, 2, 2, 2))
    karDOTian = (0, (1, 2.5))
    l=1.54e-10

    ai = np.arange(0.206,1.505,0.0005)*np.pi/180 # x-array für Theoriekurve
    qz=4*np.pi/l*np.sin(ai) # q-array für die Theoriekurve
    k=2*np.pi/l # k-Vektor

### Angegebene Instruktionen beschäftigen sich mit der Vergrößerung eines Parameters
#########################################################################
    #Brechungsindices
    fak1 = 0.7e-6 #PS schiebt runter und vergrößert die Amplitude, macht die Kurve steiler
#    fak2 = 6.7e-6 #Si schiebt Kurve hoch, verkleinert die Amplitude
    fak2 = 6.6e-6 #Si schiebt Kurve hoch, verkleinert die Amplitude
#########################################################################
    n1=1 #Luft
    n2=1- fak1   # PS
    n3=1- fak2   # Si
#########################################################################
    #Rauigkeit
    sigma1=8.1e-10 #PS verkleinert die Amplitude in den hinteren Oszillationen
    sigma2=5.7e-10 #Si drückt Ende der Kurve runter und verkleinert die Oszillationen
#########################################################################
    #Schichtdicke
    z2_1 = 870e-10  # verkleinert die Wellenlänge der Oszillationen
#########################################################################


    x, y = np.loadtxt('1416_messung_iguess.txt', unpack=True,delimiter=' , ')
### Normierung
    y = y/(5*995661)

    plotallgraphs(x, y)


    print('--- done ---')
