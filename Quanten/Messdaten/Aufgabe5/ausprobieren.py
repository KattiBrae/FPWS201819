def graph(x,y):
    plt.plot(x,y,'x', label="Messwerte", color="red")

    def f(x,a,b):
        return(a*x+b)
    Werte, Fehler = curve_fit(f, x, y)
    print(Werte)
    print(np.diag(Fehler**2)**(1/4))
    x_new = np.linspace(x[0], x[-1], 500)
    plt.figure(1)
    plt.plot(x_new,f(x_new,*Werte),'-', color="red")
#############################
def passendesX(y):
    X=[]
    x=0
    while (x<len(y)):
        x=x+1
        X.append(x)
    return(X)
#############################
def vonYzuK(y):
    c = 343.28
    l = c / y
    k=(2*np.pi)/l
    return(k)
#############################
def vonKzuY(k):
    c = 343.28
    l=(2*np.pi)/k
    y = c / l
    return(y)
#############################
def passendesY(x):
    Y=[]
    y=0
    while (y<len(x)):
        Y.append(vonKzuY(x[y]))#vonYzuK(y[x]))
        y=y+1
    return(Y)
############################
def AusDreiMachEin(a,b,c):
    y=[]
    for x in a:
        y.append(x)
    for x in b:
        y.append(x)
    for x in c:
        y.append(x)

    return(y)
##############################
def teileArray(a,b,y):     #array y wir in 3 teile geteilt
    Y1 = []
    Y2 = []
    Y3 = []
    i=0
    while (a>y[i]):
        Y1.append(y[i])
        i=i+1

    while (a<y[i] and b>y[i]):
        Y2.append(y[i])
        i=i+1

    while (b<y[i]):
        Y3.append(y[i])
        i=i+1
        if (i==len(y)):
            break

    return(Y1,Y2,Y3)
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
    #a =[2,3,4,6,7,8,9,10,12,13,14,15]     #array

    ##print (a[1])
    #print (a)


    ##o=grenzen(2,7,a)

    #x=3
    #b=[0,0,0,0] # ist das selbe wie b=[0]*4 !!!
    #B=0
    #while (x>2 and x<7):
    #    print (x, a[x])
    #    b[B]=a[x]
    #    x=x+1
    #    B=B+1

    ##b=a[3]
    ##a[3]=a[5]
    ##a[5]=b


    #print (a)
    #print (b)

    #x=3
    #B=1
    #while (x>2 and x<7):
    #    a[x]=b[len(b)-B]
    #    x=x+1
    #    B=B+1
    #print(a)


#
    y = np.loadtxt('tabelle75.txt', unpack = True , delimiter = ' ')
    Y = makeArray(y)
    k = vonYzuK(y)
    K = makeArray(k)

    #k ist die neue X-Achse
    #y ist die neue y-Achse

    ka,kb,kc = teileArray(60,100,K)
    kb.reverse()

    kd,ke,kf = teileArray(100,175,K)
    kf.reverse()

    h = AusDreiMachEin(ka,kb,kc)
    print(h)

    ya,yb,yc=teileArray(2000,4000,Y)
    yb.reverse()
    Xa=passendesX(ya)
    Xb=passendesX(yb)
    Xc=passendesX(yc)

    graph(Xa,ya)
    graph(Xb,yb)


    yd,ye,yf=teileArray(6000,8000,yc)
    ye.reverse()
    Xd=passendesX(yd)
    Xe=passendesX(ye)
    Xf=passendesX(yf)

    graph(Xd,yd)
    graph(Xe,ye)
    #graph(Xf,yf)

    yg,yh,yi=teileArray(8000,10000,yf)
    yi.reverse()
    Xg=passendesX(yg)
    Xh=passendesX(yh)
    Xi=passendesX(yi)

    graph(Xh,yh)
    graph(Xi,yi)




    #graph(k,y)

    plt.grid()
    plt.xlabel("BZ")
    plt.ylabel("Frequenz / Hz")
    plt.savefig('RedBandSchem75.pdf')
    plt.show()
    print("Fertig")




    #x=a[0]
    #a[0]=x
    #print(x)
    #a[5]=7
    #for x in a:
    #    if x==4:
    #        print ("hallo")
    #    if x>4 and x<12:
    #        print ("darzwischen")

    #x = 2
    #while x in a:       #solange x in dem array enthalten ist gieb den wert aus und +1
    #    print (x)       #eine sortierung solange die werte nur 1 auseinander liegen
    #    x=x+1

    ## in java:
    #  int b=2;
    #  for (int x; x<.length; x++)
    #  if (b==a[x]){
    #    System.out.println(b)
    #    b++
    #   }

    #for x in a:
    #    print (x)

    ##In java:
    # for (int x; x<a.length;x++){
    # System.out.println(a[x]);
    # }




    #x=8
    #b=0
    #while x in a:           #solange der wert x in dem arry ist wird dieser Wert ausgegeben
    #    #print (a[b])
    #    #b=b+1
    #    print(x)
    #    x=x+1
