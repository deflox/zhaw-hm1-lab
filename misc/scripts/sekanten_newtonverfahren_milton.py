# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 19:28:01 2021

@author: milto
"""

import numpy as np

# Polynomfunktion
def f(x): 
     return np.exp(x**2) + x**-3 - 10
    
# Die Ableitungs von f(x)
def f_ABL(x): 
     return 2*x*np.exp(x**2) + -3*x**-4

def Sekant_verfahren(f, x0, x1, tol):
    x2 = x1 - (((x1 - x0)/(f(x1) - f(x0))) * f(x1))
    i = 0
    while 0 < (f(x2 + tol) * f(x2 - tol)): # Abbruchverfahren
        i+=1
        x2 = x1 - (((x1 - x0)/(f(x1) - f(x0))) * f(x1))
        x0 = x1
        x1 = x2
        print('x', i, ': ', x2, sep='')
    return x2


# newton verfahren mit crazy abbruchsbedingung
def Newton_Verfahren(f,x0,tol):
    x1 = x0 - (f(x0)/f_ABL(x0))
    i = 0
    while 0 < (f(x1 + tol) * f(x1 - tol)):
        x1 = x0 - (f(x0)/f_ABL(x0))
        x0 = x1
        print('x', i, ': ', x1, sep='')
    return x1

# andere abbruchsbedingung als oben (eine die ich checke)
def Newton_Verfahren_2(f,x0,tol):
    x1 = x0 - (f(x0)/f_ABL(x0))
    i = 0
    diff = np.inf
    while diff>tol:
        x1 = x0 - (f(x0)/f_ABL(x0))
        diff = np.abs(x1 - x0)
        x0 = x1
        print('x', i, ': ', x1, sep='')
    return x1


print('Die 0-Stelle mit Sekantenverfahren ist:',Sekant_verfahren(f,-1,-1.2,10**-4))
print()
print ('Newtonverfahren:', Newton_Verfahren(f,2,10**-4))
print()
print ('Newtonverfahren 2:', Newton_Verfahren_2(f,2,10**-4))