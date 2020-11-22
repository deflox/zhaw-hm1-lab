import numpy as np
from IT19tb_WIN7_S9_Aufg2 import IT19tb_WIN7_S9_Aufg2

A = np.array([
    [20.,30.,10.],
    [10.,17.,6.],
    [2.,3.,2.],    
])

A_ = np.array([
    [20.1,30.1,10.1],
    [10.1,17.1,6.1],
    [2.1,3.1,2.1],    
])

b = np.array([5720.,3300.,836.])
b_ = np.array([5620.,3300.,836.])

x,x_,dx_max,dx_obs = IT19tb_WIN7_S9_Aufg2(A,A_,b,b_)

print("x: \n", x)
print("x_: \n", x_)
print("Maximale relativer Fehler:", dx_max)
print("Tatsächlicher relativer Fehler:", dx_obs)
print("Maximale relativer Fehler in Prozent:", np.round(dx_max*100,2), '%')
print("Tatsächlicher relativer Fehler in Prozent:", np.round(dx_obs*100,2), '%')