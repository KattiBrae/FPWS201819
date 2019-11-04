######################################
def u(x,y): #Funktion u

    def h(x,a,b):
        return a*x+b
    Werte, Fehler = curve_fit(h, x, y)

    x1_new = np.linspace(x1[0], x1[-1], 50, endpoint=True)
    plt.plot(x1_new,h(x1_new,*Werte),'-',linewidth=1, linestyle="--", color='blue')
    print(Werte)
    print(np.diag(Fehler**2)**(1/4))

    #return array(Werte), array(Fehler)


#######################################

if __name__=="__main__":
    import numpy as np
    import sympy
    import matplotlib.pyplot as plt
    from scipy.optimize import curve_fit
    from pylab import figure, axes, pie, title, show
    from numpy import NaN, Inf, arange, isscalar, asarray, array
    import sys

    y = np.loadtxt('tabelle75.txt', unpack=True,delimiter=' ')
    c = 343.28
    l = c / y
    k=(2*np.pi)/l
    w = 2*np.pi *y
    def f(k,a,b):
        return a*k+b
    Werte, Fehler = curve_fit(f, k, y)
    print(Werte)
    print(np.diag(Fehler**2)**(1/4))
    k_new = np.linspace(k[0], k[-1], 500)
    plt.figure(3)
    plt.plot(k_new,f(k_new,*Werte),'-', color="red")#, label='Fitfunktion $\Delta f \sim 1/d$')

    x1=1.09820298 ,220.15417888
    y1=1710,1710
    y2=2260,2260
    y3=3640,3640
    y4=4490,4490
    y5=5630,5630
    y6=6720,6720
    y7=7690,7690
    y8=8940,8940
    y9=9710,9710
    y10=11180,11180


    #Funktion u wird aufgerufen mit zwei werten. es gibt keinen Rückgarbewert
    u(x1,y1)
    u(x1,y2)
    u(x1,y3)
    u(x1,y4)
    u(x1,y5)
    u(x1,y6)
    u(x1,y7)
    u(x1,y8)
    u(x1,y9)
    u(x1,y10)


    plt.fill_between(x1, y1, y2, color='blue', alpha=.1)
    plt.fill_between(x1, y3, y4, color='blue', alpha=.1)
    plt.fill_between(x1, y5, y6, color='blue', alpha=.1)
    plt.fill_between(x1, y7, y8, color='blue', alpha=.1)
    plt.fill_between(x1, y9, y10, color='blue', alpha=.1)
    plt.plot(k,y,'x', label="Messwerte", color="red")
    plt.ylabel(r'Frequenz / Hz')
    plt.xlabel(r'k/$\frac{1}{m}$')
    plt.grid()
    plt.legend()

    plt.savefig('bla75.pdf')
    print ('Fertig')
