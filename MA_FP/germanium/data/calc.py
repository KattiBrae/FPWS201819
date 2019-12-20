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
peaks_x = [  594,  1187, 1667, 1988, 2149, 3765, 4655, 5245, 5371, 6801]
peakno = np.arange(0, len(peaks_x), 1 )
content = np.loadtxt('params.txt', unpack=True,delimiter=' ')
energy, possibility = np.loadtxt('europium_literatur.txt', unpack=True,delimiter=' , ')



t = ufloat(605484000, 54000)
hwz = ufloat(426.7e+06, 5e+06)
B = ufloat(4130, 60)
m = log(2)

A = B*unp.exp(-m/hwz*t)
#print(A)

r=22.5e-03
h=65e-03

Omegadurch4pi =  sin(1/4 * atan(r/h))**2

T = 2134

Q = []
for i in range(len(content)):
    q = content[i]/(Omegadurch4pi *A *T * possibility[i])
    Q.append(q)
#    print(q)
#print(Q)


steigung = 0.20725824
yachse = -1.22364356

#E = steigung*x+yachse
E = 195

x = (E-yachse)/steigung
print(x)
