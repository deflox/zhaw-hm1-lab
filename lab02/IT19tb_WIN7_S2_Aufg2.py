import numpy as np
import matplotlib.pyplot as plt

# Aufgabe 2a
# Bei der f2() unterscheidet sich der Plot von f1() da bei der Rechnung (x-2)^7 die Werte von x
# und 2 so nah beieinander liegen. Dies führt zu Fehlern bei der Berechnung und die Resultate
# werden verfälscht. Bei f1() hingegen ist dies nicht der Fall, da x hier an mehreren Rechenstellen
# benutzt wird.

def f1(x):
    return x**7 - 14*x**6 + 84*x**5 - 280*x**4 + 560*x**3 - 672*x**2 + 448*x - 128

def f2(x):
    return (x-2)**7

x_interval = np.linspace(1.99, 2.01, 501)

#plt.plot(x_interval, f1(x_interval), color = 'blue')
#plt.plot(x_interval, f2(x_interval), color = 'red')

# Aufgabe 2b

def g1(x):
    return x/(np.sin(1.0+x)-np.sin(1.0))

x_interval = np.arange(-10**-14, 10**-14, 1*10**-17)

#plt.plot(x_interval, g1(x_interval))

# Aufgabe 2c

def g2(x):
    return x / (2.0 * np.cos( (2.0+x) / 2.0 ) * np.sin( (x) / 2.0 ))

plt.plot(x_interval, g2(x_interval))

plt.show()