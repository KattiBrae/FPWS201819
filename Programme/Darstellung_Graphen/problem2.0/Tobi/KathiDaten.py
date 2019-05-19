#######################################
def LeseTabelle(Name): #Funktion u
    a, b = np.loadtxt(Name, unpack=True,delimiter=' ')
    return (a,b)

#####################################
def makeArray(a):
    A = []
    for b in a:
        A.append(b)
    return (A)

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

    print(druck)
    '''
