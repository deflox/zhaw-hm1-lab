import numpy as np
from IT19tb_WIN7_S6_Aufg2 import IT19tb_WIN7_S6_Aufg

A1 = np.array([
    [4, -1, -5], 
    [-12,4,17], 
    [32,-10,-41]
])

b1 = np.array([-5,19,-39])

print(IT19tb_WIN7_S6_Aufg(A1,b1)[2])
print(np.linalg.solve(A1,b1))

A2 = np.array([
    [2,7,3], 
    [-4,-10,0], 
    [12,34,9]
])
b2 = np.array([25,-24,107])

print(IT19tb_WIN7_S6_Aufg(A2,b2)[2])
print(np.linalg.solve(A2,b2))

A3 = np.array([
    [-2, 5, 4], 
    [-14,38,22], 
    [6,-9,-27]
])
b3 = np.array([1,40,75])

print(IT19tb_WIN7_S6_Aufg(A3,b3)[2])
print(np.linalg.solve(A3,b3))

A4 = np.array([
    [-1, 2, 3, 2, 5, 4, 3, -1], 
    [3, 4, 2, 1, 0, 2, 3, 8], 
    [2, 7,5, -1, 2, 1, 3, 5],
    [3, 1, 2, 6, -3, 7, 2, -2], 
    [5, 2, 0, 8, 7, 6, 1, 3], 
    [-1, 3, 2, 3, 5, 3, 1, 4],
    [8, 7, 3, 6, 4, 9, 7, 9], 
    [-3, 14, -2, 1, 0, -2, 10, 5]
])
b4 = np.array([-11, 103, 53, -20, 95, 78, 131, -26])

print(IT19tb_WIN7_S6_Aufg(A4,b4)[2])
print(np.linalg.solve(A4,b4))

'''
Mit der Matrix A4 erhalten ein Resultat mit einem sehr kleinen Wert: 5.32907052e-14 an der Stelle
3 im Resultatsvektor x. Mit numpy linalg solve erhalten wir an der gleichen Stelle einen anderen sehr 
kleinen Wert: 3.9245093e-16. Die restlichen Werte sind bei allen Aufgaben gleich.
'''