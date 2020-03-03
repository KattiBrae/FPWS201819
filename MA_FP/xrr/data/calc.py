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

#D = 0.02
#d = 0.2e-3
#
#a = np.arcsin(d/D)
#print(a)
#a = 0.5729673448571527 #degrees

#detek_ai, detek_counts = np.loadtxt('1239_detektorscan1.txt', unpack=True,delimiter=' , ')
#print('Max. Detektor-Scan \t' + str(max(detek_counts)))
#
#zscan_z, zscan_counts = np.loadtxt('1242_zscan1.txt', unpack=True,delimiter=' , ')
#print('Max. z-Scan \t\t' + str(max(zscan_counts)))
#
#rocking_ai, rocking_counts = np.loadtxt('1219_rock1.txt', unpack=True,delimiter=' , ')
#print('Max. rocking-Scan \t' + str(max(rocking_counts)))
#
#messung_ai, messung_counts = np.loadtxt('1416_messung_iguess.txt', unpack=True,delimiter=' , ')
#print('Max. Messung \t\t' + str(max(messung_counts)))
#

exp  = 0.208
theo = 0.22
relabw = (exp-theo)/theo *100
print(relabw)
