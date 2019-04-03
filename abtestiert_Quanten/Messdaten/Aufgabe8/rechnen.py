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
    plt.ylabel(r"$\Delta f$")
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
#
    x1=u(470,1130)
    x2=u(490,1300)
    x3=u(470,1430)

    i(x1,x2,x3,D)
#
    x4=u(3440,3930)
    x5=u(3420,4160)
    x6=u(3390,4410)

    i(x4,x5,x6,D)
#
    x7=u(6820,7130)
    x8=u(6770,7300)
    x9=u(6730,7510)

    i(x7,x8,x9,D)
#
    x10=u(10180,10460)
    x11=u(10110,10580)
    x12=u(10040,10740)

    i(x10,x11,x12,D)


    plt.grid()
    plt.savefig("test.pdf")
##############################
#Es ist der Abstand zwischen zwei Maxilam stellen. Diese gehören jeweils zusammen wie aud den bildern zu sehen.
