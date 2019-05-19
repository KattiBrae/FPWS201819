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

    x, y = np.loadtxt('tabelle.txt', unpack=True,delimiter=' ')
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

    x1=1.09820298 ,201.15417888
    y1=2370,2370
    y2=3330,3330
    y3=5100,5100
    y4=6630,6630
    y5=8040,8040
    y6=9880,9880

    #Funktion u wird aufgerufen mit zwei werten. es gibt keinen Rückgarbewert
    u(x1,y1)
    u(x1,y2)
    u(x1,y3)
    u(x1,y4)
    u(x1,y5)
    u(x1,y6)


#    for(int i; i<k.length; i++):
#        if (y> 2370 and y< 5100):
#            x=x-50
#            print(x)



    plt.fill_between(x1, y1, y2, color='blue', alpha=.1)
    plt.fill_between(x1, y3, y4, color='blue', alpha=.1)
    plt.fill_between(x1, y5, y6, color='blue', alpha=.1)
    plt.plot(k,y,'x', label="Messwerte", color="red")
    plt.ylabel(r'Frequenz / Hz')
    plt.xlabel(r'k /$\frac{1}{m}$')
    plt.grid()
    plt.legend()

    plt.savefig('bla.pdf')
    print ('Fertig')