import numpy as np
import matplotlib.pyplot as plt

test = np.array([1,2,3],dtype=np.float)

#print(test.transpose())

A = np.array([
    [2,0,1],
    [7,-5,9],
    [6,-6,9],
],dtype=np.float)

T = np.array([
    [3,1,1],
    [-1,1,2],
    [-3,0,1],
],dtype=np.float)

T_inv = np.array([
    [1,-1,1],
    [-5,6,-7],
    [3,-3,4],
],dtype=np.float)

#print(np.matmul(np.matmul(T_inv,A),T))

A = np.array([
    [1,-2,0],
    [2,0,1],
    [0,-2,1],
],dtype=np.float)

ew,ev = np.linalg.eig(A)
print(ew)