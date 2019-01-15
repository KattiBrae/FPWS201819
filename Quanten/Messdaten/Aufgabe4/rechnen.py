"""
L=10
D =16
Anfang  Ende
"""
x=10,10,10
y1=-(2480-3230)
y2=-(5170-6550)
y3=-(8080-9830)
"""
L=12
D=16
"""
c=12,12,12
y4=-(2470-3260)
y5=-(5170-6580)
y6=-(8020-9840)
"""
L=8
D=16
"""
v=8,8,8
y7=-(2490-3170)
y8=-(5170-6520)
y9=-(8080-9820)


import matplotlib.pyplot as plt
from matplotlib.pyplot import plot, scatter, show
import numpy as np
#x, y = np.loadtxt(Tabelle, unpack=True,delimiter=' ')
s = y1, y2, y3
plot(x, s, "x", label="Messwerte")
d = y4, y5, y6
plot(c, d, "x")
f = y7, y8, y9
plot(v, f, "x")
plt.grid()
plt.legend()
plt.xlabel('Rohrlänge')
plt.ylabel(r'Breiter der Bandlücke $\Delta$ f')
plt.savefig("Bandlücke.pdf")
print('Fertig')
