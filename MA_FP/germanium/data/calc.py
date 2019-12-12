def channelrange(counts, channel, peaks_channel, peakno):
    tmp_channel = []
    for j in range(len(peaks_channel)):
        if (j == peakno):
            for i in range(len(counts)):
                if (channel[i] >= peaks_channel[j]-10) and (channel[i] <= peaks_channel[j]+10):
                    tmp_channel.append(channel[i])
                else:
                    pass
    return(tmp_channel)

def countrange(counts, channel, peaks_channel, peakno):
    tmp_counts = []
    for j in range(len(peaks_channel)):
        if (j == peakno):
            for i in range(len(counts)):
                if (channel[i] >= peaks_channel[j]-10) and (channel[i] <= peaks_channel[j]+10):
                    tmp_counts.append(counts[i])
                else:
                    pass
        mean = np.mean(tmp_counts)
        sigma = np.std(tmp_counts)

    return(tmp_counts)

def mean(counts, channel, peaks_channel, peakno):
    tmp_counts = []
    for j in range(len(peaks_channel)):
        if (j == peakno):
            for i in range(len(counts)):
                if (channel[i] >= peaks_channel[j]-10) and (channel[i] <= peaks_channel[j]+10):
                    tmp_counts.append(counts[i])
                else:
                    pass
        mean = np.mean(tmp_counts)
        sigma = np.std(tmp_counts)

    return(mean)

def sigma(counts, channel, peaks_channel, peakno):
    tmp_counts = []
    for j in range(len(peaks_channel)):
        if (j == peakno):
            for i in range(len(counts)):
                if (channel[i] >= peaks_channel[j]-10) and (channel[i] <= peaks_channel[j]+10):
                    tmp_counts.append(counts[i])
                else:
                    pass
        mean = np.mean(tmp_counts)
        sigma = np.std(tmp_counts)

    return(sigma)

def gaussfit(x, y, peaks_channel, mean, sigma):
    def gaus(x,a,x0,sigma):
        return a*exp(-(x-x0)**2/(2*sigma**2))

    params,var = curve_fit(gaus,x,y,p0=[1,mean,sigma])
    fehler = np.sqrt(np.diag(var))

    x_new = np.linspace(x[0], x[-1], 5000, endpoint=True)
    plt.plot(x_new,gaus(x_new,*params),'-', color='C1', alpha=0.6)










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

    counts = np.loadtxt('europium.txt', unpack=True,delimiter=' ')
    channel = np.arange(0, len(counts), 1 )
    peaks_channel = [  594,  1187, 1667, 1988, 2149, 3765, 4655, 5245, 5371, 6801]

    xerster = np.vectorize(channelrange(counts, channel, peaks_channel, 1))
    yerster = np.vectorize(countrange(counts, channel, peaks_channel, 1))
    gaussfit(xerster, yerster, peaks_channel, mean(counts, channel, peaks_channel, 1), sigma(counts, channel, peaks_channel, 1))

    plt.savefig('try.pdf')

#t = ufloat(605484000, 54000)
#hwz = ufloat(426.7e+06, 5e+06)
#B = ufloat(4130, 60)
#m = log(2)
#
#A = B*unp.exp(-m/hwz*t)
##print(A)
#
#r=22.5e-03
#h=65e-03
#
#Omega =  sin(1/4 * atan(r/h))**2
##print(Omega)







#plt.plot(channel_array, count_array, 'x', color='red',)
#mean,std=norm.fit(count_array)
