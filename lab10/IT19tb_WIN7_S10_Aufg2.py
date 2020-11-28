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

R = np.triu(A,1)
L = np.tril(A,-1)
D = np.diagflat(np.diag(A,0))

print('(L+D)^-1 = \n', np.linalg.inv(L+D))
print('-(L+D)^-1 * R = \n', np.matmul(-1*np.linalg.inv(L+D),R))
print('(L+D)^-1 * b = \n', np.matmul(np.linalg.inv(L+D),b))

B = np.matmul(-1*np.linalg.inv(L+D),R)
C = np.matmul(np.linalg.inv(L+D),b)

x = np.array([
    [1.],
    [-1.],
    [3.],
]);

for i in range(3):
    x = np.matmul(B,x) + C
    print('X = \n', x)