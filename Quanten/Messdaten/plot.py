Tabelle =      'L8x75cF100-10000S10.dat'
Speichername = 'L8x75cF100-10000S10.pdf'

import sys
from numpy import NaN, Inf, arange, isscalar, asarray, array

def peakdet(    v,      # Y-Werte (Vektor)
                delta,  # Toleranzbereich Scalar
                x):     # X-Werte Frequenz (Vektor gleich groß wie v)

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

    lookformax = True

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
    x, y = np.loadtxt(Tabelle, unpack=True,delimiter=' ')
    s = list(y)
    plot(x, y)
    maxtab, mintab = peakdet(s,0.5,x)
    print(Tabelle)
    print('Maximum'), print('x, y'),  print(maxtab)
    print('Minimum'), print('x, y'),  print(mintab)
    scatter(array(maxtab)[:,0], array(maxtab)[:,1], color='blue', label='Maximum')
    scatter(array(mintab)[:,0], array(mintab)[:,1], color='red', label='Minimum')
    plt.legend()
    plt.grid()
    plt.xlabel('Frequenz')
    plt.ylabel('Intensität')
    plt.savefig(Speichername)
    print('Fertig')
