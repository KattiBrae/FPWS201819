import numpy as np
import scipy as sp
import sympy
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from pylab import figure, axes, pie, title, show, array

#print('Wellenlänge')
#d=0.052
#dd=0.002
#L=0.807
#dL=0.002
#a=1e-05
#lam =a*np.sin(np.arctan( d/L ))
#print(lam)
##ddlam= a*L /( ( L**2 + d**2 )*np.sqrt( ( d**2 ) / ( L**2 ) + 1 ))
#ddlam=1.23147972145e-05
#print(ddlam)
##dLlam= -a*d/( ( d**2 + L**2 )*np.sqrt( ( d**2 ) / ( L**2 ) + 1 ))
#dLlam=-7.93518531792e-07
#print(dLlam)
#
#print('Fehler')
#gauss= np.sqrt( (ddlam)**2*(dd)**2 + (dLlam)**2*(dL)**2 )
#print(gauss)

#rot1
#158
#160
#169
#173
#187
#192
#192
#200
#212
#224
#238
#256
#
#rot2
#70
#76
#79
#81
#82
#89
#88
#93
#96
#102
#106
#116

#d=70 /158
#print(d)
#d=76 /160
#print(d)
#d=79 /169
#print(d)
#d=81 /173
#print(d)
#d=82 /187
#print(d)
#d=89 /192
#print(d)
#d=88 /192
#print(d)
#d=93 /200
#print(d)
#d=96 /212
#print(d)
#d=102/224
#print(d)
#d=106/238
#print(d)
#d=116/256
#print(d)

#rot2/rot1
#0.4430379746835443
#0.475
#0.46745562130177515
#0.4682080924855491
#0.4385026737967914
#0.4635416666666667
#0.4583333333333333
#0.465
#0.4528301886792453
#0.45535714285714285
#0.44537815126050423
#0.453125

#d=4e-03
#L=120e-03
##n=1.4567
##lambd=643.8e-09
#n=1.4635
#lambd=480.0e-09
#Dlambda =lambd**2/(2*d)*np.sqrt(1/(n**2-1))
#print(Dlambda)

#lambd=643.8e-09                 ->
Dlambda= 4.8912559475e-11
#lambd=480.0e-09                 ->
#Dlambda= 2.69520209289e-11

#dellambda= 1/2 * Dlambda * 0.4430379746835443
#print(dellambda)
#dellambda= 1/2 * Dlambda * 0.475
#print(dellambda)
#dellambda= 1/2 * Dlambda * 0.46745562130177515
#print(dellambda)
#dellambda= 1/2 * Dlambda * 0.4682080924855491
#print(dellambda)
#dellambda= 1/2 * Dlambda * 0.4385026737967914
#print(dellambda)
#dellambda= 1/2 * Dlambda * 0.4635416666666667
#print(dellambda)
#dellambda= 1/2 * Dlambda * 0.4583333333333333
#print(dellambda)
#dellambda= 1/2 * Dlambda * 0.465
#print(dellambda)
#dellambda= 1/2 * Dlambda * 0.4528301886792453
#print(dellambda)
#dellambda= 1/2 * Dlambda * 0.45535714285714285
#print(dellambda)
#dellambda= 1/2 * Dlambda * 0.44537815126050423
#print(dellambda)
#dellambda= 1/2 * Dlambda * 0.453125
#print(dellambda)


#dellambda= 1/2 * d * Dlambda
#print(dellambda)

#Wellenlängenverschiebung rot
#1.0835060643196202e-11
#1.16167328753125e-11
#1.1432225439423077e-11
#1.1450628085187862e-11
#1.0724144056016042e-11
#1.133650466998698e-11
#1.1209128213020833e-11
#1.1372170077937501e-11
#1.1074541767924529e-11
#1.1136341666183035e-11
#1.089229265619748e-11
#1.1081751756054688e-11


N = (1.0835060643196202e-11, 1.16167328753125e-11, 1.1432225439423077e-11, 1.1450628085187862e-11, 1.0724144056016042e-11, 1.133650466998698e-11, 1.1209128213020833e-11, 1.1372170077937501e-11, 1.1074541767924529e-11, 1.1136341666183035e-11, 1.089229265619748e-11, 1.1081751756054688e-11)
mu= np.mean(N)
std= np.std(N)
print(mu, ',' , std)



#Mittelwert Wellenlängenverschiebung
#mu= 1.11801268255e-11
