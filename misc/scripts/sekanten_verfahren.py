import numpy as np

def sekanten_verfahren(f, x0, x1, tol):
    new = x1-(x1-x0)/(f(x1)-f(x0))*f(x1)
    while np.abs(x0 - x1) > tol:
        new = x1-(x1-x0)/(f(x1)-f(x0))*f(x1)
        x0 = x1
        x1 = new
    return new