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
        if (i<179):
            tmp = q[i+1]-q[i]
            abstandderpeaks.append(tmp)
        else:
            pass
    mittelwert = np.mean(abstandderpeaks)
    fehler = np.std(abstandderpeaks)
    schichtdicke = 2*np.pi/ufloat(mittelwert, fehler)
    return schichtdicke
def kritischerwinkel(delta):
    alphakrit = np.sqrt(2*delta)*180/np.pi
    qkrit = von_winkel_zu_q(alphakrit)
    return(alphakrit, qkrit)
def parratt(z):
    kz1=k*np.sqrt((n1**2-np.cos(ai)**2))
    kz2=k*np.sqrt((n2**2-np.cos(ai)**2))
    kz3=k*np.sqrt((n3**2-np.cos(ai)**2))

    r12=(kz1-kz2)/(kz1+kz2)*np.exp(-2*kz1*kz2*sigma1**2)
    r23=(kz2-kz3)/(kz2+kz3)*np.exp(-2*kz2*kz3*sigma2**2)
    x2=np.exp(0-(kz2*z)*2j)*r23
    x1=(r12+x2)/(1+r12*x2)
    par = np.abs(x1)**2
    for i in range(len(par)):   # sonst gibts nur komplexe Daten vor Beginn der Kiessing-Oszillationen
        if(i <= 296):           # 296 ist manuell angepasst
            par[i] = 1
        else:
            pass
    return par
#########################################################################
### Ab hier werden die geschriebenen Funktionen aufgerufen
#########################################################################
def plotallgraphs(x, counts):
    fig, ax = plt.subplots()
    q = von_winkel_zu_q(x)

    a,b = lade_diffuse_messung()
    counts_korrigiert_diffus = korrektur_diffuse_messung(counts, b)
    counts_korrigiert_geometriefaktor = korrektur_geometriefaktor()
    counts_final = counts_korrigiert_geometriefaktor
    minimum_x, minimum_y, peak_array = finde_minima(counts_final, q)
    schichtdicke = berechne_schichtdicke(q, peak_array)
    u = 40 # Ende des Plateaus
    beg = 11    # Anfang der sinnvollen Messdaten
    end = 300   # Ende der sinnvollen Messdaten

    unkorr = 1e-01*counts[beg:end]  # Verschiebung der Datensätze um 0.1 nach unten.
    diffusedaten = 1e-01*b[beg:end] # Verschiebung der Datensätze um 0.1 nach unten. counts_korrigiert_diffus wird in der produzierenden Funktion mit 0.1 multipliziert, da es sonst Fehler mit den Listen etc gibt... Yolo

    ax.plot(q[beg:end], unkorr, linestyle=denslydotted, linewidth = 1, color='C2', markersize=8, markeredgewidth=2, label='Unkorrigierte Daten ' +r'$\times 0.1$', alpha=0.8)
    ax.plot(a[beg:end], diffusedaten, linestyle='-', linewidth = 1, color='C5', markersize=8, markeredgewidth=2, label='Diffuse Messung ' +r'$\times 0.1$', alpha=0.8)
    ax.plot(a[beg:end], counts_korrigiert_diffus[beg:end], linestyle=denslydashed, linewidth = 1, color='C4', markersize=8, markeredgewidth=2, label='Daten um diffuse Messung korrigiert ' +r'$\times 0.1$', alpha=0.8)

    ax.plot(q[beg:end], counts_final[beg:end], linestyle='-', color='C0', label='Daten um Geometriefaktor korrigiert')
    ax.plot(minimum_x, minimum_y, '+', color='C3', markersize=10, markeredgewidth=1, label='Verw. Minima für Schichtdicke: \n' + r'$\rightarrow$' + r'z = (%.2f' %(schichtdicke.n * 1e9) + '$\pm$' + r'%.2f)' %(schichtdicke.s * 1e9) + r'$\cdot 10^{-10}$ m')

    alphakritPS, qkritPS = kritischerwinkel(delta1)
    ax.axvline(qkritPS, ymin=0, ymax=1, linewidth=0.7, linestyle=longdashs, color='C8', label=r'$\alpha_c (PS)=%.3f °$' %alphakritPS)
    alphakritSi, qkritSi = kritischerwinkel(delta2)
    ax.axvline(qkritSi, ymin=0, ymax=1, linewidth=0.7, linestyle=longdashs, color='C9', label=r'$\alpha_c (Si)=%.3f °$' %alphakritSi)

    par = parratt(z)
    plt.plot(qz, par, linestyle='-', color='C1',label='Theoriekurve')

    textstr = '\n'.join((
        'Parameter der Theoriekurve:',
        r'$n_1      = $'+'\t'+r'$ %.1f $' % (n1) + '  (Luft)',
        r'$n_2      = $'+'\t'+r'$ 1 - %.1f \cdot 10^{-6} $' % (delta1*1e06) + '  (PS)',
        r'$n_3      = $'+'\t'+r'$ 1 - %.1f \cdot 10^{-6} $' % (delta2*1e06) + '  (Si)',
        r'$\sigma_1 = $'+'\t'+r'$ %.1f \cdot 10^{-10} m $' % (sigma1*1e10) + '  (Luft/PS)',
        r'$\sigma_2 = $'+'\t'+r'$ %.1f \cdot 10^{-10} m $' % (sigma2*1e10) + '  (PS/Si)',
        '  ' + r'$z        = $'+'\t  '+r'$  %s \cdot 10^{-10} m$' % (int(z*1e10)) + '  (PS)',))
    props = dict(facecolor='white', edgecolor=(0.808, 0.808, 0.808), alpha=0.8, boxstyle='round, pad=0.2')
    ax.text(0.01, 0.01, textstr, transform=ax.transAxes, va='bottom', ha='left', bbox=props)

### Plot-Basics
    plt.yscale('log')
    plt.grid(alpha=0.3)
    ax.legend(fancybox=True, ncol=1)
    ax.set_xlabel('q in ' +r'$\frac{1}{m}$', labelpad=2)
    ax.set_ylabel('Reflektivität', labelpad=8)
    fig.tight_layout()
    plt.savefig('done_plot_messung.pdf')


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
    plt.rcParams['font.size'] = 13
    plt.rcParams['lines.linewidth'] = 2

### Verwendete alternative Linestyles
    denslydotted = (0, (1, 1))
    denslydashed = (0, (3, 1.25))
    longdashs = (0, (10, 3))

### Variablen für den ganzen Entwickler
    l=1.54e-10  # Wellenlänge
    ai = np.arange(0.06,1.505,0.0005)*np.pi/180 # x-array für Theoriekurve
    qz=4*np.pi/l*np.sin(ai) # q-array für die Theoriekurve
    k=2*np.pi/l # k-Vektor

### Parameter für die manuelle Anpassung des Parratt-Algorithmus
### Angegebene Instruktionen beschäftigen sich mit der Vergrößerung eines Parameters
#########################################################################
    #Brechungsindices
    delta1 = 0.7e-6 #PS schiebt runter und vergrößert die Amplitude, macht die Kurve steiler
    delta2 = 6.6e-6 #Si schiebt Kurve hoch, verkleinert die Amplitude
#########################################################################
    n1=1 #Luft
    n2=1- delta1   # PS
    n3=1- delta2   # Si
#########################################################################
    #Rauigkeit
    sigma1=8.1e-10 #PS verkleinert die Amplitude in den hinteren Oszillationen
    sigma2=5.7e-10 #Si drückt Ende der Kurve runter und verkleinert die Oszillationen
#########################################################################
    #Schichtdicke
    z = 870e-10  # verkleinert die Wellenlänge der Oszillationen
#########################################################################


    x, y = np.loadtxt('1416_messung.txt', unpack=True,delimiter=' , ')
    y = y/(5*995661)    # Normierung
    plotallgraphs(x, y)


    print('--- done ---')
