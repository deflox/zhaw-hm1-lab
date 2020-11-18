import numpy as np

def IT19tb_WIN7_S9_Aufg2(A,A_,b,b_):
    A = A.astype('float64')
    A_ = A_.astype('float64')
    b = b.astype('float64')
    b_ = b_.astype('float64')
    
    x = np.linalg.solve(A, b)
    x_ = np.linalg.solve(A_, b_)
    
    dx_max = "NaN"
    dx_obs = np.linalg.norm((x-x_),np.inf)/np.linalg.norm(x,np.inf)
    
    condA = np.linalg.cond(A,np.inf)
    A_rel = (np.linalg.norm((A-A_),np.inf))/(np.linalg.norm(A,np.inf))
    
    if (condA * A_rel < 1):
        dx_max = ( condA / (1 - condA * A_rel) ) * ( A_rel + ((np.linalg.norm((b-b_),np.inf))/(np.linalg.norm(b,np.inf))) )
    
    return x,x_,dx_max,dx_obs