import numpy as np

A_old = np.array([
    [20000.,30000.,10000.],
    [10000.,17000.,6000.],
    [2000.,3000.,2000.],
]);

b_old = np.array([
    [5720000.],
    [3300000.],
    [836000.],
])

x_old = np.linalg.solve(A_old,b_old)
print("x_old:", x_old)


A = np.array([
    [19900.,29900.,9900.],
    [9900.,16900.,5900.],
    [1900.,2900.,1900.],
]);

b = np.array([
    [5820000.],
    [3400000.],
    [936000.],
])

x = np.linalg.solve(A,b)
print("x:", x)

print("x_1 Fehler", (x_old[0]-x[0])/x_old[0])
print("x_2 Fehler", (x_old[1]-x[1])/x_old[1])
print("x_3 Fehler", (x_old[2]-x[2])/x_old[2])