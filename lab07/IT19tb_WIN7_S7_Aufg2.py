import numpy as np
import scipy as sp
from scipy import linalg

# Aufgabe 2a
A = np.array([
    [0.8,2.2,3.6],
    [2.,3.,4.],
    [1.2,2.,5.8]
])
R = np.array([
    [2.,3.,4.],
    [0,1.,2.],
    [0,0,3.]
])
L = np.array([
    [1.,0,0],
    [0.4,1,0],
    [0.6,0.2,1.]
])
P = np.array([
    [0,1.,0],
    [1.,0,0],
    [0,0,1.]
])

b = np.array([2.4,1.,4.])

print(np.matmul(L,R))
print(np.matmul(P,A))

# Aufgabe 2c
print("Aufgabe 2c")
A_complete = np.array([
    [0.8,2.2,3.6,2.4],
    [2.,3.,4.,1.],
    [1.2,2.,5.8,4.]
])

p,l,u = linalg.lu(A_complete)

print("P=", p)
print("L=", l)
print("R=", u)

print("Solution: ", np.linalg.solve(A,b))