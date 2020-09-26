import numpy as np
import matplotlib.pyplot as plt

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
    
    # calculate differentiation coefficients
    dp_cf = np.arange(len(a)-1)
    for i in range (0, len(a)-1):
        dp_cf[i] = (len(a)-i-1) * a[i]
    dp = np.arange(len(x))
    for i in range (0, len(x)):
        dp[i] = fx(dp_cf, x[i])
        
    # calculate integral coefficients
    pint_cf = np.arange(len(a) + 1)
    pint_cf[len(pint_cf)-1] = 0;
    for i in range (0, len(a)):
        pint_cf[i] = (a[i]/(len(a)-i))*float(1)
    pint = np.arange(len(x))
    for i in range (0, len(x)):
        pint[i] = fx(pint_cf, x[i])
        
    print(pint_cf)
    
    return x,p,dp,pint

input_a = [1,4,3]
# x^2 + 2x + 3
# 2x + 2
# 1/3x^3 + x^2 + 3x + 0
input_xmin = -10
input_xmax = 10

x_values, p_values, dp_values, pint_values = IT19tb_WIN7_S1_Aufg2(input_a, input_xmin, input_xmax)

plt.plot(x_values,p_values)
plt.plot(x_values,dp_values)
plt.plot(x_values,pint_values)
plt.grid()