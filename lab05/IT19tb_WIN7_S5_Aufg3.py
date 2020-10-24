import numpy as np

def IT19tb_WIN7_S1_Aufg3(f, x0, x1, tol):
    for i in range(0, 20):
        new = x1-(x1-x0)/(f(x1)-f(x0))*f(x1)
        if np.abs(new - x1) < tol:
            return new
        x0 = x1
        x1 = new
        
def a1(x):
    return np.e**(x**2)+x**(-3)-10

print("Nullstelle aus Aufgabe 1:", IT19tb_WIN7_S1_Aufg3(a1, -1.0, -1.2, 1e-6))