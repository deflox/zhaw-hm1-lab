import numpy as np
import matplotlib.pyplot as plt

input_a = [1,2,3]
# x^2 + 2x + 3x^0
input_xmin = -10
input_xmax = 10

def fx(a, x):
    result = 0
    for i in range (0, len(a)):
        result += a[i] * x**(len(a)-i-1)
    return result

def IT19tb_WIN7_S1_Aufg2(a, xmin, xmax):
    #step = (xmax - xmin)/10.0
    x = np.arange(xmin, xmax, 1.0)
    
    p = np.arange(len(x))
    for i in range (0, len(x)):
        p[i] = fx(a, x[i])
    
    return x,p

x,y = IT19tb_WIN7_S1_Aufg2(input_a, input_xmin, input_xmax)

plt.plot(x,y)
plt.grid()