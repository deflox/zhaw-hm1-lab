import numpy as np
from IT19tb_WIN7_S10_Aufg3 import IT19tb_WIN7_S10_Aufg3a

# Überprüfung mittels Werten aus Aufgabe 1


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

x0 = np.array([
    [1.],
    [-1.],
    [3.],
]);

x,n,n2 = IT19tb_WIN7_S10_Aufg3a(A,b,x0,10**-1,2)

print('n:', n)
print('n2:', n2)
print('x: \n', x)

# Aufgabe 3b

dim  = 3000
A    = np.diag(np.diag(np.ones((dim,dim))*4000))+np.ones((dim,dim))
dum1 = np.arange(1,np.int(dim/2+1),dtype=np.float64).reshape((np.int(dim/2),1))
dum2 = np.arange(np.int(dim/2),0,-1,dtype=np.float64).reshape((np.int(dim/2),1))
x    = np.append(dum1,dum2,axis=0)
b    = A@x
x0   = np.zeros((dim,1))
tol  = 1e-4

'''
start = time.time()
x1, n1, xn1 = IT19tb_WIN03_S10_Aufg3a(A,b,x0,tol,'J')
stop = time.time()
t1 = stop-start

start = time.time()
x2, n2, xn2 = IT19tb_WIN03_S10_Aufg3a(A,b,x0,tol,'GS')
stop = time.time()
t2 = stop-start
'''