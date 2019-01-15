"""
Bandlücken
Anfang  Ende
D10
"""
x=10,10,10
y1=-(1840-3360)
y2=-(4300-6740)
y3=-(7400-10100)
#print(y1,y2,y3)
"""
D13
"""
c= 13, 13, 13
y4=-(2150-3280)
y5=-(4670-6660)
y6=-(7660-9980)
"""
D16
"""
v=16, 16, 16
y7=-(2470-3260)
y8=-(5170-6570)
y9=-(8020-9840)

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
plt.xlabel('Blendenbreit')
plt.ylabel(r'Breiter der Bandlücke $\Delta$ f')
plt.savefig("Bandlücken.pdf")
print('Fertig')
