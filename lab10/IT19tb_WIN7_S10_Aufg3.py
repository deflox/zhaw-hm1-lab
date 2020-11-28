import numpy as np

'''
Berechnet iterativ die Lösung des Gleichungssystems Ax=b bis zur Genauigkeit tol.

Operationen:
    1: Jacobi-Verfahren
    2: Gauss-Seidel Verfahren

'''
def IT19tb_WIN7_S10_Aufg3a(A,b,x0,tol,opt):
    R = np.triu(A,1)
    L = np.tril(A,-1)
    D = np.diagflat(np.diag(A,0))
    
    B = 0
    C = 0
    
    if (opt == 1):
        D_inv = np.linalg.inv(D)
        B = np.matmul(-1*D_inv,L+R)
        C = np.matmul(D_inv,b)
    elif (opt == 2):
        LD_inv = np.linalg.inv(L+D)
        B = np.matmul(-1*LD_inv,R)
        C = np.matmul(LD_inv,b)
    else:
        return 'Unknown Operation'
    
    if (np.linalg.norm(B,np.inf) >= 1):
        return 'Kein Abbrechkriterium möglich.'
    
    x_alt = np.copy(x0)
    x_neu = np.matmul(B,x_alt) + C
    
    n2_steps = np.log10( (tol*(1-np.linalg.norm(B,np.inf)))/(np.linalg.norm(x_neu-x_alt,np.inf)) ) / np.log10( np.linalg.norm(B,np.inf) );
    n2_steps = np.ceil(n2_steps)
    
    n_steps = 1
    while ( ( ((np.linalg.norm(B,np.inf)) / (1-np.linalg.norm(B,np.inf))) * np.linalg.norm(x_neu-x_alt,np.inf) ) > tol ):
        x_alt = x_neu
        x_neu = np.matmul(B,x_alt) + C
        n_steps += 1
    
    return x_neu, n_steps, n2_steps