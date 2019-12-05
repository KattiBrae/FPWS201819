import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import uncertainties.unumpy as unp
import uncertainties
import scipy.constants as const
from uncertainties.unumpy import (nominal_values as noms, std_devs as stds)

def activity(A_0, tau, t):
    return  A_0*unp.exp(-np.log(2)*t/tau)

def avg_loss(energy, params, covariance_matrix):
    uncertainties = np.sqrt(np.diag(covariance_matrix))
    a = unp.uarray(params[0], uncertainties[0])
    b = unp.uarray(params[1], uncertainties[1])
    
    kappa = energy/b
    return kappa, b

def diffWQ_table(angle, counts, time , exp, theo):
    if len(angle) != len(counts) != len(time):
        print("Länge der Arrays stimmt nicht überein!")
        return 0
    file = open("../content/data/tables/Txt/diffWQ.txt", "w")
    dOds = "\left(\\frac{\symup{d}$\sigma$}{\symup{d}$\Omega$}\\right)"
    string = "Theta N t " +dOds+"_{\\text{exp}} "+dOds+"_{\\text{theo}}"
    file.write(string)
    file.write("° - s $m^2$ $m^2$ \n")
    for i in range(len(angle)):
        string = str(angle[i]) + " " + str(counts[i]) + " " + str(time[i]) + " " + str(exp[i]) + " " + str(theo[i]) + "\n"
        file.write(string)


def Plot(x=[], y=[], limx=None, limy=None, xname='', yname='', name='', markername='Wertepaare', marker='rx', linear=True, linecolor='b-', linename='Ausgleichsgerade', xscale=1, yscale=1, save=True, Plot=True):
	uParams = None
	if(Plot):
		dx = abs(x[-1]-x[0])
		if(limx==None):
			xplot = np.linspace((x[0]-0.05*dx)*xscale,(x[-1]+0.05*dx)*xscale,1000)
		else:
			xplot = np.linspace(limx[0]*xscale,limx[1]*xscale,1000)
		if(save):
			plt.cla()
			plt.clf()
		plt.errorbar(noms(x)*xscale, noms(y)*yscale, xerr=stds(x)*xscale, yerr=stds(y)*yscale, fmt=marker, markersize=6, elinewidth=0.5, capsize=2, capthick=0.5, ecolor='g',barsabove=True ,label=markername)
	if(linear == True):
		params, covar = curve_fit(Line, noms(x), noms(y))
		uParams=uncertainties.correlated_values(params, covar)
		if(Plot):
			plt.plot(xplot*xscale, Line(xplot, *params)*yscale, linecolor, label=linename)
	if(Plot):
		if(limx==None):
			plt.xlim((x[0]-0.05*dx)*xscale,(x[-1]+0.05*dx)*xscale)
		else:
			plt.xlim(limx[0]*xscale,limx[1]*xscale)
		if(limy != None):
			plt.ylim(limy[0]*yscale,limy[1]*yscale)
		plt.xlabel(xname)
		plt.ylabel(yname)
		plt.legend(loc='best')
		plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
		if(save):
			plt.savefig('build/'+name+'.pdf')
	if(linear):
		return(uParams)