import numpy as np
import scipy.linalg as la

A_orig = np.array([
    [1.,0,2.],
    [0,1.,0],
    [10**-4,0,10**-4],
])

B_orig = np.array([1.,1.,0])

B_disturbed = np.array([1.,1.,0.01/60003.])

P_py, L_py, R_py = la.lu(A_orig)

print('P_py = \n', P_py)
print('L_py = \n', L_py)
print('R_py = \n', R_py)

x_orig = np.linalg.solve(A_orig, B_orig)
x_disturbed = np.linalg.solve(A_orig, B_disturbed)

print('b_orig solve', x_orig)
print('b_disturbed solve:', x_disturbed)

print('x_disturbed - x_orig norm', np.linalg.norm((x_orig-x_disturbed), np.inf))

A_disturbed = np.array([
    [1.+1e-7,0+1e-7,2.+1e-7],
    [0+1e-7,1.+1e-7,0+1e-7],
    [10**-4+1e-7,0+1e-7,10**-4+1e-7],
])

print('A_orig \n', A_orig)
print('A_disturbed \n', A_disturbed)
print('A_orig - A_disturbed \n', A_orig-A_disturbed)
print('A_orig - A_disturbed norm', np.linalg.norm((A_orig-A_disturbed), np.inf))