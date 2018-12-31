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
plt.plot(x,y,'x')
plt.plot(x_new,f(x_new,*Werte),'-', label='Fitfunktion $\Delta f \sim 1/d$')
plt.xlabel('Länge d')
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
f=1.68e5*(1/x)+8.5
l=2*f
c=l*f*(1/1000)
print(c)
