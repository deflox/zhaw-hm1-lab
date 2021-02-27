# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 16:35:12 2021

@author: milto
"""

import numpy as np
import numpy.linalg as lg

A = np.array([[10.0**(-5), 10.0**(-5)],
              [2.0, 3.0]], dtype=np.float32)

Z= np.array([[30, 0, 0],
             [0, 100, 0],
             [0, 0, 50]], dtype=np.float32)


b = np.array([10.0**-5,1.0], dtype=np.float32)

# Matrixinverse berechnen
print('Matrix-Inverse of A:\n',np.linalg.inv(A))
print('Matrix-Inverse of Z:\n',np.linalg.inv(Z))

# Matrix: 1-Norm & infinity Norm
print('cond(A)_1:', np.linalg.cond(A,1))
print('cond(A)_Infty:', np.linalg.cond(A,np.inf))


# Gleichungssystem lösen (Gauss)
print('Solve - Ax=b :',np.linalg.solve(A,b))

# Vektor: 1-Norm
print('Vektor 1-Norm:',lg.norm(np.array([-1,1]),1))

print(
      lg.norm((np.linalg.solve(A,b) - np.array([-1,1])),1)
      / lg.norm(np.array([-1,1]),1)
      )
