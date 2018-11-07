import numpy as np

f, h1, s1, s2, h2 =np.loadtxt('resonanz.txt', unpack=True, delimiter=',')

#Horizontalspule
#Radius
Rh=15.79
#Windungen
Nh=154

#Vertikalspule
#Radius
Rv=11.735
#Windungen
Nv=20

#B-Feldberechnug
B=(NIR**2)/(R**2+x**2)**(3/2)
