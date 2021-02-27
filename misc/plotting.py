import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)

x_values = np.arange(0,2*np.pi,0.01)

plt.plot(x_values,f(x_values),label='sin(x)')
plt.ylim(-2,2)
plt.xlim(0,10)
plt.xticks(np.arange(0,5,1))
plt.yticks(np.arange(0,5,1))
plt.xlabel('x-Werte')
plt.ylabel('y-Werte')
plt.legend()
plt.grid()
plt.show()