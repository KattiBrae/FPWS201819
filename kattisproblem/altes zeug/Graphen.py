#######################################  Funktion u
#def u(x,y): #Funktion u
#
#    def h(x,a,b):
#        return a*x+b
#    Werte, Fehler = curve_fit(h, x, y)
#
#    x1_new = np.linspace(x1[0], x1[-1], 50, endpoint=True)
#    plt.plot(x1_new,h(x1_new,*Werte),'-',linewidth=1, linestyle="--", color='blue')
#    print(Werte)
#    print(np.diag(Fehler**2)**(1/4))
#
#    #return array(Werte), array(Fehler)
#

#######################################

if __name__=="__main__":
    import numpy as np
    import sympy
    import matplotlib.pyplot as plt
    from scipy.optimize import curve_fit
    from pylab import figure, axes, pie, title, show
    from numpy import NaN, Inf, arange, isscalar, asarray, array
    import sys

    


    date1, b1, sigma1 = np.loadtxt('C3F8_ohneDPPA_1021.txt', unpack=True,delimiter=' ')
    pressure1 = np.full((len(sigma1), 1), 1.021)
    time1 = np.arange(0, len(sigma1), 1 )
    plt.plot(time1, sigma1,'x', label="Messwerte", color="red")

    date2, b2, sigma2 = np.loadtxt('C3F8_ohneDPPA_1250.txt', unpack=True,delimiter=' ')
    pressure2 = np.full((len(sigma2), 1), 1.250)
    time2 = np.arange(len(time1), len(sigma2)+len(time1), 1 )
    plt.plot(time2, sigma2,'x', color="red")

    date3, b3, sigma3 = np.loadtxt('C3F8_ohneDPPA_1500.txt', unpack=True,delimiter=' ')
    pressure3 = np.full((len(sigma3), 1), 1.500)
    time3 = np.arange(len(time2)+len(time1), len(sigma3)+len(time2)+len(time1), 1 )
    plt.plot(time3, sigma3,'x', color="red")

    date4, b4, sigma4 = np.loadtxt('C3F8_ohneDPPA_1751.txt', unpack=True,delimiter=' ')
    pressure4 = np.full((len(sigma4), 1), 1.751)
    time4 = np.arange(len(time3)+len(time2)+len(time1), len(sigma4)+len(time3)+len(time2)+len(time1), 1 )
    plt.plot(time4, sigma4,'x', color="red")

    date5, b5, sigma5 = np.loadtxt('C3F8_ohneDPPA_1999.txt', unpack=True,delimiter=' ')
    pressure5 = np.full((len(sigma5), 1), 1.999)
    time5 = np.arange(len(time4)+len(time3)+len(time2)+len(time1), len(sigma5)+len(time4)+len(time3)+len(time2)+len(time1), 1 )
    plt.plot(time5, sigma5,'x', color="red")

    date6, b6, sigma6 = np.loadtxt('C3F8_ohneDPPA_2250.txt', unpack=True,delimiter=' ')
    pressure6 = np.full((len(sigma6), 1), 2.250)
    time6 = np.arange(len(time5)+len(time4)+len(time3)+len(time2)+len(time1), len(sigma6)+len(time5)+len(time4)+len(time3)+len(time2)+len(time1), 1 )
    plt.plot(time6, sigma6,'x', color="red")




    #def f(k,a,b):
    #    return a*k+b
    #Werte, Fehler = curve_fit(f, k, y)
    #print(Werte)
    #print(np.diag(Fehler**2)**(1/4))
    #k_new = np.linspace(k[0], k[-1], 500)
    #plt.figure(3)
    #plt.plot(k_new,f(k_new,*Werte),'-', color="red")#, label='Fitfunktion $\Delta f \sim 1/d$')


#    plt.fill_between(x1, y1, y2, color='blue', alpha=.1)                                                    #fült die fläche zwischen Graphen
#    plt.fill_between(x1, y3, y4, color='blue', alpha=.1)
#    plt.fill_between(x1, y5, y6, color='blue', alpha=.1)
#    plt.plot(time, sigma,'x', label="Messwerte", color="red")
    plt.ylabel(r'Oberflächenspannung $\sigma$ $mN/m^2$')
    plt.xlabel(r'Zeit / s')
    plt.grid()
    plt.legend()

    plt.savefig('bla.pdf')
    print ('Fertig')
