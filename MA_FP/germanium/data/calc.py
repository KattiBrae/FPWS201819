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


t = ufloat(605484000, 54000)
hwz = ufloat(426.7e+06, 5e+06)
B = ufloat(4130, 60)
m = log(2)

A = B*unp.exp(-m/hwz*t)
#print(A)

r=22.5e-03
h=65e-03

Omega =  sin(1/4 * atan(r/h))**2
#print(Omega)

counts = np.loadtxt('europium.txt', unpack=True,delimiter=' ')
channel = np.arange(0, len(counts), 1 )
peaks_channel = [  594,  1187, 1667, 1988, 2149, 3765, 4655, 5245, 5371, 6801]

#tmp = []
#for j in range(len(peaks_channel)):
#    for i in range(len(counts)):
#        if (channel[i] >= peaks_channel[j]-50) and (channel[i] <= peaks_channel[j]+50):
#            tmp.append(counts[i])
#        else:
#            pass
#    print(tmp)
#    tmp = []

tmp = []
for j in range(len(peaks_channel)):
    for i in range(len(counts)):
        if (channel[i] >= peaks_channel[j]-50) and (channel[i] <= peaks_channel[j]+50):
            tmp.append(channel[i])
        else:
            pass
    print(tmp)
    tmp = []

channel_array = [544, 545, 546, 547, 548, 549, 550, 551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572, 573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594, 595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616, 617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 640, 641, 642, 643, 644]
count_array = [22.0, 30.0, 30.0, 20.0, 28.0, 26.0, 25.0, 21.0, 30.0, 34.0, 36.0, 32.0, 30.0, 21.0, 31.0, 24.0, 34.0, 28.0, 26.0, 29.0, 25.0, 36.0, 29.0, 33.0, 31.0, 30.0, 36.0, 34.0, 33.0, 38.0, 36.0, 36.0, 27.0, 32.0, 34.0, 31.0, 36.0, 35.0, 41.0, 28.0, 22.0, 32.0, 43.0, 82.0, 130.0, 227.0, 418.0, 652.0, 965.0, 1101.0, 1219.0, 1071.0, 861.0, 598.0, 386.0, 221.0, 123.0, 67.0, 41.0, 26.0, 16.0, 22.0, 17.0, 18.0, 17.0, 20.0, 23.0, 18.0, 20.0, 20.0, 21.0, 23.0, 18.0, 20.0, 17.0, 22.0, 18.0, 22.0, 18.0, 18.0, 22.0, 16.0, 25.0, 30.0, 21.0, 28.0, 23.0, 19.0, 18.0, 20.0, 22.0, 16.0, 21.0, 24.0, 15.0, 22.0, 20.0, 22.0, 16.0, 15.0, 28.0]


plt.plot(channel_array, count_array, 'x', color='red',)

mean,std=norm.fit(counts)
print(mean, std)
plt.savefig('try.pdf')
