##############################
def u(x,y):
    z=y-x
    print(z)
    return(z)
##############################
def i(y1,y2,x):
    y=(y1,y2)
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
    plt.xlabel("Größe der Einheitszelle / $mm$")
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
    D=75,50
    d=75,75
#Bandlücke abstand zwichen Maxima (immer zwei gehören zusammen)
    y1=u(1710,2260)
    y2=u(3640,4490)
    y3=u(5630,6720)
    y4=u(7690,8940)
    y5=u(9710,11180)


    y6=u(2370,3330)
    y7=u(5100,6630)
    y8=u(8040,9880)

    i(y1,y6,D)
    i(y2,y7,D)
    i(y3,y8,D)
    i(y4,y4,d)
    i(y5,y5,d)
#

    #

    plt.grid()
    plt.savefig("newtest.pdf")
##############################
