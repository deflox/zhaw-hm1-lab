import numpy as np

u1 = np.array([
    [(1 + np.sqrt(30)) / np.sqrt(2*np.sqrt(30) + 60)],
    [-5 / np.sqrt(2*np.sqrt(30) + 60)],
    [2 / np.sqrt(2*np.sqrt(30) + 60)]
])

u1T = np.transpose(u1)

print (np.matmul(u1, u1T))