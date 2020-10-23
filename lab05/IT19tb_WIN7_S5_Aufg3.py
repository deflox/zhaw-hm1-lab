import numpy as np
import matplotlib.pyplot as plt

def IT19tb_WIN7_S1_Aufg3(f, x0, x1, tol):
    for i in range(0, 1000):
        new = x1-(x1-x0)/(f(x1)-f(x0))*f(x1)
        if np.abs(new - x1) < tol:
            return new
        x0 = x1
        x1 = new