#######################################
def LeseTabelle(Name): #Funktion u
    a, b = np.loadtxt(Name, unpack=True,delimiter=' ')
    return (a,b)
#######################################
def getlenght(yA):
    a=0
    for i in range(len(yA)):
        a=a+len(yA[i])
    return a
######################################
#Oberfläschenspannung
def getY(yA):                       #yA ist ein Array gefüllt mit den Arrays aus den Dateien
    y=[]
    for i in range(len(yA)):        #zählt die einzelnen Arrays hoch
        for x in yA[i]:             #speichert die einzelnen Elemente in das Array y
            y.append(x)
    return(y)
#####################################
#Zeit
def getX(yA):
    X=[]
    x=0
    while (x<getlenght(yA)):        #Array mit der Zeit, zählt mit jeder Zeile eine Sekunde hoch
        x=x+1
        X.append(x)
    print(X)
    return(X)
#####################################
def makeArray(a):
    A = []
    for b in a:
        A.append(b)
    return (A)
####################################
def plot():
    XAchse = getX(yA)
    YAchse = getY(yA)

    plt.plot(XAchse,YAchse,'x')
    #plt.legend()
    plt.ylabel(r'Oberflächenspannung $\sigma$ $mN/m^2$')
    plt.xlabel(r'Zeit / s')
    plt.grid()
    plt.savefig('C3F8_ohneDPPA_Reihe1.pdf')
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
    a, b = LeseTabelle('KathiTabelle1.txt')
    c, d = LeseTabelle('KathiTabelle2.txt') #Kurzer
    A=makeArray(a)
    B=makeArray(b)
    C=makeArray(c)
    D=makeArray(d)

    C.append(1e20)
    X=[]
    i=0
    j=0
    h=0
    while(i<len(D)):

        while(A[j]<C[i+1]):
            X.append(D[i])
            j=j+1
            if (j==len(A)):
                break

        i=i+1
    print(X)









    '''

        #print(A[j]   ,C[i+1],B[j]   ,D[i])
        #print(A[j+1] ,C[i+1],B[j+1] ,D[i])
        #print(A[j+2] ,C[i+2],B[j+2] ,D[i+1])
        #print(A[j+3] ,C[i+2],B[j+3] ,D[i+1])
        #print(A[j+4] ,C[i+3],B[j+4] ,D[i+2])
        #print(A[j+5] ,C[i+3],B[j+5] ,D[i+2])
        #print(A[j+6] ,C[i+3],B[j+6] ,D[i+2])
        #print(A[j+7] ,C[i+3],B[j+7] ,D[i+2])
        #print(A[j+8] ,C[i+4],B[j+8] ,D[i+3])
        #print(A[j+9] ,C[i+4],B[j+9] ,D[i+3])
        #print(A[j+10],C[i+4],B[j+10],D[i+3])
        #print(A[j+11],C[i+5],B[j+11],D[i+4])



    print(C)
    C.append(C[-1]+1)
    C.append(C[-1]+1)
    print(C)

    i=0
    j=0
    Druck=[]
    print(len(A))
    while (i+1<len(C)):
        while (C[i+1]>A[j]):
            Druck.append(D[i])
            print (i,j)
            j=j+1

        i=i+1
    ###########
    print(Druck)



#Solange wie C kleiner ist als A Soll der wert von D in ein Array
    druck = []
    i=0
    j=0
    while (i<len(C)):
        if (i==0):
            druck.append(D[0])
            break
        if (C[i]<A[i+1] and C[i]>A[i-1]):
            druck.append(D[j])
            break
        if (C[i]>=A[i]):
            j=j+1
            break
        i=i+1

    print(druck)
    '''
