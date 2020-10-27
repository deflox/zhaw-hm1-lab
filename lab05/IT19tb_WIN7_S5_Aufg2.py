import numpy as np

# Newton 

def f(h):
    return (-(1./3.))*np.pi*h**3 + np.pi*5*h**2 - (((4./3.)*np.pi*5**3)-472);

def f_diff(h):
    return -np.pi*h**2 + 2*np.pi*5*h

h_alt = 1
for i in range(0,10):
    h_neu = h_alt - (f(h_alt)/f_diff(h_alt))
    print(h_neu)
    h_alt = np.round(h_neu,4)