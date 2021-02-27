import numpy as np

def subtract(M, b, i, c, j):
    # subtrahiere in der matrix m von der zeile i
    # das c-fache der zeile j
    M[i,:] = M[i,:] - c * M[j,:]
    b[i,0] = b[i,0] - c * b[j,0]
    
def swap(M, b, i, j):
    # vertauscht in der matrix m und b die zeilen 
    # i und j
    if (i != j):
        print('Vertausche', i+1, 'Zeile mit', j+1, 'Zeile')
    
    temp = np.copy(M[i,:])
    M[i,:] = M[j,:]
    M[j,:] = temp
    temp = np.copy(b[i,:])
    b[i,:] = b[j,:]
    b[j,:] = temp

def gauss(A,b):
    
    # wandelt eine reguläre n x n matrix A und resultatsvektor
    # b mit dem gauss algorithmus unter verwendung von spalten-
    # pivotisierung in eine rechtsobere dreiecksmatrix r um
    R = np.copy(A)
    b = np.copy(b)
    n = np.shape(R)[0]
    
    # iteriere über erste bis vorletzt spalte j
    for j in range(0, n-1):
        print(str(j+1) + '. Iterationsschritt:')  
        
        # bestimme in spalte j ab zeile j diejenige Zeile i
        # mit betragsmässig grösstem Element
        #i = j + np.argmax(np.abs(R[j:n, j]))
        # vertausche zeile i mit zeile j
        #swap(R, b, i, j)
                
        # mache in spalte j ab zeile j+1 alle elemente zu 0
        for i in range(j+1, n):
            print(i+1,'Zeile -', R[i,j]/R[j,j], '*', j+1, 'Zeile')
            subtract(R, b, i, R[i,j]/R[j,j], j)
       
        print('R: \n', R)
        print('b: \n', b)
        print()
            
    return R,b


A = np.array([
    [13-1,-4],
    [30,-9-1],
], dtype=np.float)

b = np.array([
    [0],
    [0],
], dtype=np.float)

'''
A = np.array([
    [2-1j,5],
    [-1,-2-1j],
], dtype=np.complex)

b = np.array([
    [0],
    [0],
], dtype=np.complex)
'''

R_result,b_result = gauss(A,b)

print()
print('Result:')
print('R: \n', R_result)
print('b: \n', b_result)