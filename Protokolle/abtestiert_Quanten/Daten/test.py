
import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Graphik1')
print('Steigung','Y-Achsenabschnitt')
x, y = np.loadtxt('A1L1x50mmF5000-14000S2.dat', unpack=True,delimiter=' ')

#def f(x,a,b):
#    return a*x+b
#popt, pcov = curve_fit(f, x, y)
#print(popt)
#print(np.diag(pcov))
#
#x_new = np.linspace(x[0], x[-1], 500)

#import numpy as np
#from scipy.signal import find_peaks_cwt
#cb = np.array([0, 90 ])
#indexes = find_peaks_cwt(cb, np.arange(1, 14000))

#import numpy as np
#from peakdetect import peakdetect
#cb = np.array([0,90 ])
#peaks = peakdetect(cb, lookahead=100)

#import numpy as np
#from oct2py import octave
#cb = np.array([0,90 ])
#octave.eval("pkg load signal")
#(peaks, indexes) = octave.findpeaks(cb, 'DoubleSided', 'MinPeakHeight', 0.04, 'MinPeakDistance', 100, 'MinPeakWidth', 0)
#
#import numpy as np
#import peakutils
#cb = np.array([-0.010223, ... ])
#indexes = peakutils.indexes(cb, thres=0.02/max(cb), min_dist=100)

#import numpy as np
#from detect_peaks import detect_peaks
#cb = np.array([-0.010223, ... ])
#indexes = detect_peaks(cb, mph=0.04, mpd=100)


#import numpy as np
#import peakutils
#cb = np.array([-0.010223, ... ])
#indexes = peakutils.indexes(cb, thres=0.02/max(cb), min_dist=100)
## [ 333  693 1234 1600]
#
#interpolatedIndexes = peakutils.interpolate(range(0, len(cb)), cb, ind=indexes)
## [  332.61234263   694.94831376  1231.92840845  1600.52446335]

import numpy as np
from vector import vector, plot_peaks
from libs import detect_peaks
print('Detect peaks with minimum height and distance filters.')
indexes = detect_peaks.detect_peaks(vector, mph=7, mpd=2)
print('Peaks are: %s' % (indexes))

plt.figure(1)
plt.plot(x,y,'x')
#plt.peaks()
#plt.plot(x_new,f(x_new,*popt),'-', label='Lineare Regression')
plt.xlabel('Frequenz')
plt.ylabel('Intensität')
plt.grid()
#plt.legend()




plt.savefig('A1L1x50mmF5000-14000S2.pdf')
print ('Fertig')
