import numpy as np

# Aufgabe 1b

A = np.array([
    [8.,5.,2.],
    [5.,9.,1.],
    [4.,2.,7.],
])

b = np.array([
    [19.],
    [5.],
    [34.],
])

#print('Linalg Solve: \n', np.linalg.solve(A,b))

B = np.array([
    [0,-5./8.,-2./8.],
    [-5./9.,0,-1./9.],
    [-4./7.,-2./7.,0]
])

C = np.array([
    [19./8.],
    [5./9.],
    [34./7.],
])

#print('B = \n', B)
#print('C = \n', C)

x = np.array([
    [1.],
    [-1.],
    [3.],
]);

for i in range(3):
    x = np.matmul(B,x) + C
    print('X = \n', x)