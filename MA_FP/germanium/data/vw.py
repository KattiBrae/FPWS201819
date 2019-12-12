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

plt.rcParams['figure.figsize'] = (10, 7)
plt.rcParams['font.size'] = 16
plt.rcParams['lines.linewidth'] = 2

counts = np.loadtxt('europium.txt', unpack=True,delimiter=' ')
channel = np.arange(0, len(counts), 1 )
error=np.sqrt(counts)

E, P = np.loadtxt('europium_literatur.txt', unpack=True,delimiter=' , ')

peaks_channel = [  594,  1187, 1667, 1988, 2149, 3765, 4655, 5245, 5371, 6801]

peaks_counts = []
for i in range(len(channel)):
    for j in range(len(peaks_channel)):
        if ( i == peaks_channel[j]):
            peaks_counts.append(counts[i])
        else:
            pass


gaussdata = []
sigma = []
for j in range(len(peaks_channel)):
    for i in range(len(channel)):
        if ( (j == 0) and ( channel[i] <= peaks_channel[j]-50) and (channel[i] >= peaks_channel[j]+50) ):
            gaussdata.append(channel[i])
#        elif ( (j > 0) and (j < 9) and (channel[i] >= (peaks_channel[j] - peaks_channel[j-1])/2) and (channel[i] <= peaks_channel[j] + (peaks_channel[j+1]-peaks_channel[j])/2 )):
#            gaussdata.append(channel[i])
#        elif ( (j == 9) and ( channel[i] >= (peaks_channel[j] - (peaks_channel[j]-peaks_channel[j-1])/2)) and (channel[i] <= peaks_channel[j] + (peaks_channel[j] - peaks_channel[j-1])/2) ):
#            gaussdata.append(channel[i])
        else:
            pass
    mean,std=norm.fit(gaussdata)
    sigma.append(std)
    plt.plot(gaussdata, norm.pdf(gaussdata/max(peaks_channel), scale=peaks_channel[j]), loc=sigma[j], color='red', linewidth=1)
    gaussdata = []
print(sigma)


plt.plot(channel, counts, '-', linewidth='1', color='C0', label='Daten')
plt.plot(peaks_channel, peaks_counts, 'x', markersize='10', markeredgewidth='2', color='C1', label='Peaks')
#plt.yscale('log')

plt.legend(fancybox=True, ncol=1)
plt.xlabel('rel. Channel, rel. Energie', labelpad=2)
plt.ylabel('Häufigkeit', labelpad=8)

plt.grid()
plt.savefig('vollenergienachweiswahrscheinlichkeit.pdf')
