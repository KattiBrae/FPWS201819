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

E, dE, P, dP = np.loadtxt('barium_literatur.txt', unpack=True,delimiter=',')

r=22.5e-03
h=65e-03
Omegadurch4pi =  sin(1/4 * atan(r/h))**2

T = 2347

#Inhalt0 = ufloat(7173.0, 84.69356528095862)
#Inhalt1 = ufloat(1099.0, 33.15116890850155)
#Inhalt2 = ufloat(2290.0, 47.853944456021594)
#Inhalt3 = ufloat(6207.0, 78.78451624526231)
#Inhalt4 = ufloat(845.0, 29.068883707497267)
#komplett = Inhalt0+Inhalt1+Inhalt2+Inhalt3+Inhalt4
Inh = [7173.0, 1099.0, 2290.0, 6207.0, 845.0]
dInh = [84.69356528095862, 33.15116890850155, 47.853944456021594, 78.78451624526231, 29.068883707497267]
Inhalt = unp.uarray(Inh, dInh)


#a = ufloat(0.113, 0.055)
#b = ufloat(-0.36, 0.17)
#c = ufloat(-0.0077, 0.0059)
a = 0.113
b = -0.36
c = -0.0077

#E = unp.uarray(E, dE)
E = [81.05787772000001, 276.29513979999996, 302.61693628, 356.0895622, 383.65490812]
#print(E)
A = []
Q = []
for i in range(len(E)):
    tmp=a*E[i]**b+c
    Q.append(tmp)
    Akt = 1/Omegadurch4pi *Inhalt[i]/( Q[i]*T*P[i])
    A.append(Akt)
#    print('i: ' + str(i))
#    print('E: ' + str(E[i]))
#    print()
#    print('Q: ' + str(Q))
#    print('P: ' + str(P[i]))
#    print('Akt: ' + str(Akt))
print(A)
#[0.015522670553584939, 0.010445319696592558, 0.007234272625168757, 0.006752962659419753, 0.005930667242600041, 0.005569659237846702]

Ages = np.mean(A)
print(Ages)
