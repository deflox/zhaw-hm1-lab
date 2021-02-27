import numpy as np
import matplotlib.pyplot as plt

def f(x)  : return x * np.exp(x)
def df(x) : return np.exp(x)*(x+1)
def K(x)  : return np.abs(x)*np.abs(df(x))/np.abs(f(x))

x_values = np.arange(-3,1,0.01)
plt.plot(x_values,K(x_values))
plt.grid()