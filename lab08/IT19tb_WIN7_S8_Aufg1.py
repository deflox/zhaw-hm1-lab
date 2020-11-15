import numpy as np

A = np.array([
    [1,-2,3],
    [-5,4,1],
    [2,-1,3]
])

b = np.transpose(np.array([1,9,5]))

def getv1(a, a11):
    return np.transpose(a) + (signum(a11) * np.linalg.norm(a) * np.transpose(np.array([1,0,0])))

def getu1(v1):
    return v1/np.linalg.norm(v1)

def signum (n) :
    if n >= 0: return 1
    else: return -1

'''
u1 = np.array([
    [(1 + np.sqrt(30)) / np.sqrt(2*np.sqrt(30) + 60)],
    [-5 / np.sqrt(2*np.sqrt(30) + 60)],
    [2 / np.sqrt(2*np.sqrt(30) + 60)]
])
'''

u1 = (getu1(getv1(np.transpose(np.array([1,-5,2])), 1)))

u1T = np.transpose(u1)

#print (np.matmul(u1, u1T))

#print (2*np.matmul(u1, u1T))

Q1 = np.eye(3,3) - 2*np.matmul(u1, u1T)

#print (Q1)

print (A)

print (Q1)

print (np.matmul(A, Q1))