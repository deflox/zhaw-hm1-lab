import numpy as np
from IT19tb_WIN7_S6_Aufg2 import IT19tb_WIN7_S6_Aufg

A = np.array([
    [20,30,10],
    [10,17,6],
    [2,3,2]
])

b = np.array([5.2,3,0.76])

print(IT19tb_WIN7_S6_Aufg(A,b)[2])

# multiply matrices
L = np.array([
    [1,0,0],
    [0.5,1,0],
    [0.1,0,1],
])
R = np.array([
    [20,30,10],
    [0,2,1],
    [0,0,1],
])
ALR = np.matmul(L,R)
print(ALR)