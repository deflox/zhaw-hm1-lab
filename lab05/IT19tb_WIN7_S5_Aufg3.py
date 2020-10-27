import numpy as np

def IT19tb_WIN7_S1_Aufg3(f, x0, x1, tol):
    new = x1-(x1-x0)/(f(x1)-f(x0))*f(x1)
    while np.abs(x0 - x1) > tol:
        new = x1-(x1-x0)/(f(x1)-f(x0))*f(x1)
        x0 = x1
        x1 = new
    return new
        
def a1(x):
    return np.e**(x**2)+x**(-3)-10

def a2(h):
    return (-(1./3.))*np.pi*h**3 + np.pi*5*h**2 - (((4./3.)*np.pi*5**3)-472);

print("Nullstelle aus Aufgabe 1:", IT19tb_WIN7_S1_Aufg3(a1, -1.0, -1.2, 1e-6))
print("Nullstelle aus Aufgabe 2:", IT19tb_WIN7_S1_Aufg3(a2, 1.7, 1.9, 1e-6))

'''
Wir würden beim Versuch das Newton-Verfahren zu implementieren auf die
Schwierigkeit stossen, dass wir noch die Ableitung der jeweiligen Funktion
benötigen. Eine Lösung wäre, dass man die Ableitung als Funktionsparameter
übergibt, was aber wahrscheinlich nicht das Ziel wäre, da es nicht immer
einfach ist, die Ableitung zu finden.

'''