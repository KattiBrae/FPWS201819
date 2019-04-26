import numpy as np
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show

plt.rcParams['figure.figsize'] = (20, 10)
plt.rcParams['font.size'] = 16
plt.rcParams['lines.linewidth'] = 2

fig = plt.figure()

print('Graphik1')
print('Steigung','Y-Achsenabschnitt')
date, unwichtig, y = np.loadtxt('C3F8_ohne_1', unpack=True,delimiter=' ')
p, d = np.loadtxt('notes_C3F8_ohne_1.txt', unpack=True,delimiter=',')

x = np.arange(0, len(y), 1 )
pp0 = np.arange(0, len(y), 1 )
s = 72.0 - y

p0 = 7.5636

druck=fig.add_subplot(111)
spannung=fig.add_subplot(111, frame_on=False)

i=0
j=0
for i in range(len(date)):
    if (d[i] <= date[j] < d[i+1]):
        pp0[j] = p[i]/p0
        j = j + 1
    else:
        pass



#y=-y
#def f(x,a,b):
##    return 1/(r1*r2)*a*(r2-c*(x+b))*(r1-d*(x+b))+e
#    return a*x+b
#popt, pcov = curve_fit(f, x, y)
#print(popt)
#print(np.sqrt(np.diag(pcov)))

#x_new = np.linspace(x[0], x[-1], 500)


#plt.figure(1)
druck.plot(x,y,'-')
druck.set_xlabel('Zeit t / s')
druck.set_ylabel('Oberflächendruck ' r'$\pi$ / $\frac{mN}{m}$' )
druck.tick_params(axis='x')
druck.tick_params(axis='y')

#spannung = druck.twinx()
spannung.plot(x,s,'-')
spannung.invert_yaxis()
spannung.set_ylabel('Oberflächenspannung ' r'$\sigma$ / $\frac{mN}{m}$' )
spannung.xaxis.tick_top()
spannung.yaxis.tick_right()
spannung.xaxis.set_label_position('top')
spannung.yaxis.set_label_position('right')
spannung.tick_params(axis='x',)
spannung.tick_params(axis='y',)
#redu = x.twiny()
#redu.plot(p,y,'-')
#redu.set_ylabel('Reduzierter Druck ' r'$\frac{p}{p_0}$' )

#plt.plot(x_new,f(x_new,*popt),'-', label='Regression $\propto L^2$')
#plt.xlabel('Zeit t / s')
#plt.ylabel('Oberflächendruck ' r'$\pi$ / $\frac{mN}{m}$')
plt.grid()
plt.legend()




plt.savefig('C3F8_ohne_1_druck.pdf')
print ('Fertig')



#while date[i] >= d1 and date[i] < d2:
#    p[i] = p1/p0
#    i = i + 1
#    pass
#while date[i] >= d2 and date[i] < d3:
#    p[i] = p2/p0
#    i = i + 1
#    pass
#while date[i] >= d3 and date[i] < d4:
#    p[i] = p3/p0
#    i = i + 1
#    pass
#while date[i] >= d4 and date[i] < d5:
#    p[i] = p4/p0
#    i = i + 1
#    pass
#while date[i] >= d5 and date[i] < d6:
#    p[i] = p5/p0
#    i = i + 1
#    pass
#while date[i] >= d6 and date[i] < d7:
#    p[i] = p6/p0
#    i = i + 1
#    pass
#while date[i] >= d7 and date[i] < d8:
#    p[i] = p7/p0
#    i = i + 1
#    pass
#while date[i] >= d8 and date[i] < d9:
#    p[i] = p8/p0
#    i = i + 1
#    pass
#while date[i] >= d9 and date[i] < d10:
#    p[i] = p9/p0
#    i = i + 1
#    pass
#while date[i] >= d10 and date[i] < d11:
#    p[i] = p10/p0
#    i = i + 1
#    pass
#while date[i] >= d11 and date[i] < d12:
#    p[i] = p11/p0
#    i = i + 1
#    pass
#while date[i] >= d12 and date[i] < d13:
#    p[i] = p12/p0
#    i = i + 1
#    pass
#while date[i] >= d13:
#    p[i] = p13/p0
#    i = i + 1
#    pass
#
