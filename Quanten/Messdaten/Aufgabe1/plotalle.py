Tabelle1 =      'A1L1x75mmF6000-9000S10.dat' ; label1='75mm'
Tabelle2 =      'A1L2x75mmF6000-9000S10.dat' ; label2='150mm'
Tabelle3 =      'A1L3x75mmF6000-9000S10.dat' ; label3='225mm'
Tabelle4 =      'A1L4x75mmF6000-9000S10.dat' ; label4='300mm'
Tabelle5 =      'A1L5x75mmF6000-9000S10.dat' ; label5='375mm'
Tabelle6 =      'A1L6x75mmF6000-9000S10.dat' ; label6='450mm'
Tabelle7 =      'A1L7x75mmF6000-9000S10.dat' ; label7='525mm'
Tabelle8 =      'A1L8x75mmF6000-9000S10.dat' ; label8='600mm'
T1 =1; T2=1; T3=1; T4=1; T5=1; T6=1; T7=1; T8=1 # 1 = wird betrachtet sonst nicht. Programm ist auf 8 ausgelegt mehr nicht.
Speichername = 'Alle.pdf'
#lookformax = True  # zuerst ein Maximum
lookformax = False  # zuerst ein Minimum
a = 1               # ab wann Schwankung als Extrema gewertet wird

import sys
from numpy import NaN, Inf, arange, isscalar, asarray, array

def peakdet(    v,      # Y-Werte (Vektor)
                delta,  # Toleranzbereich Scalar
                x,      # X-Werte Frequenz (Vektor gleich groß wie v)
                bolean):# Erst Minimum oder Maximum?

    maxtab = []
    mintab = []

    if x is None : x = arange(len(v))

    v = asarray(v)

    if len(v) != len(x):
        sys.exit('Input vectors v and x must have same length')
    if not isscalar(delta):
        sys.exit('Input argument delta must be a scalar')
    if delta <= 0:
        sys.exit('Input argument delta must be positive')

    mn, mx = Inf, -Inf
    mnpos, mxpos = NaN, NaN

    lookformax = bolean

    for i in arange(len(v)):
        this = v[i]
        if this > mx:
            mx = this
            mxpos = x[i]
        if this < mn:
            mn = this
            mnpos = x[i]

        if lookformax:
            if this < mx-delta:
                maxtab.append((mxpos, mx))
                mn = this
                mnpos = x[i]
                lookformax = False
        else:
            if this > mn+delta:
                mintab.append((mnpos, mn))
                mx = this
                mxpos = x[i]
                lookformax = True

    return array(maxtab), array(mintab)

if __name__=="__main__":
    import matplotlib.pyplot as plt
    from matplotlib.pyplot import plot, scatter, show
    import numpy as np
    if T1 is 1:
        x, y = np.loadtxt(Tabelle1, unpack=True,delimiter=' ')
        s = list(y)
        plot(x, y, label=label1)
        maxtab, mintab = peakdet(s,1,x,lookformax)
        print(Tabelle1)
        print('Maximum'), print('x, y'),  print(maxtab)
        print('Minimum'), print('x, y'),  print(mintab)
        scatter(array(maxtab)[:,0], array(maxtab)[:,1], color='blue')#, label='Maximum')
        #scatter(array(mintab)[:,0], array(mintab)[:,1], color='red', label='Minimum')
    ##########
    if T2 is 1:
        x, y = np.loadtxt(Tabelle2, unpack=True,delimiter=' ')
        s = list(y)
        plot(x, y, label=label2)
        maxtab, mintab = peakdet(s,1,x,lookformax)
        print(Tabelle2)
        print('Maximum'), print('x, y'),  print(maxtab)
        print('Minimum'), print('x, y'),  print(mintab)
        scatter(array(maxtab)[:,0], array(maxtab)[:,1], color='blue')#, label='Maximum')
    #############
    if T3 is 1:
        x, y = np.loadtxt(Tabelle3, unpack=True,delimiter=' ')
        s = list(y)
        plot(x, y, label=label3)
        maxtab, mintab = peakdet(s,1,x,lookformax)
        print(Tabelle3)
        print('Maximum'), print('x, y'),  print(maxtab)
        print('Minimum'), print('x, y'),  print(mintab)
        scatter(array(maxtab)[:,0], array(maxtab)[:,1], color='blue')#, label='Maximum')
    ################
    if T4 is 1:
        x, y = np.loadtxt(Tabelle4, unpack=True,delimiter=' ')
        s = list(y)
        plot(x, y, label=label4)
        maxtab, mintab = peakdet(s,1,x,lookformax)
        print(Tabelle4)
        print('Maximum'), print('x, y'),  print(maxtab)
        print('Minimum'), print('x, y'),  print(mintab)
        scatter(array(maxtab)[:,0], array(maxtab)[:,1], color='blue')#, label='Maximum')
    #################
    if T5 is 1:
        x, y = np.loadtxt(Tabelle5, unpack=True,delimiter=' ')
        s = list(y)
        plot(x, y, label=label5)
        maxtab, mintab = peakdet(s,1,x,lookformax)
        print(Tabelle5)
        print('Maximum'), print('x, y'),  print(maxtab)
        print('Minimum'), print('x, y'),  print(mintab)
        scatter(array(maxtab)[:,0], array(maxtab)[:,1], color='blue')#, label='Maximum')
    ###################
    if T6 is 1:
        x, y = np.loadtxt(Tabelle6, unpack=True,delimiter=' ')
        s = list(y)
        plot(x, y, label=label6)
        maxtab, mintab = peakdet(s,1,x,lookformax)
        print(Tabelle6)
        print('Maximum'), print('x, y'),  print(maxtab)
        print('Minimum'), print('x, y'),  print(mintab)
        scatter(array(maxtab)[:,0], array(maxtab)[:,1], color='blue')#, label='Maximum')
    ##################
    if T7 is 1:
        x, y = np.loadtxt(Tabelle7, unpack=True,delimiter=' ')
        s = list(y)
        plot(x, y, label=label7)
        maxtab, mintab = peakdet(s,1,x,lookformax)
        print(Tabelle7)
        print('Maximum'), print('x, y'),  print(maxtab)
        print('Minimum'), print('x, y'),  print(mintab)
        scatter(array(maxtab)[:,0], array(maxtab)[:,1], color='blue')#, label='Maximum')
    ################
    if T8 is 1:
        x, y = np.loadtxt(Tabelle8, unpack=True,delimiter=' ')
        s = list(y)
        plot(x, y, label=label8)
        maxtab, mintab = peakdet(s,1,x,lookformax)
        print(Tabelle8)
        print('Maximum'), print('x, y'),  print(maxtab)
        print('Minimum'), print('x, y'),  print(mintab)
        scatter(array(maxtab)[:,0], array(maxtab)[:,1], color='blue')#, label='Maximum')
    #####################

    plt.legend()
    plt.grid()
    plt.xlabel('Frequenz')
    plt.ylabel('Intensität')
    plt.savefig(Speichername)
    print('Fertig')
