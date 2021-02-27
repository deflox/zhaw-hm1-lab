import numpy as np

def qr_verfahren(A):
    
    A = np.copy(A)                       #necessary to prevent changes in the original matrix A_in
    A = A.astype('float64')              #change to float
    
    n = np.shape(A)[0]
    
    if n != np.shape(A)[1]:
        raise Exception('Matrix is not square') 
    
    Q = np.eye(n)
    R = A
    
    for j in np.arange(0,n-1):
        a = np.copy(R[:,j][j:]).reshape(n-j,1) # spaltenvektor des neuen R's
        e = np.eye(n-j)[:,0].reshape(n-j,1) # spalte der einheitsmatrix
        length_a = np.linalg.norm(a) # länge des spalten vektors
        if a[0] >= 0: sig = 1
        else: sig = -1
        v = a + (sig * length_a * e)
        u = v/np.linalg.norm(v)
        H = np.eye(n-j) - (2 * np.matmul(u,np.transpose(u)))
        Qi = np.eye(n)
        Qi[j:,j:] = H
        R = np.matmul(Qi,R)
        Q = np.matmul(Q,np.transpose(Qi))
        
    return(Q,R)