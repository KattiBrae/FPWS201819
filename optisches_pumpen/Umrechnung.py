import numpy as np
#import scipy.constants as const

#frequenz, horizontal umdrehungen, Sweepumdrehungen(für beide atome)
f, h1, s1, s2, h2 =np.loadtxt('resonanz.txt', unpack=True, delimiter=',')

#eine umdrehung =0,1V
#Atom eins
Ih1=0.3*(h1+0.08)
Is1=0.1*s1
print('Ih1', Ih1)
print('Is1', Is1)
#Atom zwei
Ih2=0.3*(h2+0.08)
Is2=0.1*s2
print('Ih2', Ih2)
print('Is2', Is2)

#Sweep-Spule
#Radius
Rs=16.39*10**-2#in meter
#Windungen
Ns=11
#Horizontalspule
#Radius
Rh=15.79*10**-2#in meter
#Windungen
Nh=154

#Vertikalspule
#Radius
Rv=11.735*10**-2#in meter
#Windungen
Nv=20


mu_0=4*np.pi*10**(-7)
print(mu_0)

########
#Bh1=(mu_0*8*Nh*Ih1)/(Rh*np.sqrt(125))
#Bs1=(mu_0*8*Ns*Is1)/(Rs*np.sqrt(125))
#Bh2=(mu_0*8*Nh*Ih2)/(Rh*np.sqrt(125))
#Bs2=(mu_0*8*Ns*Is2)/(Rs*np.sqrt(125))
#*Rh**2
#*Rh**2
#*Rh**2
#*Rh**2

Bh1=(mu_0*Nh*Ih1*Rh**2)/((Rh**2+(Rh/2)**2)**(3/2))
Bs1=(mu_0*Ns*Is1*Rs**2)/((Rs**2+(Rs/2)**2)**(3/2))
Bh2=(mu_0*Nh*Ih2*Rh**2)/((Rh**2+(Rh/2)**2)**(3/2))
Bs2=(mu_0*Ns*Is2*Rs**2)/((Rs**2+(Rs/2)**2)**(3/2))
#print('bbbbbbbbbbbbbhhhhhhhhhhhhhhh11111111111')

########
#Summe der Felder
B1=Bh1+Bs1
B2=Bh2+Bs2
print('###########für die Freqenzen##########')
print(f)
#print('###########Ih##############################')
#print(Ih1,Ih2)
#print('#############Is#########################')
#print(Is1,Is2)
print('##########B-Feld Atom eins##########')
B1=B1*10**6#umrechnung in mu T
print(B1)
print('##########B-Feld Atom zwei##########')
B2=B2*10**6#umrechnung in mu T
print(B2)

###########################Plot####################################
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show
import scipy.constants as const


print('B1')



def g(f,a,b):
    return a*f+b
popt, pcov = curve_fit(g, f, B1)
print(popt)
print(np.sqrt(np.diag(pcov)))

f_new = np.linspace(f[0], f[-1], 500)


print('B2')



def q(f,e,w):
    return e*f+w
popt2, pcov2 = curve_fit(q, f, B2)
print(popt2)
print(np.sqrt(np.diag(pcov2)))


f_new = np.linspace(f[0], f[-1], 500)



plt.figure(1)
plt.plot(f,B1,'x')
plt.plot(f,B2,'x')
plt.plot(f_new,g(f_new,*popt),'-', label='Messung1')
plt.plot(f_new,q(f_new,*popt2),'-',label='Messung2')

plt.xlabel('Frequenz / kHz')
plt.ylabel('B-Feld / $\mu$T')
plt.grid()
plt.legend()


plt.savefig('B-Feld.pdf')
############# g_F #################
#a &e Steigung der Ausgleichsgraden
a = 1.4382169e-10  #10^-6/10^3   muT/kHz
A= 0.0232002e-10    #Fehler von a
e = 2.1409131e-10 #T/Hz
E=0.030643e-10      #Fehler von E

h = 6.62607004e-34 #J*s
mu_b =9.27400899e-24 #J/T
print('##########   Lande Faktoren  ##########')
g_h1 = h/(mu_b*a)
g_h2 = h/(mu_b*e)
print(g_h1,g_h2)
##Fehlerberechnung
G_h1 = np.sqrt((h/(mu_b*a**2))**2*A**2)
G_h2 = np.sqrt((h/(mu_b*e**2))**2*E**2)
print('###### Fehler Lande Faktor   ########')
print(G_h1)
print(G_h2)

#### Kernspin ####
gj = 2.0023
I1=1/2*(gj/g_h1-1)
I2=1/2*(gj/g_h2-1)
print('#######  Kernspin    ##########')
print(I1,I2)
###### Fehler Kernspin  #####
print('######## Fehler Kernspin #######')
i1=np.sqrt((1/2*(gj/g_h1**2))**2*G_h1**2)
i2=np.sqrt((1/2*(gj/g_h2**2))**2*G_h2**2)
print(i1)
print(i2)


#########Wechselwirkungsenergie###########
print('######   Quadratische Zeeman #######')
DE1=4.53*10**(-24)  # gegeben in der Anleitung
DE2=2.01*10**(-24)  # gegeben in der Anleitung
U_HF1=g_h1*mu_b*B1+g_h1**2*mu_b**2*B1**2*(-3)/DE1
U_HF2=g_h2*mu_b*B1+g_h2**2*mu_b**2*B2**2*(-3)/DE2
print(U_HF1)
print(U_HF2)
######### Fehler vom Qudrat. Zeeman ######
print('######## Fehler Zeeman#######')
u_HF1=np.sqrt((mu_b*B1+g_h1*mu_b**2*B1**2*(-3)/DE1)**2*G_h1**2)
u_HF2=np.sqrt((mu_b*B2+g_h2*mu_b**2*B2**2*(-3)/DE2)**2*G_h2**2)
print(u_HF1)
print(u_HF2)

print ('Fertig')
