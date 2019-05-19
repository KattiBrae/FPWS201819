
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

    #A12L12x50mmF0-12000S10B11D16Defektan3mit12_5mm
    x1=u(2450,3270)
    x2=u(5240,6610)
    x3=u(7980,9870)

    #A12L12x50mmF0-12000S10B11D16Defektan3mit75mm
    x4=u(2450,3300)
    x5=u(5150,6580)
    x6=u(7980,9930)

    #A12L12x50mmF0-12000S10B11D16Defektan8mit12_5mm
    x7=u(2410,3270)
    x8=u(5140,6610)
    x9=u(7990,9870)

    #A12L12x50mmF0-12000S10B11D16Defektan8mit75mm
    x10=u(2420,3300)
    x11=u(5120,6590)
    x12=u(8010,9890)

    y=(1,2,3)

    i(x1,x2,x3,y)#x4,x5,x6,x7,y)
    i(x4,x5,x6,y)
    i(x7,x8,x9,y)
    i(x10,x11,x12,y)
    #

    plt.grid()
    plt.savefig("newtest.pdf")
##############################
