#def channelrange(y, channel, peaks_channel, peakno):
#    tmp_channel = []
#    for j in range(len(peaks_channel)):
#        if (j == peakno):
#            for i in range(len(y)):
#                if (channel[i] >= peaks_channel[j]-10) and (channel[i] <= peaks_channel[j]+10):
#                    tmp_channel.append(channel[i])
#                else:
#                    pass
#    return(tmp_channel)
#
#def countrange(y, channel, peaks_channel, peakno):
#    tmp_y = []
#    for j in range(len(peaks_channel)):
#        if (j == peakno):
#            for i in range(len(y)):
#                if (channel[i] >= peaks_channel[j]-10) and (channel[i] <= peaks_channel[j]+10):
#                    tmp_y.append(y[i])
#                else:
#                    pass
#        mean = np.mean(tmp_y)
#        sigma = np.std(tmp_y)
#
#    return(tmp_y)
#
#def mean(y, channel, peaks_channel, peakno):
#    tmp_y = []
#    for j in range(len(peaks_channel)):
#        if (j == peakno):
#            for i in range(len(y)):
#                if (channel[i] >= peaks_channel[j]-10) and (channel[i] <= peaks_channel[j]+10):
#                    tmp_y.append(y[i])
#                else:
#                    pass
#        mean = np.mean(tmp_y)
#        sigma = np.std(tmp_y)
#
#    return(mean)
#
#def sigma(y, channel, peaks_channel, peakno):
#    tmp_y = []
#    for j in range(len(peaks_channel)):
#        if (j == peakno):
#            for i in range(len(y)):
#                if (channel[i] >= peaks_channel[j]-10) and (channel[i] <= peaks_channel[j]+10):
#                    tmp_y.append(y[i])
#                else:
#                    pass
#        mean = np.mean(tmp_y)
#        sigma = np.std(tmp_y)
#
#    return(sigma)
#
#def gaussfit(x, y, peaks_channel, mean, sigma):
#    def gaus(x,a,x0,sigma):
#        return a*exp(-(x-x0)**2/(2*sigma**2))
#
#    params,var = curve_fit(gaus,x,y,p0=[1,mean,sigma])
#    fehler = np.sqrt(np.diag(var))
#
#    x_new = np.linspace(x[0], x[-1], 5000, endpoint=True)
#    plt.plot(x_new,gaus(x_new,*params),'-', color='C1', alpha=0.6)
#









#if __name__=="__main__":
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

y = np.loadtxt('europium.txt', unpack=True,delimiter=' ')
x = np.arange(0, len(y), 1 )
peaks_x = [  594]#  1187, 1667, 1988, 2149, 3765, 4655, 5245, 5371, 6801]
peakno = np.arange(0, len(peaks_x), 1 )

#xerster = np.vectorize(xrange(y, x, peaks_x, 1))
#yerster = np.vectorize(countrange(y, x, peaks_x, 1))
#gaussfit(xerster, yerster, peaks_x, mean(y, x, peaks_x, 1), sigma(y, x, peaks_x, 1))


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



tmp_x = []
for j in range(len(peaks_x)):
    if (j == peakno):
        for i in range(len(y)):
            if (x[i] >= peaks_x[j]-15) and (x[i] <= peaks_x[j]+15):
                tmp_x.append(x[i])
            else:
                pass
    mean = np.mean(tmp_x)
    sigma = np.std(tmp_x)

tmp_y = []
for j in range(len(peaks_x)):
    if (j == peakno):
        for i in range(len(y)):
            if (x[i] >= peaks_x[j]-15) and (x[i] <= peaks_x[j]+15):
                tmp_y.append(y[i])
            else:
                pass
print(mean, sigma)

def gaus(x,a,mu,std,c):
    return a/(2*const.pi*std**2) * np.exp(-(x-mu)**2/(2*std**2))+c

params,var = curve_fit(gaus,x,y,p0=[500,mean,sigma,30])
fehler = np.sqrt(np.diag(var))

plt.plot(tmp_x, tmp_y)
x_new = np.linspace(tmp_x[0], tmp_x[-1], 5000, endpoint=True)
plt.plot(x_new,gaus(x_new,*params),'-', color='C1', alpha=0.6)

plt.savefig('try.pdf')


#plt.plot(x_array, count_array, 'x', color='red',)
#mean,std=norm.fit(count_array)
