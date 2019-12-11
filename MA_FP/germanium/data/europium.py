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

plt.rcParams['figure.figsize'] = (15, 10)
plt.rcParams['font.size'] = 16
plt.rcParams['lines.linewidth'] = 2


counts = np.loadtxt('europium.txt', unpack=True,delimiter=' ')
channel = np.arange(0, len(counts), 1 )
error=np.sqrt(counts)



E, P = np.loadtxt('europium_literatur.txt', unpack=True,delimiter=' , ')


#peaks = sig.find_peaks(counts, prominence = 10)
#print(peaks)
E_norm = E/max(E)

peaks_channel_norm = []
#peaks_channel = [  64,  198,  200,  224,  594,  726, 1187, 1667, 1988, 2146, 2149, 3765, 4655, 5245, 5368, 5371, 5374, 6801]
peaks_channel = [  594,  1187, 1667, 1988, 2149, 3765, 4655, 5245, 5371, 6801]
for b in peaks_channel:
    peaks_channel_norm.append(b/max(peaks_channel))

peaks_counts = []
for i in range(len(channel)):
    for j in range(len(peaks_channel)):
        if ( i == peaks_channel[j]):
            peaks_counts.append(counts[i])
        else:
            pass




plt.plot(E_norm, np.zeros(len(E),)-40, 'x', markersize='10', markeredgewidth='2', color='C2', label='Literaturwerte')
plt.plot(channel/max(peaks_channel), counts, '-', linewidth='1', color='C0', label='Daten')
#plt.errorbar(channel, counts, yerr=error, fmt="none", capsize=5, capthick=1, ms=5, color='C2', label='Unsicherheit')
plt.plot(peaks_channel_norm, peaks_counts, 'x', markersize='10', markeredgewidth='2', color='C1', label='Peaks')
#plt.plot(peaks_channel_norm, np.zeros(len(peaks_counts)), 'x', markersize='10', markeredgewidth='2', color='C1')

for i in range(len(peaks_channel_norm)):
    if (i == 3) or (i == 7):
        plt.annotate((xy)=(-0.04+E_norm[i], 60+peaks_counts[i]), s='%.1f keV' %E[i], fontsize=11,)
    elif (i == 4) or (i == 8):
        plt.annotate((xy)=(-0.015+E_norm[i], 20+peaks_counts[i]), s='%.1f keV' %E[i], fontsize=11,)
    else:
        plt.annotate((xy)=(-0.025+E_norm[i], 20+peaks_counts[i]), s='%.1f keV' %E[i], fontsize=11,)








plt.legend(fontsize=11, fancybox=True, loc='upper right', ncol=1)                                  # schiebt die Legende in die obere linke Ecke
plt.xlabel('rel. Channel, rel. Energie', labelpad=2)                                                            # Label x-Achse
plt.ylabel('Häufigkeit', labelpad=8)                     # Label Oberflächenspannung
#plt.yscale('log')

plt.grid()                                                                                          # Gitternetz
plt.savefig('spektrum_europium.pdf')



#def f(channel,a,b,c):
#    return a*np.exp(-b*channel)+c
#params, var = curve_fit(f, channel, counts)
#fehler = np.sqrt(np.diag(var))
#print('parameter, fehler')
#print(params, fehler)
#x_new = np.linspace(channel[0], channel[-1], 5000)
#plt.plot(x_new,f(x_new,*popt),'-', label='Ausgleichsrechnung ' r'$\propto e^{-\lambda t}$')





#(array([  64,  198,  200,  224,  594,  726, 1187, 1667, 1988, 2146, 2149, 3765, 4655, 5245, 5368, 5371, 5374, 6801]),
#       {'prominences': array([  56.,   70.,   70.,   51., 1219.,   30.,  193.,  371.,   41., 43.,   43.,   66.,   41.,   32.,   33.,   33.,   33.,   37.]),
#       'left_bases': array([  50,   50,   50,  216,   50,  652, 1140, 1353, 1797, 1797, 1797, 3670, 4634, 5229, 5345, 5345, 5345, 6774]),
#       'right_bases': array([ 179,  281,  281,  281, 1797, 1140, 1353, 1797, 2010, 2506, 2506, 3820, 4671, 5280, 5388, 5388, 5388, 6816])})
