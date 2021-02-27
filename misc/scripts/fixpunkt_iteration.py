import numpy as np

def fixpunktiteration(f,x0,eps,lamd):
    notConverged=True
    
    k=0
    N=1000
    
    while (notConverged and k<N):
        x1=f(x0)
        incr=np.abs(x1-x0)
        error=lamd/(1-lamd)*incr
        notConverged=error>eps
        k=k+1
        x0=x1
    
    return(x1,k)

def F(x): return (1./(np.cos(x+(np.pi/4.)) - 1)) + 2.

eps = 1e-6
lamd = 0.6640946355544965
x0 = 1.1

xn, n = fixpunktiteration(F, x0, eps, lamd)

print('xn: ', xn)
print('Iterations:', n)