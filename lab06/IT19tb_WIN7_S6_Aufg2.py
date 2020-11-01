import numpy as np

def IT19tb_WIN7_S6_Aufg(A_in,b_in):
    if (len(A_in) != len(A_in[0])):
        print("Function does only support regular matrices.")
        return
    
    A = np.zeros((len(A_in),len(A_in)))
    for i in range(0, len(A_in)):
        for y in range(0, len(A_in)):
            A[i][y] = A_in[i][y]
            
    b = np.zeros(len(b_in))
    for i in range(0, len(b_in)):
        b[i] = b_in[i]
    
    lineChangements = 0
    
    # calculate the A triangle
    column = 0
    for i in range(1, len(A)):
        if (A[i-1][column] == 0):
            lineChangements += 1
            (A,b) = rearangeForNull(A,b, i-1, column)
        
        for y in range(i, len(A)):
            coefficient = A[y][column]/A[i-1][column]
            for z in range(column, len(A[y])):
                A[y][z] = A[y][z] - coefficient * A[i-1][z]
            b[y] = b[y] - coefficient * b[i-1]
        
        column += 1
        
    # calculate the values
    x_values = np.zeros(len(A))
    column = len(A)-1
    for i in range(len(A)-1, -1, -1):
        sumup = b[i]
        for y in range(len(A)-1, column, -1):
            sumup -= A[i][y] * x_values[y]
        x_values[i] = sumup / A[i][column]
        column -= 1
        
    # calculate the determinant
    det = A[0][0]
    for i in range(1, len(A)):
        det *= A[i][i]
    
    det *= (-1)**lineChangements
    
    return A, det, x_values

def rearangeForNull(A,b,row,column):
    goodRow = 0
    for i in range(row+1, len(A)):
        if (A[i][column] != 0):
            goodRow = i
            return switchRows(A,b, row, goodRow)
    
def switchRows(A,b, oldRow, newRow):
    A_new = np.zeros((len(A), len(A[0])))
    b_new = np.zeros(len(b))
    
    for i in range(0, len(A)):
        if (i == oldRow):
            A_new[i] = A[newRow]
            b_new[i] = b[newRow]
        elif (i == newRow):
            A_new[i] = A[oldRow]
            b_new[i] = b[oldRow]
        else:
            A_new[i] = A[i]
            b_new[i] = b[i]
            
    return (A_new, b_new)