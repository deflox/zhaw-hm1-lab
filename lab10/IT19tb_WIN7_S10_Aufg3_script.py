import numpy as np
import time
import matplotlib.pyplot as plt
from IT19tb_WIN7_S10_Aufg3 import IT19tb_WIN7_S10_Aufg3a
from IT19tb_WIN7_S6_Aufg2 import IT19tb_WIN7_S6_Aufg

# Überprüfung mittels Werten aus Aufgabe 1

'''
A = np.array([
    [8.,5.,2.],
    [5.,9.,1.],
    [4.,2.,7.],
])
b = np.array([
    [19.],
    [5.],
    [34.],
])

x0 = np.array([
    [1.],
    [-1.],
    [3.],
]);


x,n,n2 = IT19tb_WIN7_S10_Aufg3a(A,b,x0,10**-4,2)

print('n:', n)
print('n2:', n2)
print('x: \n', x)
'''

# Aufgabe 3b

dim  = 300
A    = np.diag(np.diag(np.ones((dim,dim))*4000))+np.ones((dim,dim))
dum1 = np.arange(1,np.int(dim/2+1),dtype=np.float64).reshape((np.int(dim/2),1))
dum2 = np.arange(np.int(dim/2),0,-1,dtype=np.float64).reshape((np.int(dim/2),1))
x    = np.append(dum1,dum2,axis=0)
b    = A@x
x0   = np.zeros((dim,1))
tol  = 1e-4

start = time.time()
x1,n,n2 = IT19tb_WIN7_S10_Aufg3a(A,b,x0,tol,1)
stop = time.time()

t1 = stop-start

start = time.time()
x2,n,n2 = IT19tb_WIN7_S10_Aufg3a(A,b,x0,tol,2)
stop = time.time()

t2 = stop-start

start = time.time()
A_triangle,A_det,x3 = IT19tb_WIN7_S6_Aufg(A,b)
stop = time.time()

t3 = stop-start

print('Zeit Jacobi-Verfahren:', t1)
print('Zeit Gauss-Seidel-Verfahren:', t2)
print('Zeit Gauss-Verfahren Serie 6:', t3)

x1_fehler = np.abs(np.subtract(x3.reshape(dim,1),x1))
x2_fehler = np.abs(np.subtract(x3.reshape(dim,1),x2))

plt.plot(x1_fehler,color='blue',label='Fehler Jacobi-Verfahren')
plt.plot(x2_fehler,color='red',label='Fehler Gauss-Seidel-Verfahren')
plt.xlabel("Elemente des Lösungsvektors")
plt.legend()


'''
Leider konnten wir das Resultat für die 3000x3000 Matrix nicht mit unserer Funktion aus der Serie 6 in einer
angemessenen Zeit berechnen (wir haben ca. 1h gewartet). Daher haben wir nur mit einer 300x300 Matrix gerechnet
und sind zum Schluss gekommen, dass das Gaus-Seidel-Verfahren ca. eine Grössenordnung genauer ist als das Jacobi-Verfahren.
'''