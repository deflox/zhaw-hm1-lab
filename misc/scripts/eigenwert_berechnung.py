import numpy as np

A = np.array([
    [1,-2,0],
    [2,0,1],
    [0,-2,1],
],dtype=np.float)

P = np.identity(np.shape(A)[0])

N_max = 50
for i in range(0, N_max+1):
    Q,R = np.linalg.qr(A)
    A = np.matmul(R,Q)
    P = np.matmul(P,Q)
    if (i % 10 == 0):
        print('i = ', i)
        print('Ai = \n', A)
        print()