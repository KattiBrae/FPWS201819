import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

y, x = np.loadtxt('hysterese.txt', unpack=True,delimiter=' ')

plt.grid()
plt.plot(y,x)
plt.show()
