##############################
def u(x,y):
    z=y-x
    print(z)
    return(z)
##############################
def i(y1,y2,y3,x):
    y=(y1,y2,y3)
    def f(x,a,b):
        return(a*x+b)
    Werte, Fehler = curve_fit(f, x, y)
    print(Werte)
    print(np.diag(Fehler**2)**(1/4))
    x_new = np.linspace(x[0], x[-1], 500)
    plt.figure(1)
    plt.plot(x_new,f(x_new,*Werte),'-', color="red")#, label='Fitfunktion $\Delta f \sim 1/d$')
    plt.plot(x,y,"x",color="blue")
    #plt.legend()
    plt.xlabel("Blendengröße")
    plt.ylabel(r"Bandgröße $\Delta f$")
##############################
if __name__ == '__main__':
    import numpy as np
    import sympy
    import matplotlib.pyplot as plt
    from scipy.optimize import curve_fit
    from pylab import figure, axes, pie, title, show
    from numpy import NaN, Inf, arange, isscalar, asarray, array
    import sys
#
    D=10,13,16
#Bandlücke abstand zwichen Maxima (immer zwei gehören zusammen)
    x1=u(1130,3440)
    x2=u(1300,3420)
    x3=u(1430,3390)

    i(x1,x2,x3,D)
    #
    x4=u(3930,6820)
    x5=u(4160,6770)
    x6=u(4410,6730)

    i(x4,x5,x6,D)
    #
    x7=u(7130,10180)
    x8=u(7300,10110)
    x9=u(7510,10040)

    i(x7,x8,x9,D)
    #

    plt.grid()
    plt.savefig("newtest.pdf")
##############################
