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
#    print(mean, sigma)
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



    def gaus(x,a,mu,std,c):
        return a/(2*const.pi*std**2) * np.exp(-(x-mu)**2/(2*std**2))+c

    params,var = curve_fit(gaus,x,y,p0=[amp,mean,sigma,off], maxfev=5000)
    fehler = np.sqrt(np.diag(var))
    #print(params, fehler)



    plt.grid()

    x_new = np.linspace(tmp_x[0], tmp_x[-1], 5000, endpoint=True)
#    ax.step(tmp_x,tmp_y, where='mid', color='C0', alpha=0.6)
    ax.fill_between(tmp_x, 0, tmp_y, step='mid', alpha=0.4)
    ax.plot(tmp_x, tmp_y, 'x', color='C0', drawstyle='steps', markersize=8, markeredgewidth=2)
    ax.plot(x_new,gaus(x_new,*params),'-', color='C1', label='Fit - Normalverteilung')

    ax.legend(fancybox=True, ncol=1)
    ax.set_xlabel('Channel', labelpad=2)
    ax.set_ylabel('Häufigkeit', labelpad=8)


    plt.savefig('einzelnergaussfit_%s.pdf' %peakno)

#    print(total-off)        # Peak-Inhalt
#    print(np.sqrt(total-off))   # Fehler Peak-Inhalt

def vollE(E, Q, dQ):

    def f(E,a,b,c):
        return a*E**(b)+c

    params,var = curve_fit(f,E,Q, p0=[7,-1,0], maxfev=5000)
    fehler = np.sqrt(np.diag(var))
    print(params, fehler)



    x_new = np.linspace(E[0], E[-1], 5000, endpoint=True)
    plt.plot(x_new,f(x_new,*params),'-', color='C1', label='Ausgleichsrechnung nach: $Q = aE^{b}+c$')
    plt.errorbar(E, Q, yerr=dQ, fmt="none", capsize=5, capthick=1, ms=5, color='C2', label='Unsicherheit')
    plt.plot(E, Q, 'x', markersize=8, markeredgewidth=2, label='Daten')


    plt.legend(fancybox=True, ncol=1)
    plt.xlabel('$E$ in keV', labelpad=2)
    plt.ylabel('$Q$', labelpad=8)

    plt.grid()

    plt.savefig('vollenergienachweiswahrscheinlichkeit.pdf')



if __name__=="__main__":
    import numpy as np
    import sympy
    import matplotlib.pyplot as plt
    import matplotlib.patches as mpatches
    from matplotlib import transforms
    from matplotlib import rc
    from scipy.optimize import curve_fit
    from pylab import figure, axes, pie, title, show
    from numpy import NaN, Inf, arange, isscalar, asarray, array
    import sys
    import scipy.signal as sig
    from scipy.stats import norm
    import scipy.constants as const
    import uncertainties
    import uncertainties.unumpy as unp
    from uncertainties import ufloat
    from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)
    from math import exp, log, sin, atan


    plt.rcParams['figure.figsize'] = (10, 7)
    plt.rcParams['font.size'] = 16
    plt.rcParams['lines.linewidth'] = 2

    y = np.loadtxt('europium.txt', unpack=True,delimiter=' ')
    x = np.arange(0, len(y), 1 )
    peaks_x = [  594,  1187, 1667, 1988, 2149, 3765, 4655, 5245, 5371, 6801]
    peakno = np.arange(0, len(peaks_x), 1 )

    peaks_counts = []
    for i in range(len(x)):
        for j in range(len(peaks_x)):
            if ( i == peaks_x[j]):
                peaks_counts.append(y[i])
            else:
                pass


    #gaussfit(x, y, peaks_x, 0, 10,   0, 30, 1, -1)
    #gaussfit(x, y, peaks_x, 1, 10,   0, 15, 0, -1)
    #gaussfit(x, y, peaks_x, 2, 11,   0, 15, 2, -1)
    #gaussfit(x, y, peaks_x, 3, 10,   0, 10, 4, -2)
    #gaussfit(x, y, peaks_x, 4, 11,   0, 10, 0, -3)
    #gaussfit(x, y, peaks_x, 5, 15,   0,  1, 0, -3)
    #gaussfit(x, y, peaks_x, 6, 14,   0,  1, 2, +1)
    #gaussfit(x, y, peaks_x, 7, 13,   0,  1, 0, -1)
    #gaussfit(x, y, peaks_x, 8, 15,   0,  1, 0, -1)
    #gaussfit(x, y, peaks_x, 9, 20,   0,  1, 0, -6)

    E, possibility = np.loadtxt('europium_literatur.txt', unpack=True,delimiter=' , ')
    Q, dQ = np.loadtxt('Q.txt', unpack=True, delimiter=',')

#    Q = []
#    for i in range(len(tmp)):
#        Q.append(ufloat(tmp[i], dtmp[i]))
#    print(Q)

    vollE(E, Q, dQ)


    print('--- done ---')

#peaks_channel = [  594,  1187, 1667, 1988, 2149, 3765, 4655, 5245, 5371, 6801]
#
#peaks_counts = []
#for i in range(len(channel)):
#    for j in range(len(peaks_channel)):
#        if ( i == peaks_channel[j]):
#            peaks_counts.append(counts[i])
#        else:
#            pass
#
#
#gaussdata = []
#sigma = []
#for j in range(len(peaks_channel)):
#    for i in range(len(channel)):
#        if ( (j == 0) and ( channel[i] <= peaks_channel[j]-50) and (channel[i] >= peaks_channel[j]+50) ):
#            gaussdata.append(channel[i])
##        elif ( (j > 0) and (j < 9) and (channel[i] >= (peaks_channel[j] - peaks_channel[j-1])/2) and (channel[i] <= peaks_channel[j] + (peaks_channel[j+1]-peaks_channel[j])/2 )):
##            gaussdata.append(channel[i])
##        elif ( (j == 9) and ( channel[i] >= (peaks_channel[j] - (peaks_channel[j]-peaks_channel[j-1])/2)) and (channel[i] <= peaks_channel[j] + (peaks_channel[j] - peaks_channel[j-1])/2) ):
##            gaussdata.append(channel[i])
#        else:
#            pass
#    mean,std=norm.fit(gaussdata)
#    sigma.append(std)
#    plt.plot(gaussdata, norm.pdf(gaussdata/max(peaks_channel), scale=peaks_channel[j]), loc=sigma[j], color='red', linewidth=1)
#    gaussdata = []
#print(sigma)
#
#
#plt.plot(channel, counts, '-', linewidth='1', color='C0', label='Daten')
#plt.plot(peaks_channel, peaks_counts, 'x', markersize='10', markeredgewidth='2', color='C1', label='Peaks')
##plt.yscale('log')
#
#plt.legend(fancybox=True, ncol=1)
#plt.xlabel('rel. Channel, rel. Energie', labelpad=2)
#plt.ylabel('Häufigkeit', labelpad=8)
#
#plt.grid()
#plt.savefig('vollenergienachweiswahrscheinlichkeit.pdf')
#
