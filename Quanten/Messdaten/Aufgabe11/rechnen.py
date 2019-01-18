
##############################
def u(x,y):
    z=y-x
    print(z)
    return(z)
##############################
def i(y1,y2,y3,y4,y5,y6,y7,x):
    y=(y1,y2,y3,y4,y5,y6,y7)
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
    plt.xlabel("Nummer")
    plt.ylabel(r"Bandlücke $\Delta f$")
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
    x1=u(2150,2480)
    x2=u(3300,3790)
    x3=u(4510,4880)
    x4=u(5490,6620)
    x5=u(7880,9150)
    x6=u(9480,10290)
    x7=u(10690,11450)

    y=1,2,3,4,5,6,7

    i(x1,x2,x3,x4,x5,x6,x7,y)
    #

    plt.grid()
    plt.savefig("newtest.pdf")
##############################
