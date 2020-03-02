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
    qdiffus = von_winkel_zu_q(a)
    return qdiffus, b
def korrektur_diffuse_messung(counts, b):
    korrigierte_counts = []
    for i in range(len(counts)):
        tmp = counts[i]-b[i]
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
       190, 200, 211, 221, 232, 241,# 245, 252, 263, 266, 275, 278, 283,
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
def replace_zero_in_array_with_something_very_close_to_zero(x, replacement):
    A = []
    for i in range(len(x)):
        if (x[i] == 0):
            tmp = replacement
            A.append(tmp)
        else:
            tmp = x[i]
            A.append(tmp)
    return A
def plotallgraphs(x, counts):
    fig, ax = plt.subplots()
    q = von_winkel_zu_q(x)

### Messdaten
#    ax.plot(q, counts, linestyle='dashed', linewidth=0.5, color='C0', markersize=8, markeredgewidth=2, label='Unkorrigierte Daten')

### Diffuse Messung
    a,b = lade_diffuse_messung()
#    ax.plot(a, b, linestyle='-', linewidth=0.8, color='C0', markersize=8, markeredgewidth=2, label='Diffuse Messung')

### Daten um diffuse Messsung korrigiert
    counts_korrigiert_diffus = korrektur_diffuse_messung(counts, b)
#    ax.plot(a, counts_korrigiert_diffus, linestyle='-', linewidth=0.8, color='C1', markersize=8, markeredgewidth=2, label='Daten um diffuse Messung korrigiert')

### Korrigierte Daten korrigiert um Geometriefaktor
    counts_korrigiert_geometriefaktor = korrektur_geometriefaktor()
    counts_final = counts_korrigiert_geometriefaktor
#    ax.plot(q, counts_final, linestyle='-', color='C3', markersize=8, markeredgewidth=2, label='Daten um Geometriefaktor korrigiert')

### Peaks
    minimum_x, minimum_y, peak_array = finde_minima(counts_final, q)
    schichtdicke = berechne_schichtdicke(q, peak_array)
#    ax.plot(minimum_x, minimum_y, '+', color='indigo', markersize=8, markeredgewidth=1.5) # umdrehen funzt!
    lightindigo = lighten_color('indigo', 0.3)
#    ax.annotate(s='Verwendete Minima zur \nBerechnung der Schichtdicke. \nSchichtdicke: ' + r'(%.2f' %(schichtdicke.n * 1e10) + '$\pm$' + r'%.2f)' %(schichtdicke.s * 1e10) + r'$10^{-10}$ m', xy=(q[peak_array[0]]+2e07, counts_final[peak_array[0]]+1e04), xytext=(q[100]+300000000, counts_final[100]+30000), arrowprops={'arrowstyle': '->', 'color':lightindigo}, fontsize=9, color='indigo',  rotation=0)
#    ax.annotate(s=' ', xy=(q[peak_array[-1]], counts_final[peak_array[-1]]+1e01), xytext=(q[100]+1000000000, counts_final[100]+30000), arrowprops={'arrowstyle': '->', 'color':lightindigo}, fontsize=9, color='indigo',  rotation=0)
#    print('Schichtdicke' + str(schichtdicke))

### Kritischer Winkel Totalreflexion
    u = 39 # Ende des Plateaus
#    ax.plot(q[u], counts_final[u], 'x', color='black', markersize=3, markeredgewidth=0.8, )
#    ax.annotate(s='Kritischer Winkel \nTotalreflexion: ' + str(x[u]) + '°', xy=(q[u], counts_final[u]), xytext=(q[u]+100000000, counts_final[u]+30000000), arrowprops={'arrowstyle': '->'}, fontsize=9, color='black', va='center')

### Parratt-Plot
#    z2 = l/(2*schichtdicke.n)
#    z2 = 500e-10
#    z2 = l

#    ax.plot(q, parratt(x, n_2, n_3, sigma_1, sigma_2, z2), linestyle='dashdot', linewidth=2, color='blue', label='Parratt-Funktion')


    params,var = curve_fit(parratt, q[40:500], counts_final[40:500], p0=[n_2, n_3, sigma_1, sigma_2, z2])
    fehler = np.sqrt(np.diag(var))
    q_new = np.linspace(q[0], q[-1], 1e05, endpoint=True)
    ax.plot(q_new,parratt(q_new, *params), linestyle='dashdot', linewidth=1, color='black', label='Parratt-Fit')



### alles, was geplottet wird
#    ax.plot(q, counts, linestyle='dashed', linewidth=0.5, color='C0', markersize=8, markeredgewidth=2, label='Unkorrigierte Daten')
#    ax.plot(a, b, linestyle='-', linewidth=0.8, color='C0', markersize=8, markeredgewidth=2, label='Diffuse Messung')
#    ax.plot(a, counts_korrigiert_diffus, linestyle='-', linewidth=0.8, color='C1', markersize=8, markeredgewidth=2, label='Daten um diffuse Messung korrigiert')
    ax.plot(q, counts_final, linestyle='-', color='C3', markersize=8, markeredgewidth=2, label='Daten um Geometriefaktor korrigiert')
#    ax.plot(minimum_x, minimum_y, '+', color='indigo', markersize=8, markeredgewidth=1.5)
#    ax.plot(q[u], counts_final[u], 'x', color='black', markersize=3, markeredgewidth=0.8)
#
#    ax.annotate(s='Verwendete Minima zur \nBerechnung der Schichtdicke. \nSchichtdicke: ' + r'(%.2f' %(schichtdicke.n * 1e10) + '$\pm$' + r'%.2f)' %(schichtdicke.s * 1e10) + r'$10^{-10}$ m', xy=(q[peak_array[0]]+2e07, counts_final[peak_array[0]]+1e04), xytext=(q[100]+300000000, counts_final[100]+30000), arrowprops={'arrowstyle': '->', 'color':lightindigo}, fontsize=9, color='indigo',  rotation=0)
#    ax.annotate(s=' ', xy=(q[peak_array[-1]], counts_final[peak_array[-1]]+1e01), xytext=(q[100]+1000000000, counts_final[100]+30000), arrowprops={'arrowstyle': '->', 'color':lightindigo}, fontsize=9, color='indigo',  rotation=0)
#    ax.annotate(s='Kritischer Winkel \nTotalreflexion: ' + str(x[u]) + '°', xy=(q[u], counts_final[u]), xytext=(q[u]+100000000, counts_final[u]+30000000), arrowprops={'arrowstyle': '->'}, fontsize=9, color='black', va='center')


### Plot-Basics
    plt.yscale('log')
    plt.grid(alpha=0.3)
    ax.legend(fancybox=True, ncol=1)
    ax.set_xlabel('q in ' +r'$\frac{1}{m}$', labelpad=2)
    ax.set_ylabel('Intensität', labelpad=8)
    plt.savefig('plot_messung_allegraphen.pdf')


def parratt(x, n_2, n_3, sigma_1, sigma_2, z):
#    x = replace_zero_in_array_with_something_very_close_to_zero(x, 0.1)

    k = (2*np.pi)/l         # Betrag Wellenvektor allg.
    ki = k * np.sin(x)      # Brauchen wir wohl gar nicht
    kz_1 = k * np.sqrt(abs(n_1**2 - (np.cos(x))**2))
    kz_2 = k * np.sqrt(abs(n_2**2 - (np.cos(x))**2)) # Drei mal die gleiche Formel für verschiedene Brechungsindices 1, 2, 3
    kz_3 = k * np.sqrt(abs(n_3**2 - (np.cos(x))**2))

    r_1_2 = (kz_1-kz_2)/(kz_1+kz_2)*np.exp(-2*kz_1*kz_2*sigma_1**2)     # r was in Gleichung 10 in der Lehrstuhlversuch-Anleitung steht
    r_2_3 = (kz_2-kz_3)/(kz_2+kz_3)*np.exp(-2*kz_2*kz_3*sigma_2**2)     #

    x_2 = np.exp(2 * cm.sqrt(-1) * kz_2 * z) * r_2_3                    # Hinterer Teil der Gleichung 10
    x_1 = (r_1_2+x_2)/(1+r_1_2*x_2)                                     # Gleichung 10 zusammengefasst

    amp = 1e06
    hoffentlichpassts = abs((np.abs(x_1))**2)
    return hoffentlichpassts

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
    plt.rcParams['lines.linewidth'] = 1

    n_1=1      #Luft
    n_2=1-1e-6 #Schicht
    n_3=1-2e-6 #Substrat
    l=1.54e-10
    sigma_1 = 8e-10
    sigma_2 = 3e-10
    z2 = 10e-10
    offset = 1e10

    x, y = np.loadtxt('1416_messung_iguess.txt', unpack=True,delimiter=' , ')

    plotallgraphs(x, y)



    print('--- done ---')
