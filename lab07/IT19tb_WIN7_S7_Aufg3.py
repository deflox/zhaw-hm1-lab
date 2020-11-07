import numpy as np
import matplotlib.pyplot as plt
from IT19tb_WIN7_S6_Aufg2 import IT19tb_WIN7_S6_Aufg

# Aufgabe 3a

'''
Polynom dritten Grades: y = x**3+x**2+x**1+x**0

x-Werte: 0,2,9,13

Gleichung:
x_1(0)**3+x_2(0)**2+x_3(0)**1+x_4(0)**0=150
x_1(2)**3+x_2(2)**2+x_3(2)**1+x_4(2)**0=104
x_1(9)**3+x_2(9)**2+x_3(9)**1+x_4(9)**0=172
x_1(13)**3+x_2(13)**2+x_3(13)**1+x_4(13)**0=152

'''

in1 = np.array([0,2.,9.,13.])

A1 = np.array([
    [in1[0]**3,in1[0]**2,in1[0]**1,in1[0]**0],
    [in1[1]**3,in1[1]**2,in1[1]**1,in1[1]**0],
    [in1[2]**3,in1[2]**2,in1[2]**1,in1[2]**0],
    [in1[3]**3,in1[3]**2,in1[3]**1,in1[3]**0],
])

b = np.array([150.,104.,172.,152.])

results1 = IT19tb_WIN7_S6_Aufg(A1,b)[2]

def f1(x):
    return results1[0]*x**3 + results1[1]*x**2 + results1[2]*x + results1[3]

x_values = np.arange(0,14,0.1)
plt.plot(x_values,f1(x_values))
plt.grid()
plt.show()

# Aufgabe 3b

in2 = np.array([1997.,1999.,2006.,2010.])

A2 = np.array([
    [in2[0]**3,in2[0]**2,in2[0]**1,in2[0]**0],
    [in2[1]**3,in2[1]**2,in2[1]**1,in2[1]**0],
    [in2[2]**3,in2[2]**2,in2[2]**1,in2[2]**0],
    [in2[3]**3,in2[3]**2,in2[3]**1,in2[3]**0],
])

results2 = IT19tb_WIN7_S6_Aufg(A2,b)[2]

def f2(x):
    return results2[0]*x**3 + results2[1]*x**2 + results2[2]*x + results2[3]

x_values = np.arange(1997,2010,0.1)
plt.plot(x_values,f2(x_values))
plt.grid()
plt.show()

# Aufgabe 3c

print("Schätzungswert für 2003:", f1(6))
print("Schätzungswert für 2004:", f1(7))

# Aufgabe 3d

# für a)
x_values_a = in1
y_values_a = b
za = np.polyfit(x_values_a, y_values_a, 3)
pa = np.poly1d(za)
print("Schätzungswert für 2003 (6): (polyfit)", pa(6))
print("Schätzungswert für 2004 (7): (polyfit)", pa(7))

# für b)
x_values_b = in2
y_values_b = b
zb = np.polyfit(x_values_b, y_values_b, 3)
pb = np.poly1d(zb)
print("Schätzungswert für 2003: (polyfit)", pb(2003))
print("Schätzungswert für 2004: (polyfit)", pb(2004))