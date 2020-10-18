import numpy as np
import matplotlib.pyplot as plt

def f(phi, r):
    return r + (np.cos(phi/2.)*r)

phi_interval = np.arange(0,np.pi*2,0.01)

plt.plot(phi_interval, f(phi_interval, 1))
plt.grid()