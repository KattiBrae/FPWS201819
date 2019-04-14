#######################################
def LeseTabelle(Name): #Funktion u
    a, b, c = np.loadtxt(Name, unpack=True,delimiter=' ')
    return (a,b,c)
#######################################
def getlenght(yA):
    a=0
    for i in range(len(yA)):
        a=a+len(yA[i])
    return a
######################################
def getY(yA):
    y=[]
    for i in range(len(yA)):
        for x in yA[i]:
            y.append(x)
    return(y)
#####################################
def getX(yA):
    X=[]
    x=0
    while (x<getlenght(yA)):
        x=x+1
        X.append(x)
    return(X)
####################################
def makeArray(a):
    A = []
    for b in a:
        A.append(b)
    return (A)
###################################
def plot():
    XAchse = getX(yA)
    YAchse = getY(yA)

    plt.plot(XAchse,YAchse,'x')
    #plt.legend()
    plt.ylabel(r'Oberflächenspannung $\sigma$ $mN/m^2$')
    plt.xlabel(r'Zeit / s')
    plt.grid()
    plt.show()
###################################

if __name__=="__main__":
    import numpy as np
    import sympy
    import matplotlib.pyplot as plt
    from scipy.optimize import curve_fit
    from pylab import figure, axes, pie, title, show
    from numpy import NaN, Inf, arange, isscalar, asarray, array
    import sys


    ###Eingabe###
    date1, b1, s1 = LeseTabelle('C3F8_ohneDPPA_1021.txt')
    date2, b2, s2 = LeseTabelle('C3F8_ohneDPPA_1250.txt')
    date3, b3, s3 = LeseTabelle('C3F8_ohneDPPA_1500.txt')
    date4, b4, s4 = LeseTabelle('C3F8_ohneDPPA_1751.txt')
    date5, b5, s5 = LeseTabelle('C3F8_ohneDPPA_1999.txt')
    date6, b6, s6 = LeseTabelle('C3F8_ohneDPPA_2250.txt')
    yA = (s1,s2,s3,s4,s5,s6)
    ###########
    
    plot()
