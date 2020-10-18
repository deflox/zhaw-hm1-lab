import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 27

def f_fix(x):
    return x 

def F(x):
    return (27/x**2)


def fixpunktiteration(k):
    prev = F(k)
    for i in range (1, 100):
        neu = F(prev)
        if np.abs(neu - prev) < 1e-6:
            return neu;
        prev = neu
    return "Nicht anziehend"

x_interval = np.arange(-2, 4, 0.1)

plt.plot(x_interval, f(x_interval), label="f(x)")
plt.plot(x_interval, f_fix(x_interval), label="f_fix(x)")
#plt.plot(x_interval, F(x_interval), label="F(x)")
plt.legend()
plt.grid()

print(fixpunktiteration(3))