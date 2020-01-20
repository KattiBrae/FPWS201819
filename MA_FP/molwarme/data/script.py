import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from uncertainties import unumpy as unp
import scipy.constants as const

deb_exp = unp.uarray(327,30)
def deb(rho, M, vt, vl):
    return const.hbar/const.k * (18*const.pi**2*const.N_A*rho*(1/vl**3 + 2/vt**3)**(-1.0) * 1/M)**(1.0/3)

print('deb, theo = , ',deb(8920, 0.063546, 2260, 4700))
print('deb, omega theo = ',const.k/const.hbar*deb(8920, 0.063546, 2260, 4700))
print('deb, omega exp = ',const.k/const.hbar*deb_exp)