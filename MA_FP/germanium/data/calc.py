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


t = ufloat(605484000, 54000)
hwz = ufloat(426.7e+06, 5e+06)
B = ufloat(4130, 60)
m = log(2)

A = B*unp.exp(-m/hwz*t)
print(A)



r=22.5e-03
h=65e-03


Omega =  sin(1/4 * atan(r/h))**2
print(Omega)
