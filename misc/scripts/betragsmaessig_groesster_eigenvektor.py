import numpy as np

A = np.array([
    [2,2,2],
    [0,3,1],
    [1,-2,1],    
],dtype=np.float)

w0 = np.array([1,2,-2],dtype=np.float)
v0 = w0 / np.linalg.norm(w0,2)

print('v0 = ', v0); print();

i_max = 20
for i in range(1,i_max+1):
    w1 = np.dot(A,v0)
    v1 = w1 / np.linalg.norm(w1,2)
    lam1 = np.dot(v0,w1)
    if i <= 5 or i % 10 == 0:
        print('i =', i); print('vi =', v1);
        print('lami =', lam1); print();
    v0 = np.copy(v1)