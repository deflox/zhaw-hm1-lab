import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.e**(x**2)+x**(-3)-10

x_interval = np.arange(-2, 2, 0.01)
plt.plot(x_interval, f(x_interval))
plt.grid()
plt.ylim(-10, 10)