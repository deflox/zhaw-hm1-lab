import numpy as np

A = np.array([
    [1,-2,3],
    [-5,4,1],
    [2,-1,3]
])

print(A[:,0][1:])

# Aufgabe 1a

# 1. Iteration

r1 = np.array([
    [1.],
    [-5.],
    [2.]
]);
i1 = np.array([
    [1.],
    [0],
    [0]
]);

v1 = r1 + (np.linalg.norm(r1) * i1)
u1 = v1/np.linalg.norm(v1)
H1 = np.eye(3,3) - (2*np.matmul(u1,np.transpose(u1)))
R_neu = np.matmul(H1,A)

# 2. Iteration

r2 = np.array([
    [R_neu[1][1]],
    [R_neu[2][1]]
]);
i2 = np.array([
    [1],
    [0]
])

v2 = r2 + ((-1 * np.linalg.norm(r2)) * i2);
u2 = v2/np.linalg.norm(v2)
H2 = np.eye(2,2) - (2*np.matmul(u2,np.transpose(u2)))

H2_adjusted = np.array([
    [1,0,0],
    [0,H2[0][0],H2[0][1]],
    [0,H2[1][0],H2[1][1]]
])

R_neu_2 = np.matmul(H2_adjusted,R_neu)
Q_neu_2 = np.matmul(np.transpose(H1),np.transpose(H2_adjusted));


# Aufgabe 1b

Q = Q_neu_2
R = R_neu_2

b = np.array([1.,9.,5.])

c = np.matmul(np.transpose(Q),b)

x3 = c[2]/R[2][2]
x2 = (c[1]-R[1][2]*x3)/R[1][1]
x1 = (c[0]-R[0][2]*x3-R[0][1]*x2)/R[0][0]