import numpy as np

# from IT19tb_WIN7_S10_Aufg3 import IT19tb_WIN7_S10_Aufg3a

A = np.array([
    [8.,5.,2.],
    [5.,9.,1.],
    [4.,2.,7.],
])

print('np.diag(A,0): \n', np.diag(A,0))
print('np.triu(A,1): \n', np.triu(A,1))
print('np.tril(A,1): \n', np.tril(A,-1))

test_vector = np.array([1,2,3])
print('np.diagflat(input): \n', np.diagflat(test_vector))

print('np.linalg.inf(A): \n', np.linalg.inv(A))

x = 5.5
print('np.floor(x):', np.floor(x))
print('np.ceil(x):', np.ceil(x))