import numpy as np

def fx(a, x):
    result = 0
    for i in range (0, len(a)):
        result += a[i] * x**(len(a)-i-1)
    return result

def IT19tb_WIN7_S1_Aufg2(a, xmin, xmax):
    x = np.arange(xmin, xmax, 1.0)

    # calculate y values for function
    p = np.arange(len(x)*float(1))
    for i in range (0, len(x)):
        p[i] = fx(a, x[i])
    
    # calculate differentiation coefficients and y values
    dp_cf = np.arange((len(a)-1)*float(1))
    for i in range (0, len(a)-1):
        dp_cf[i] = (len(a)-i-1) * a[i]
    dp = np.arange(len(x))
    for i in range (0, len(x)):
        dp[i] = fx(dp_cf, x[i])
        
    # calculate integral coefficients and y values
    pint_cf = np.arange((len(a) + 1)*float(1))
    pint_cf[len(pint_cf)-1] = 0.0;
    for i in range (0, len(a)):
        pint_cf[i] = (a[i]/(len(a)-i))
    pint = np.arange(len(x))
    for i in range (0, len(x)):
        pint[i] = fx(pint_cf, x[i])
    
    return x,p,dp,pint