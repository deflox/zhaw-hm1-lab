import numpy as np
import matplotlib.pyplot as plt
from IT19tb_WIN7_S6_Aufg2 import IT19tb_WIN7_S6_Aufg

# Aufgabe 3a

'''
Polynom dritten Grades: y = x**3+x**2+x**1+x**0

x-Werte: 0,2,9,13

Gleichung:
a*(0)**3+b*(0)**2+c*(0)**1+d*(0)**0=150
a*(2)**3+b*(2)**2+c*(2)**1+d*(2)**0=104
a*(9)**3+b*(9)**2+c*(9)**1+d*(9)**0=172
a*(13)**3+b*(13)**2+c*(13)**1+d*(13)**0=152

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

x_values = np.arange(0,13,0.1)
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

'''
Abgesehen von der Beschriftungen bei der x-Achse können wir im Plot keinen
Unterschied erkennen.
'''

# Aufgabe 3c

print("Schätzungswert für 2003:", f1(6))
print("Schätzungswert für 2004:", f1(7))

# Aufgabe 3d

# für a)
x_values_a = in1
y_values_a = b
za = np.polyfit(x_values_a, y_values_a, 3)
pa = np.poly1d(za)
#print("Schätzungswert für 2003 (6): (polyfit)", pa(6))
#print("Schätzungswert für 2004 (7): (polyfit)", pa(7))

# für b)
x_values_c = in2
y_values_c = b
zc = np.polyfit(x_values_c, y_values_c, 3)
pc = np.poly1d(zc)
#print("Schätzungswert für 2003: (polyfit)", pc(2003))
#print("Schätzungswert für 2004: (polyfit)", pc(2004))

abweichung_2003_a = ((pa(6)-f1(6))/pa(6))/100
print("Prozentuale Fehlerabschätzung bei f1 (Aufgabe a) für 2003:", abweichung_2003_a)
abweichung_2004_a = ((pa(7)-f1(7))/pa(7))/100
print("Prozentuale Fehlerabschätzung bei f1 (Aufgabe a) für 2004:", abweichung_2004_a)

abweichung_2003_c = ((pc(2003)-f2(2003))/pc(2003))/100
print("Prozentuale Fehlerabschätzung bei f2 (Aufgabe c) für 2003:", abweichung_2003_c)
abweichung_2004_c = np.abs(((pc(2004)-f2(2004))/pc(2004))/100)
print("Prozentuale Fehlerabschätzung bei f2 (Aufgabe c) für 2004:", abweichung_2004_c)

'''
Unsere Lösungen aus der Aufgabe c haben eine höhere prozentuale Abweichung als bei Aufgabe a.
'''