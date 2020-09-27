import numpy as np
import matplotlib.pyplot as plt

# plot polynomial function

def f(x):
    return x**5 - 5*x**4 - 30*x**3 + 110*x**2 + 29*x - 105

def fDiff(x):
    return 5*x**4 - 20*x**3 - 90*x**2 + 220*x + 29

def F(x):
    return (1/6)*x**6 - x**5 - (7.5)*x**4 + (110/3)*x**3 + (29/2)*x**2 - 105*x + 0

x_interval = np.arange(-10.0, 10.0, 0.1)

plt.plot(x_interval, f(x_interval), color = 'blue', label='f  (x)')
plt.plot(x_interval, fDiff(x_interval), color = 'red', label='f\' (x)')
plt.plot(x_interval, F(x_interval), color = 'green', label='F (x)')
plt.ylim(-1300, 1300)
plt.xlim(-8, 8)
plt.grid(which = 'both')
plt.xlabel("X-Werte")
plt.ylabel("Errechnete Y-Werte")
plt.legend()
plt.show()