Bild = "bild.jpg"       #Bild Quelle
Speichername = 'NeuBild.pdf'
#lookformax = True  # zuerst ein Maximum
lookformax = False  # zuerst ein Minimum
s = 5              # ab wann Schwankung als Extrema gewertet wird
zeile = 500        # zu betrachtetde pixelzeile


def image2pixelarray(filepath):

    im = Image.open(filepath).convert('L')
    (width, height) = im.size
    greyscale_map = list(im.getdata())
    greyscale_map = np.array(greyscale_map)
    greyscale_map = greyscale_map.reshape((height, width))
    return greyscale_map                                    #gray... ist ein array aus arrays

######################################################################################################
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



if __name__ == '__main__':
    from PIL import Image
    import numpy as np
    import matplotlib.pyplot as plt
    #from scipy.optimize import curve_fit
    from pylab import figure, axes, pie, title, show
    import sys



    greyscale_map = image2pixelarray(Bild)   #aufruf der klasse
    a = greyscale_map[zeile]                            #aus gre... wird ein Array genommen
    #print(a)



######################################



    plt.plot(a)
    maxtab, mintab = peakdet(a,s,None,lookformax)
    #print(Tabelle)
    print('Maximum'), print('x = Pixelzahl, y = Intensität'),  print(maxtab)
    #print('Minimum'), print('x, y'),  print(mintab)
    plt.scatter(array(maxtab)[:,0], array(maxtab)[:,1], color='blue', label='Maximum')
    #scatter(array(mintab)[:,0], array(mintab)[:,1], color='red', label='Minimum')
    plt.legend()
    plt.grid()
    plt.xlabel('Piksel')
    plt.ylabel('Intensität')
    plt.savefig(Speichername)
    print('Fertig')
