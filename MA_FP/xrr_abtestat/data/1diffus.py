def vollesspektrum(x, y):
    fig, ax = plt.subplots()

    ax.fill_between(x, 0, y, step='mid')#, alpha=0.4)
    ax.plot(x, y, '-', linewidth=0.0000000000000001, color='C0', drawstyle='steps', markersize=8, markeredgewidth=2, label='Daten')

    plt.grid(alpha=0.3)
    ax.legend(fancybox=True, ncol=1)
    ax.set_xlabel('Energie in keV', labelpad=2)
    ax.set_ylabel('Häufigkeit', labelpad=8)

    plt.savefig('bananium_vollesspektrum.pdf')


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
    ax.set_xlabel('Energie in keV', labelpad=2)
    ax.set_ylabel('Häufigkeit', labelpad=8)

    plt.savefig('bananium_vollesspektrumlog.pdf')

def channel(x, y, peaks_x, peakno, width, left, right):
    tmp_x = []
    for j in range(len(peaks_x)): # zählt den Index der Peaks hoch
        if (j == peakno):       # wenn Index == Peak Nummer
            for i in range(len(y)):     # zählt den Index der counts hoch
                if (x[i] >= peaks_x[j]-width+left) and (x[i] <= peaks_x[j]+width+right): # wenn energie kleiner/größer als peakenergie
                    tmp_x.append(x[i])
                else:
                    pass
    mean = np.mean(tmp_x)
    sigma = np.std(tmp_x)
#    print('----------------------------')
#    print('Mittelwert über np.mean')
#    print('Mean: ' + str(mean))
#    print('Std: ' + str(sigma))
#    print('----------------------------')

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

def channelarraytoenergyarray(intake, steigung, yachse):
    tmp = []
    for i in range(len(intake)):
        val = steigung*intake[i]+yachse
        tmp.append(val)
    return(tmp)

def gaussfit(x, y, peaks_x, peakno, width, amp, off, left, right, steigung, yachse):
    fig, ax = plt.subplots()

    tmp_x, mean_channel, sigma = channel(x, y, peaks_x, peakno, width, left, right)
    tmp_y, total = counts(x, y, peaks_x, peakno, width, left, right)

    tmp_x = channelarraytoenergyarray(tmp_x, steigung, yachse)
    mean = np.mean(tmp_x)
    sigma = np.std(tmp_x)
    x = channelarraytoenergyarray(x, steigung, yachse)
    einchannel = steigung

#    if (peakno == 0):
#        amp = 0.01
#        sigma = 0.01
#        mean = 191

    def gauss(x,a,mu,std,c):
        return a/np.sqrt((2*const.pi*std**2)) * np.exp(-(x-mu)**2/(2*std**2))+c
#        return a * np.exp(-(x-mu)**2/(2*std**2))+c

    params,var = curve_fit(gauss,x,y,p0=[amp,mean,sigma,off], maxfev=1000000000)
    fehler = np.sqrt(np.diag(var))

#    print('----------------------------')
#    print('Parameter und Fehler aus dem Fit')
#    print('Amp, Mean, Std, Off')
#    print(params)
#    print(fehler)
#    print('----------------------------')

    print('----------------------------')
    print('Peakinhalt über Summe der Counts, Peak ' + str(peakno))
    print('Inhalt: ' + str(total-off))        # Peak-Inhalt
    print('Fehler Inhalt: ' + str(np.sqrt(total-off)))   # Fehler Peak-Inhalt
    print('----------------------------')
#
#    mean=params[1]
#    std=params[2]
#
#    counthwb = y[int(round(mean_channel))]
#
#    FWHM = 2*np.sqrt(2*np.log(2))*std
##    FWHMint = int(round(FWHM))
##    FWHM = FWHMint
#
#    FWHM_x = [mean-FWHM/2 + einchannel/2 - 0.015, mean+FWHM/2]
##    FWHM_y = [gauss(mean, *params)/2, gauss(mean, *params)/2]
#    FWHM_y = [counthwb/2, counthwb/2]
#
#    FWTM = 2*np.sqrt(2*np.log(10))*std
##    FWTMint = int(round(FWTM))
##    FWTM = FWTMint
#
#    FWTM_x = [mean-FWTM/2 - einchannel/2 + 0.025, mean+FWTM/2 - einchannel/2 + 0.06]
##    FWTM_y = [gauss(mean, *params)/10, gauss(mean, *params)/10]
#    FWTM_y = [counthwb/10, counthwb/10]
#    hwb = steigung * 10# + yachse
#    zwb = steigung * 19# + yachse
#
#    print('----------------------------')
#    print('FWHM Fit: ' + str(FWHM))
#    print('FWTM Fit: ' + str(FWTM))
#    print(FWHM/FWTM)
##    print(np.sqrt(np.log(2)/np.log(10)))
#    print('----------------------------')
#
#    print('----------------------------')
#    print('FWHM Daten: ' + str(hwb))
#    print('FWTM Daten: ' + str(zwb))
#    print(hwb/zwb)
##    print(np.sqrt(np.log(2)/np.log(10)))
#    print('----------------------------')
#
##### Plot Halbwertsbreite, Zehntelwertsbreite
#    ax.plot(FWHM_x, FWHM_y, '-', color='C3')
#    ax.annotate((xy)=(mean -0.5, gauss(mean, *params)/2 +2) , fontsize= 12, color='C3', s='Halbwertsbreite: \n10 Channel \n2.07 keV ' , rotation=0)
##    ax.axvspan(mean-FWHM/2, mean+FWHM/2, facecolor='C2', alpha=0.1)
#    ax.plot(FWTM_x, FWTM_y, '-', color='C3')
#    ax.annotate((xy)=(mean -0.5, gauss(mean, *params)/10 +5) , fontsize=12, color='C3', s='Zehntelwertsbreite: \n19 Channel \n3.94 keV ', rotation=0)

#### Plot Daten
    ax.fill_between(tmp_x, 0, tmp_y, step='mid', alpha=0.4)
    ax.plot(tmp_x, tmp_y, 'x', color='C0', drawstyle='steps', markersize=8, markeredgewidth=2, label='Daten')

#### Plot Fit
    x_new = np.linspace(tmp_x[0], tmp_x[-1], 5000, endpoint=True)
    ax.plot(x_new,gauss(x_new,*params),'-', color='C1', label='Normalverteilung')

#    ax.plot(x_new,gauss(x_new, amp, mean, std, off),'-', color='C2', label='probe')


#    ax.set_ylim(top=100, bottom=0)
#    ax.set_xlim(-200, 400)

    plt.grid(alpha=0.3)
    ax.legend(fancybox=True, ncol=1)
    ax.set_xlabel('Energie in keV', labelpad=2)
    ax.set_ylabel('Häufigkeit', labelpad=8)

    plt.savefig('bananium_peak_%s.pdf' %peakno)

def cutDataArrayBetweenTwoValues(countingup, beingcut, uG, oG): # cuts off data from array before start and after stop of measurement // schneidet am Array die Werte vor und nach der Messung ab
        ############################## takeListsMakeArrays calling cutDataArrayBetweenTwoValues
    A = []                                                                              # hier wird abgespeichert
    for i in range(len(countingup)):                                                          # für alle Indices in der Liste date
        if countingup[i] >= uG and countingup[i] <= oG:                      # wenn der Wert von date beim Index kleiner ist als der start oder größer ist als der stop
            A.append(beingcut[i])                                                              # speichere den Wert von dem Datensatz in A
        else:
            pass

    return (A)

def fillYarray(allecounts, channelabgeschnitten):
    resultarr = []
    for i in range(len(allecounts)):    # zählt den Index der Counts hoch
        for j in range(len(channelabgeschnitten)):     # zählt den Index der abgeschnittenen Energie hoch
            if ( i == channelabgeschnitten[j]):
                resultarr.append(allecounts[i])
            else:
                pass
    return(resultarr)

def fitgerade(ax, x, y, color, width, name):
    def f(x,a,b):
        return a*x+b

    params,var = curve_fit(f,x,y, maxfev=10000)
    fehler = np.sqrt(np.diag(var))

    x_new = np.linspace(x[0], x[-1], 5000, endpoint=True)
    ax.plot(x_new,f(x_new,*params),'-', linewidth=2, color=color, label='Fit - %s' %name)

    dashed = np.linspace(x[0]-width, x[-1]+width, 5000, endpoint=True)
    ax.plot(dashed,f(dashed,*params), linestyle='dashed', linewidth=2, color=color)

    print('----------------------------')
    print('Gerade %s' %name)
    print(params)
    print(fehler)
    print('----------------------------')

    return(params, fehler)

def lighten_color(color, amount=0.5):
    import matplotlib.colors as mc
    import colorsys
    try:
        c = mc.cnames[color]
    except:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    return colorsys.hls_to_rgb(c[0], 1 - amount * (1 - c[1]), c[2])

def kontinuum(x, y, peaks_x, peakno, width, amp, off, left, right, steigung, yachse, channelkomplett):
    fig, ax = plt.subplots()

#### Compton-Kontinuum - Daten
    tmp_x, mean, sigma = channel(x, y, peaks_x, peakno, width, left, right)
    tmp_y, total = counts(x, y, peaks_x, peakno, width, left, right)

#### Compton-Kontinuum - Plots
    C0light = lighten_color('C0', 0.3)
    C0mid = lighten_color('C0', 0.65)
    ax.fill_between(tmp_x, 0, tmp_y, color=C0light, step='mid')#, alpha=0.4)
    #ax.plot(tmp_x, tmp_y, '-', linewidth=0.0000000000000001, color=C0light, drawstyle='steps', markersize=8, markeredgewidth=2)
    ax.plot(tmp_x, tmp_y, 'x', color=C0mid, drawstyle='steps', markersize=3, markeredgewidth=1, label='Daten')

#### Arrays für die beiden Geraden-Fits
    arrlinks_x = cutDataArrayBetweenTwoValues(channelkomplett, channelkomplett, 1700, 2250)
    arrlinks_y = fillYarray(y, arrlinks_x)
    arrrechts_x = cutDataArrayBetweenTwoValues(channelkomplett, channelkomplett, 2100, 2400)
    arrrechts_y = fillYarray(y, arrrechts_x)

    tmp = []
    for i in range(len(arrlinks_x)):
        energie = steigung*arrlinks_x[i] + yachse
        tmp.append(energie)
    arrlinks_x = tmp

    tmp = []
    for i in range(len(arrrechts_x)):
        energie = steigung*arrrechts_x[i] + yachse
        tmp.append(energie)
    arrrechts_x = tmp


    import matplotlib.transforms as mtransforms
    trans = mtransforms.blended_transform_factory(ax.transData, ax.transAxes)
    ax.fill_between(arrlinks_x, 0, 1, facecolor='C1', alpha=0.1, transform=trans)
    ax.fill_between(arrrechts_x, 0, 1, facecolor='C3', alpha=0.1, transform=trans)

#### Beide Geraden-Fits
    paramslinks, fehlerlinks = fitgerade(ax, arrlinks_x, arrlinks_y, 'C1', steigung*350, 'links')
    paramsrechts, fehlerrechts = fitgerade(ax, arrrechts_x, arrrechts_y, 'C3', steigung*145, 'rechts')

    alinks = ufloat (paramslinks[0], fehlerlinks[0])
    blinks = ufloat (paramslinks[1], fehlerlinks[1])
    arechts = ufloat (paramsrechts[0], fehlerrechts[0])
    brechts = ufloat (paramsrechts[1], fehlerrechts[1])

    print('----------------------------')
    print('Schnittpunkt der Geraden (Compton-Kante) in keV')
    intersection = (brechts-blinks)/(alinks-arechts)
    print(intersection)
#    steigung = ufloat(0.20725824, 4.28713921e-05)
#    yachse = ufloat(-1.22364356, 1.66905256e-01)
#    E_chann = steigung*intersection+yachse
#    print(E_chann)

    print('Compton-Kante mit Literaturwert in keV')
    E_lit = ufloat(661.657, 0.003) #aus nucleide
    E = E_lit*1e03*const.elementary_charge
    eps = E/(const.electron_mass*const.c**2)
    theo = E*2*eps/(1+2*eps)
    print(theo/(const.elementary_charge*1e03))

    peaks_x = [0]
    tmp_x, mean, sigma = channel(x, y, peaks_x, peakno, 1, 0, 450)
    tmp_y, total = counts(x, y, peaks_x, peakno, 1, 0, 450)
#    ax.plot(tmp_x, tmp_y, 'x', color='C4', drawstyle='steps', markersize=3, markeredgewidth=1, label='Daten')

#    print('Inhalt Kontinuum!: ' + str(total))
    print('Inhalt: ' + str(total-off))        # Peak-Inhalt
    print('Fehler Inhalt: ' + str(np.sqrt(total-off)))   # Fehler Peak-Inhalt


    plt.grid(alpha=0.3)
    ax.legend(fancybox=True, ncol=1)
    ax.set_xlabel('Energie in keV', labelpad=2)
    ax.set_ylabel('Häufigkeit', labelpad=8)




    plt.savefig('bananium_kontinuum.pdf')

def rueckstreupeak(x, y, peaks_x, peakno, width, amp, off, left, right, steigung, yachse, channelkomplett):
        fig, ax = plt.subplots()

    #### Compton-Kontinuum - Daten
        tmp_x, mean, sigma = channel(x, y, peaks_x, peakno, width, left, right)
        tmp_y, total = counts(x, y, peaks_x, peakno, width, left, right)

    #### Compton-Kontinuum - Plots
        C0light = lighten_color('C0', 0.3)
        C0mid = lighten_color('C0', 0.65)
        ax.fill_between(tmp_x, 0, tmp_y, color=C0light, step='mid')#, alpha=0.4)
        #ax.plot(tmp_x, tmp_y, '-', linewidth=0.0000000000000001, color=C0light, drawstyle='steps', markersize=8, markeredgewidth=2)
        ax.plot(tmp_x, tmp_y, 'x', color=C0mid, drawstyle='steps', markersize=3, markeredgewidth=1, label='Daten')

    #### Arrays für die beiden Geraden-Fits
        var = 927
        arrlinks_x = cutDataArrayBetweenTwoValues(channelkomplett, channelkomplett, var-130, var+20)
        arrlinks_y = fillYarray(y, arrlinks_x)
        arrrechts_x = cutDataArrayBetweenTwoValues(channelkomplett, channelkomplett, var-20, var+130)
        arrrechts_y = fillYarray(y, arrrechts_x)

        tmp = []
        for i in range(len(arrlinks_x)):
            energie = steigung*arrlinks_x[i] + yachse
            tmp.append(energie)
        arrlinks_x = tmp

        tmp = []
        for i in range(len(arrrechts_x)):
            energie = steigung*arrrechts_x[i] + yachse
            tmp.append(energie)
        arrrechts_x = tmp


        import matplotlib.transforms as mtransforms
        trans = mtransforms.blended_transform_factory(ax.transData, ax.transAxes)
        ax.fill_between(arrlinks_x, 0, 1, facecolor='C1', alpha=0.1, transform=trans)
        ax.fill_between(arrrechts_x, 0, 1, facecolor='C3', alpha=0.1, transform=trans)

    #### Beide Geraden-Fits
        paramslinks, fehlerlinks = fitgerade(ax, arrlinks_x, arrlinks_y, 'C1', steigung*60, 'links')
        paramsrechts, fehlerrechts = fitgerade(ax, arrrechts_x, arrrechts_y, 'C3', steigung*60, 'rechts')

        alinks = ufloat (paramslinks[0], fehlerlinks[0])
        blinks = ufloat (paramslinks[1], fehlerlinks[1])
        arechts = ufloat (paramsrechts[0], fehlerrechts[0])
        brechts = ufloat (paramsrechts[1], fehlerrechts[1])

        print('----------------------------')
        print('Schnittpunkt der Geraden (Rückstreupeak) in keV')
        intersection = (brechts-blinks)/(alinks-arechts)
        print(intersection)
    #    steigung = ufloat(0.20725824, 4.28713921e-05)
    #    yachse = ufloat(-1.22364356, 1.66905256e-01)
    #    E_chann = steigung*intersection+yachse
    #    print(E_chann)


#        print('Compton-Kante mit Literaturwert in keV')
#        E_lit = ufloat(661.657, 0.003) #aus nucleide
#        E = E_lit*1e03*const.elementary_charge
#        eps = E/(const.electron_mass*const.c**2)
#        theo = E*2*eps/(1+2*eps)
#        print(theo/(const.elementary_charge*1e03))

        plt.grid(alpha=0.3)
        ax.legend(fancybox=True, ncol=1)
        ax.set_xlabel('Energie in keV', labelpad=2)
        ax.set_ylabel('Häufigkeit', labelpad=8)

        plt.savefig('bananium_rueckstreupeak.pdf')

def plot(x, y, filename):
    fig, ax = plt.subplots()
    plt.yscale('log')

    ax.plot(x, y, '-', linewidth=0.0000000000000001, color='C0', drawstyle='steps', markersize=8, markeredgewidth=2, label='Unkorrigierte Daten %s' %filename)

    a, b = np.loadtxt('1501_diffus.txt', unpack=True,delimiter=' , ')
    z = y-b
    ax.plot(x, z, '-', linewidth=0.0000000000000001, color='C1', drawstyle='steps', markersize=8, markeredgewidth=2, label='Korrigierte Daten (diffus) %s' %filename)



    a = 0.5729673448571527
    m = []
    for i in range(len(x)):
        if (x[i] <= 0.5729673448571527):
            tmp = y[i] * (np.sin(x[i]))/(np.sin(a))
            m.append(tmp)
        else:
            tmp = y[i]
            m.append(tmp)
    ax.plot(x, m, '-', linewidth=0.0000000000000001, color='C2', drawstyle='steps', markersize=8, markeredgewidth=2, label='Korrigiert um Geometriefaktor %s' %filename)


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
    filename = 'Diffus'

    x, y = np.loadtxt('1501_diffus.txt', unpack=True,delimiter=' , ')

    plot(x, y, filename)


    print('--- done ---')
