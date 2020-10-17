import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 5.5/((2.0*x**2)**(1.0/3.0))

def g(x,e):
    return 10.0**5 * (2*e)**(-(x/100.0))

def h(x):
    return (10.0**(2*x)/2.0**(5*x))**2
    
x_interval = np.arange(0.1,100,0.1)    

plt.loglog(x_interval,f(x_interval), label = 'f(x)')
plt.legend()
plt.grid(which='both')
plt.show()

plt.semilogy(x_interval, g(x_interval, 0.5), label='g(x), e=0.5')
plt.semilogy(x_interval, g(x_interval, 1), label='g(x), e=1')
plt.semilogy(x_interval, g(x_interval, 2), label='g(x), e=2')
plt.semilogy(x_interval, g(x_interval, 10), label='g(x), e=10')
plt.legend()
plt.grid(which='both')
plt.show()

plt.semilogy(x_interval, h(x_interval), label='h(x)')
plt.legend()
plt.grid(which='both')
plt.show()