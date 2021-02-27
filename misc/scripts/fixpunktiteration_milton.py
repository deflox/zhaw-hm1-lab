# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 12:13:14 2021

@author: milto
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 16:37:16 2020

@author: milto
"""

# Fixpunktiteration
# Banacher Fixpunktsatz
# Berechnung von Alpha --> 0 < a < 1


import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-5, 5, 0.1)

# (Ausgangs-)Polynom f(x)
def f(x):
    return 2**x-2*x

# Fixpunktgleichung / Fixpunktfunktion von f(x)
def F(x):
    return 2**(x-1)

# Ableitung der Fixpunktgleichung F(x)
def F_abl(x):
    return np.log(2)*2**(x-1)
# Fixpunktiteration
# Im Array sind verschiedene Startpunkte für x
xn = np.array([0, 0.5, 1.0, 1.5, 1.999,2,2.00001])
for i in range(100):
    xn = F(xn)
    print(xn)

# PLOT Fixpunktiteration
print()
plt.xlim(0, 2)
plt.ylim(-1, 1)
plt.grid()
plt.xlabel('X')
plt.ylabel('Y')
plt.plot(x, f(x))
plt.plot(x, F(x))
plt.plot(x, F_abl(x))
plt.legend(['f(x)','F(x)','F_abl'])
plt.title('Fixpunktiteration')

# PLOT Rectangle [a,b]
# Kontraktion 
[a,b] = [0-5,1.5]
#plt.plot([a, a, b, b, a],[a, b, b, a, a], '-k') # rectangle

# BERECHNUNG ALPHA:
# Alpha herausfinden: Grösste abs. Ableitung aus Intervall
xmax = np.linspace(a, b, 100)
print('Alpha:',max(np.abs(F_abl(xmax))))
alpha = max(np.abs(F_abl(xmax)))

# Min, Max, Alpha falls gegeben
#xb = np.arange(-1,1,0.1)
#print('Minimum:',F(0))
#print('Maximum:',np.abs(F(0.5)))
#print("Alpha:",np.abs(F_abl(0.5)))

# -------------------------------------------

# A priori Fehlerabschätzung
tol = 10**-8
x0 = 1.5

def a_priori_abschaetzung(x):
    return np.log(((tol)*(1-alpha))/np.abs(F(x0)-x0)) / np.log(alpha)

print('a-priori:',a_priori_abschaetzung(x),'-->',np.ceil(a_priori_abschaetzung(x)))
