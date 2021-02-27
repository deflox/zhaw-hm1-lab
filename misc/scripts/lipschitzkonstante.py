import numpy as np
import matplotlib.pyplot as plt

interval_start = 1
interval_end   = 2
startpunkt = 1.5

def F(x):  return (1./(np.cos(x+(np.pi/4.)) - 1)) + 2.
def dF(x): return (np.sin(x+(np.pi/4.)))/((np.cos(x+(np.pi/4.))-1)**2)
def f(x):  return x

x_values = np.arange(interval_start,interval_end,0.00001)

plt.plot(x_values,F(x_values),label='F(x)')
plt.plot(x_values,dF(x_values),label='dF(x)')
plt.plot(x_values,f(x_values),label='f(x)=x')
plt.grid()
plt.legend()

# identify lipschitz constant
y_values = dF(x_values)
lipschitz_const = np.max(np.abs(y_values))

print('Leipschitz Konstante (grösste Steigung): ', lipschitz_const)
print('Resultat Interval Start ' + str(interval_start) + ' -->', F(interval_start))
print('Resultat Interval End ' + str(interval_end) + ' -->', F(interval_end))

print('')

print('Konvergiert für Startpunkt:', dF(startpunkt)<1)
print('Leipschitz Konstante < 1 :', lipschitz_const<1)
print('Start <= yStart', interval_start<=F(interval_start))
print('End >= yEnd', interval_end>=F(interval_end))

x0 = startpunkt
x1 = F(startpunkt)
abs_err = 1e-7
steps = np.log((abs_err*(1-lipschitz_const))/(np.abs(x1-x0)))/np.log(lipschitz_const)
print('Anzahl geschätzter Schritte laut A-Priori Abschätzung:', np.ceil(steps))