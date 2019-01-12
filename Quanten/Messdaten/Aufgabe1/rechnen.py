# Berechnung zur Geschwindigkeit des Schalles
# Delta f ~ 1/d     der frequenzabstand zweier maxima ist ~ zur 1/Länge
# x werte sind f
"""
A1L1x50mmF5000-14000S2.dat
x, y
[[  5.13600000e+03   6.36200000e+00]#zu vernachlässigen
 [  6.85600000e+03   8.60390000e+01]
 [  1.02520000e+04   6.23230000e+01]
 [  1.36160000e+04   1.63910000e+01]]
"""
L=50
f1=6.85600000e+03
f2=1.02520000e+04
f3=1.36160000e+04

df1=f2-f1
df2=f3-f2
print("#Delta f1:" ,df1,"#Delta f2:" ,df2, "#Delta f:", (df1+df2)/2, "#Länge:", L)

"""
A1L1x75mmF6000-9000S10.dat
x, y
[[ 6860.       52.058]] # nur ein Maximum daher kein Delta f bestimmbar

A1L2x75mmF6000-9000S10.dat
x, y
[[ 6870.       51.158]
 [ 8010.       47.74 ]]
 """
L=75*2
f1=6870
f2=8010

df1=f2-f1
print("#Delta f1:" ,df1, "#Länge:", L)

"""
A1L3x75mmF6000-9000S10.dat
x, y
[[ 6110.       48.711]
 [ 6880.       53.955]
 [ 7640.       41.569]
 [ 8400.       34.204]]
 """
L=75*3
f1=6110
f2=6880
f3=7640
f4=8400

df1=f2-f1
df2=f3-f2
df3=f4-f3
print("#Delta f1:" ,df1,"#Delta f2:" ,df2,"#Delta f3:" ,df3, "#Delta f:", (df1+df2+df3)/3, "#Länge:", L)

"""
A1L4x75mmF6000-9000S10.dat
x, y
[[ 6310.       46.764]
 [ 6880.       32.946]
 [ 7450.       34.172]
 [ 8030.       32.223]
 [ 8590.       24.776]]
"""
L=75*4
f1=6310
f2=6880
f3=7450
f4=8030
f5=8590

df1=f2-f1
df2=f3-f2
df3=f4-f3
df4=f5-f4
print("#Delta f1:" ,df1,"#Delta f2:" ,df2,"#Delta f3:" ,df3,"#Delta f4:" ,df4, "#Delta f:", (df1+df2+df3+df4)/4, "#Länge:", L)

"""
A1L5x75mmF6000-9000S10.dat
x, y
[[ 6420.       30.865]
 [ 6880.       33.412]
 [ 7340.       27.318]
 [ 7800.       25.575]
 [ 8260.       24.936]
 [ 8710.       20.024]]
"""
L=75*5
f1=6420
f2=6880
f3=7340
f4=7800
f5=8260
f6=8710

df1=f2-f1
df2=f3-f2
df3=f4-f3
df4=f5-f4
df5=f6-f5
print("#Delta f1:" ,df1,"#Delta f2:" ,df2,"#Delta f3:" ,df3,"#Delta f4:" ,df4,"#Delta f5:" ,df5, "#Delta f:", (df1+df2+df3+df4+df5)/5, "#Länge:", L)

"""
A1L6x75mmF6000-9000S10.dat
x, y
[[ 6120.       28.821]
 [ 6500.       30.062]
 [ 6880.       24.218]
 [ 7260.       25.685]
 [ 7650.       22.737]
 [ 8030.       19.897]
 [ 8410.       22.437]
 [ 8790.       18.614]]
"""
L=75*6
f1=6120
f2=6500
f3=6880
f4=7260
f5=7650
f6=8030
f7=8410
f8=8790

df1=f2-f1
df2=f3-f2
df3=f4-f3
df4=f5-f4
df5=f6-f5
df6=f7-f6
df7=f8-f7
print("#Delta f1:" ,df1,"#Delta f2:" ,df2,"#Delta f3:" ,df3,"#Delta f4:" ,df4,"#Delta f5:" ,df5,"#Delta f6:" ,df6,"#Delta f7:" ,df7, "#Delta f:", (df1+df2+df3+df4+df5+df6+df7)/7, "#Länge:", L)

"""
A1L7x75mmF6000-9000S10.dat
x, y
[[ 6230.       28.838]
 [ 6560.       22.99 ]
 [ 6880.       24.32 ]
 [ 7210.       20.116]
 [ 7540.       21.035]
 [ 7860.       19.903]
 [ 8190.       18.008]
 [ 8520.       18.965]
 [ 8850.       16.43 ]]
"""
L=75*7
f1=6230
f2=6560
f3=6880
f4=7210
f5=7540
f6=7860
f7=8190
f8=8520
f9=8850

df1=f2-f1
df2=f3-f2
df3=f4-f3
df4=f5-f4
df5=f6-f5
df6=f7-f6
df7=f8-f7
df8=f9-f8
print("#Delta f1:" ,df1,"#Delta f2:" ,df2,"#Delta f3:" ,df3,"#Delta f4:" ,df4,"#Delta f5:" ,df5,"#Delta f6:" ,df6,"#Delta f7:" ,df7,"#Delta f8:" ,df8, "#Delta f:", (df1+df2+df3+df4+df5+df6+df7+df8)/8, "#Länge:", L)

"""
A1L8x75mmF6000-9000S10.dat
x, y
[[ 6030.       25.534]
 [ 6310.       21.559]
 [ 6590.       22.307]
 [ 6880.       19.098]
 [ 7170.       20.084]
 [ 7460.       18.226]
 [ 7740.       17.702]
 [ 8030.       15.643]
 [ 8320.       14.272]
 [ 8600.       15.907]
 [ 8890.       14.711]]
"""
L=75*8
f1=6030
f2=6310
f3=6590
f4=6880
f5=7170
f6=7460
f7=7740
f8=8030
f9=8320
f10=8600
f11=8890

df1=f2-f1
df2=f3-f2
df3=f4-f3
df4=f5-f4
df5=f6-f5
df6=f7-f6
df7=f8-f7
df8=f9-f8
df9=f10-f9
df10=f11-f10
Df1=(df1+df2+df3+df4+df5+df6+df7+df8+df9+df10)/10
print("#Delta f1:" ,df1,"#Delta f2:" ,df2,"#Delta f3:" ,df3,"#Delta f4:" ,df4,"#Delta f5:" ,df5,"#Delta f6:" ,df6,"#Delta f7:" ,df7,"#Delta f8:" ,df8,"#Delta f9:" ,df9,"#Delta f10:" ,df10, "#Delta f:", Df1, "#Länge:", L)
l=Df1*2
c=Df1*l*(1/1000)
print(c)


##############plotten der werte#########
print("#########################################################################################################")
"""
3380.0 50
1140 150
763.3333333333334 225
570.0 300
572.5 375
381.42857142857144 450
327.5 525
286.0 600
"""

print("Frequenzen/Länge Fitfunktion Df = a 1/x + b")

import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

print('Graphik1')
print('Steigung','Y-Achsenabschnitt')
y, x = np.loadtxt('geschi.txt', unpack=True,delimiter=' ')

def f(x,a,b):
    return a*(1/x)+b
Werte, Fehler = curve_fit(f, x, y)
print(Werte)
print(np.diag(Fehler**2)**(1/4))


x_new = np.linspace(x[0], x[-1], 500)



plt.figure(1)
plt.plot(x_new,f(x_new,*Werte),'-', label='Fitfunktion $\Delta f \sim 1/d$')
plt.plot(x,y,'x')
plt.xlabel('Länge d / mm')
plt.ylabel('Frequenz $\Delta$ f')
plt.grid()
plt.legend()




plt.savefig('geschi.pdf')
print ('Fertig')

"""
Ergebniss aus python
mit der Form a*1/x+b
[  1.68692913e+05   8.56657992e+00]
[ 253.97695158    1.99530368]
"""
a=1.687*10**5
f=1.68e5*(1/x)+8.5
print(f)#passt ziemlich gut

C=(a)/0.075
print(C)
l=2*f
c=l*f*(1/1000)
print(c)

print("######################################################################################################")
#############
print("(Resonanzfrequenz/Rohranzahl)")
o, p = np.loadtxt('bild.txt', unpack=True,delimiter=' ')

#def f(x,a,b):
#    return a*(1/x)+b
#Werte, Fehler = curve_fit(f, x, y)
#print(Werte)
#print(np.diag(Fehler**2)**(1/4))
#
#
#x_new = np.linspace(x[0], x[-1], 500)



plt.figure(2)
plt.plot(o,p,'x', label="Messwerte")
#plt.plot(x_new,f(x_new,*Werte),'-', label='Fitfunktion $\Delta f \sim 1/d$')
plt.xlabel('Rohranzahl')
plt.ylabel('Resonanzfrequenz f')
plt.grid()
plt.legend()




plt.savefig('bild.pdf')
print ('Fertig ')
print("####################################################################################################")
#############
print("(Resonanzfrequenzen numeriert + Ausgleichsgerade)")
x1, y1 = np.loadtxt('linearfit1.txt', unpack=True,delimiter=' ')
def f1(x1,a,b):
    return a*x1+b
Werte, Fehler = curve_fit(f1, x1, y1)
print(Werte)
print(np.diag(Fehler**2)**(1/4))
x1_new = np.linspace(x1[0], x1[-1], 500)
plt.figure(3)
plt.plot(x1,y1,'x', label="Messwerte")
plt.plot(x1_new,f1(x1_new,*Werte),'-', label='Ausgleichsgerade')


x2, y2 = np.loadtxt('linearfit2.txt', unpack=True,delimiter=' ')
def f2(x2,a,b):
    return a*x2+b
Werte, Fehler = curve_fit(f2, x2, y2)
print(Werte)
print(np.diag(Fehler**2)**(1/4))
x2_new = np.linspace(x2[0], x2[-1], 500)
plt.plot(x2,y2,'x')#, label="Messwerte")
plt.plot(x2_new,f2(x2_new,*Werte),'-')#, label='Ausgleichsgerade')

x3, y3 = np.loadtxt('linearfit3.txt', unpack=True,delimiter=' ')
def f3(x3,a,b):
    return a*x3+b
Werte, Fehler = curve_fit(f3, x3, y3)
print(Werte)
print(np.diag(Fehler**2)**(1/4))
x3_new = np.linspace(x3[0], x3[-1], 500)
plt.plot(x3,y3,'x')#, label="Messwerte")
plt.plot(x3_new,f3(x3_new,*Werte),'-')#, label='Ausgleichsgerade')

x4, y4 = np.loadtxt('linearfit4.txt', unpack=True,delimiter=' ')
def f4(x4,a,b):
    return a*x4+b
Werte, Fehler = curve_fit(f4, x4, y4)
print(Werte)
print(np.diag(Fehler**2)**(1/4))
x4_new = np.linspace(x4[0], x4[-1], 500)
plt.plot(x4,y4,'x')#, label="Messwerte")
plt.plot(x4_new,f4(x4_new,*Werte),'-')#, label='Ausgleichsgerade')

x5, y5 = np.loadtxt('linearfit5.txt', unpack=True,delimiter=' ')
def f5(x5,a,b):
    return a*x5+b
Werte, Fehler = curve_fit(f5, x5, y5)
print(Werte)
print(np.diag(Fehler**2)**(1/4))
x5_new = np.linspace(x5[0], x5[-1], 500)
plt.plot(x5,y5,'x')#, label="Messwerte")
plt.plot(x5_new,f5(x5_new,*Werte),'-')#, label='Ausgleichsgerade')

x6, y6 = np.loadtxt('linearfit6.txt', unpack=True,delimiter=' ')
def f6(x6,a,b):
    return a*x6+b
Werte, Fehler = curve_fit(f6, x6, y6)
print(Werte)
print(np.diag(Fehler**2)**(1/4))
x6_new = np.linspace(x6[0], x6[-1], 500)
plt.plot(x6,y6,'x')#, label="Messwerte")
plt.plot(x6_new,f6(x6_new,*Werte),'-')#, label='Ausgleichsgerade')

x7, y7 = np.loadtxt('linearfit7.txt', unpack=True,delimiter=' ')
def f7(x7,a,b):
    return a*x7+b
Werte, Fehler = curve_fit(f7, x7, y7)
print(Werte)
print(np.diag(Fehler**2)**(1/4))
x7_new = np.linspace(x7[0], x7[-1], 500)
plt.plot(x7,y7,'x')#, label="Messwerte")
plt.plot(x7_new,f7(x7_new,*Werte),'-')#, label='Ausgleichsgerade')

plt.xlabel('Resonanzindex')
plt.ylabel('Resonanzfrequenz f')
plt.grid()
plt.legend()


plt.savefig('linearfit.pdf')




#ergebniss auf Phython
a=1140#.  5730.]
#[ inf  inf]
h1=a*0.075*2*2
print(h1)

#[  763.00000002  5349.99999995]
#[ 1.73205078  4.74341648]
h2=763*(0.075*3)*2
print(h2)

a= 571.00000009#  5738.99999974]
#[ 1.52752528  5.06622819]
h3=a*(0.075*4)*2
print(h3)

a= 458.57142856#  5963.33333337]
#[ 0.82478609  3.21208036]
h4=a*0.075*5*2
print(h4)

a= 381.90476191  #5736.42857139]
#[ 0.43470044  2.19512964]
h5=a*0.075*6*2
print(h5)

#[  327.16666669  5901.94444431]
#[ 0.41943525  2.360294  ]
h6=327.16666667*(0.075*7)*2
print(h6)

#[  286.54545455  5737.09090907]
#[ 0.37848474  2.56700835]
#y = 286.5*x+5737
h7=286.545454*(0.075*8)*2
print(h7)


H = (h1+h2+h3+h4+h5+h6+h7)/7
print(H)
dH = np.sqrt((1/7*(7-1))*((h1-H)**2+(h2-H)**2+(h3-H)**2+(h4-H)**2+(h5-H)**2+(h6-H)**2+(h7-H)**2))
print(dH)

print ('Fertig')
#############
print("############################################################################################")
# eigentliche Aufgabenstellung
#untersuchung von L8x75cF100-10000S10

#maxima:
"""
#[[  2.20000000e+02   5.07300000e+00]Intensität zu gering = keine Maxima
 [  3.00000000e+02   1.95500000e+01]
 #[  3.90000000e+02   6.59500000e+00]
 #[  4.30000000e+02   8.01500000e+00]
 #[  4.50000000e+02   8.64100000e+00]
 [  5.90000000e+02   9.35090000e+01]
 #[  6.70000000e+02   7.44500000e+00]
 [  8.70000000e+02   2.04670000e+01]
 [  1.16000000e+03   1.03650000e+01]
 [  1.44000000e+03   2.21440000e+01]
 [  1.73000000e+03   2.39490000e+01]
 [  2.01000000e+03   3.56310000e+01]
 [  2.30000000e+03   3.32860000e+01]
 [  2.59000000e+03   4.07910000e+01]
 [  2.87000000e+03   3.16130000e+01]
 [  3.16000000e+03   2.76260000e+01]
 [  3.44000000e+03   2.32940000e+01]
 [  3.73000000e+03   1.99260000e+01]
 [  4.02000000e+03   1.88020000e+01]
 [  4.31000000e+03   1.35180000e+01]
 [  4.59000000e+03   1.65800000e+01]
 [  4.88000000e+03   1.76300000e+01]
 [  5.17000000e+03   5.48730000e+01]
 [  5.45000000e+03   3.71140000e+01]
 [  5.74000000e+03   2.89440000e+01]
 [  6.03000000e+03   2.77030000e+01]
 [  6.31000000e+03   2.15790000e+01]
 [  6.60000000e+03   2.29970000e+01]
 [  6.88000000e+03   1.88570000e+01]
 [  7.17000000e+03   1.99180000e+01]
 [  7.45000000e+03   1.80480000e+01]
 [  7.74000000e+03   1.78030000e+01]
 [  8.02000000e+03   1.53150000e+01]
 [  8.32000000e+03   1.41880000e+01]
 [  8.59000000e+03   1.56280000e+01]
 [  8.88000000e+03   1.47780000e+01]
 [  9.17000000e+03   1.47730000e+01]
 [  9.46000000e+03   1.33060000e+01]
 [  9.75000000e+03   1.24180000e+01]]
"""

x8, y8 = np.loadtxt('richtig.txt', unpack=True,delimiter=' ')
def f8(x8,a,b):
    return a*x8+b
Werte, Fehler = curve_fit(f8, x8, y8)
print(Werte)
print(np.diag(Fehler**2)**(1/4))
x8_new = np.linspace(x8[0], x8[-1], 500)
plt.figure(4)
plt.plot(x8,y8,'x', label="Messwerte")
plt.plot(x8_new,f8(x8_new,*Werte),'-', label='Ausgleichsgerade')

plt.xlabel('Resonanzindex')
plt.ylabel('Resonanzfrequenz f')
plt.grid()
plt.legend()


plt.savefig('richtig.pdf')

a = 286.23376626#   12.085561  ]
#[ 0.07468486  1.49835691]
c = a*2*0.075*8
fc = np.sqrt((2*0.075*8)**2+0.07468486**2)

print(c, "+-", fc)



c = 343.28
l = c / y8
print(l)
k=(2*np.pi)/l
print(k)
w = 2*np.pi *y8


print('Graphik1')
print('Steigung','Y-Achsenabschnitt')


def f(k,a,b):
    return a*k**2
Werte, Fehler = curve_fit(f, k, w)
print(Werte)
print(np.diag(Fehler**2)**(1/4))


k_new = np.linspace(k[0], k[-1], 500)

h = 6.62607004e-34
m = 9.10938356*10**(-31)
E = (h**2*k**2)/(2*m)
print(E)
plt.figure(5)
plt.plot(k_new,f(k_new,*Werte),'-')#, label='Fitfunktion $\Delta f \sim 1/d$')
#plt.plot(k,E)
plt.plot(k,w,'x', label="Messwerte")
plt.ylabel(r'$\omega$ (k)')
plt.xlabel(r'k')
plt.grid()
plt.legend()

plt.savefig('richtig-fw.pdf')
print ('Fertig')
