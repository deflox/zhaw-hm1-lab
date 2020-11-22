import numpy as np
import matplotlib.pyplot as plt
from IT19tb_WIN7_S9_Aufg2 import IT19tb_WIN7_S9_Aufg2

dx_max_values = np.zeros(1000)
dx_obs_values = np.zeros(1000)
dx_max_obs_ratio_values = np.zeros(1000)

for i in range(1000):
    A = np.random.rand(100,100)
    b = np.random.rand(100,1)
    A_ = A + (np.random.rand(100,100)/10**5)
    b_ = b + (np.random.rand(100,1)/10**5)
    
    x,x_,dx_max,dx_obs = IT19tb_WIN7_S9_Aufg2(A,A_,b,b_)
    
    dx_obs_values[i] = dx_obs
    
    if (dx_max != np.nan):
        dx_max_values[i] = dx_max
        dx_max_obs_ratio_values[i] = dx_max/dx_obs

plt.semilogy(dx_obs_values, '.', color='black', label='dx_obs')
plt.semilogy(dx_max_values, '.', color='red', label='dx_max')
plt.semilogy(dx_max_obs_ratio_values, '.', color='blue', label='dx_max/dx_obs')
plt.xlabel("Iteration")
plt.ylim(10**-5,10**8)
plt.legend()

'''
Wir denken dass die obere Schranke immer gültig ist, jedoch ist diese relativ
weit von dx_obs entfernt. (Im Durchschnitt grössenordnung x1000).
'''