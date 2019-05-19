def Freqenzabstand(y):
    X = []
    Y = []
    i=0
    while(i<len(y)-1):
        X.append(1/(y[i]-y[i+1]))
        Y.append(i)
        i=i+1
    return(X,Y)
##############################
def makeArray(a):
    A = []
    for b in a:
        A.append(b)
    return (A)
##############################




if __name__=="__main__":
    import numpy as np
    import matplotlib.pyplot as plt
    import sympy
    from scipy.optimize import curve_fit
    from pylab import figure, axes, pie, title, show
    from numpy import NaN, Inf, arange, isscalar, asarray, array
    import sys

    x,y = np.loadtxt('tabelle.txt', unpack = True , delimiter = ' ')
    #y ist die Freqenz
    Y = makeArray(y)
    X = makeArray(x)
    roh,N = Freqenzabstand(Y)
    plt.plot(N,roh,"x")
    plt.grid()
    plt.show()
