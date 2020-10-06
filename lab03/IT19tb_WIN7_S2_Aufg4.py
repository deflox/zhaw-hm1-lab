import numpy as np
import matplotlib.pyplot as plt

def h(x):
    return np.sqrt(100.0*x**2-200*x+99)

def h_kondition(x):
    return (np.absolute(0.5*(200.0*x**2-200.0*x+99)**(-0.5)*200.0*x-200.0)*np.absolute(x))/(np.absolute(np.sqrt(200.0*x**2-200.0*x+99)))

# x_interval = np.arange(1.1, 1.1001, 10**-10)

#y_values = np.zeros(len(x_interval))
#for i in range(0, len(x_interval)):
#    y_values[i] = h(x_interval[i])

#plt.plot(x_interval, h(x_interval), label='h(x)')
plt.legend()
plt.grid()
plt.show()

# Aufgabe 2b

x_interval = np.arange(1.1,1.3,10**-7)

plt.semilogy(x_interval, h_kondition(x_interval), label='h_kondititon(x)')
plt.legend()
plt.grid()
plt.show()

print(100*1.1**2-200*1.1+99)