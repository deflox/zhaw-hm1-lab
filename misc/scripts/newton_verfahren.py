import numpy as np

def newton_verfahren(f,dF,x0,tol):
    c = 0
    xn = x0
    xn_1 = xn - (f(xn))/(dF(xn))
    while np.abs(xn_1-xn) > tol:
        c += 1
        print('xn_'+str(c)+':', xn_1)
        xn = xn_1
        xn_1 = xn - (f(xn))/(dF(xn))
        
def f(x): return np.exp(x**2) + x**(-3) - 10
def dF(x): return 2*np.exp(x**2)*x-(3)/(x**4)

x0 = 2
tol = 1e-9

newton_verfahren(f,dF,x0,tol)