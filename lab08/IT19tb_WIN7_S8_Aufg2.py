# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 13:26:09 2020

Höhere Mathematik 1, Serie 8, Gerüst für Aufgabe 2

Description: calculates the QR factorization of A so that A = QR
Input Parameters: A: array, n*n matrix
Output Parameters: Q : n*n orthogonal matrix
                   R : n*n upper right triangular matrix            
Remarks: none
Example: A = np.array([[1,2,-1],[4,-2,6],[3,1,0]]) 
        [Q,R]=IT19tb_WIN7_S8_Aufg2(A)

@author: knaa
"""

def IT19tb_WIN7_S8_Aufg2(A):
    
    import numpy as np
    
    A = np.copy(A)                       #necessary to prevent changes in the original matrix A_in
    A = A.astype('float64')              #change to float
    
    n = np.shape(A)[0]
    
    if n != np.shape(A)[1]:
        raise Exception('Matrix is not square') 
    
    Q = np.eye(n)
    R = A
    
    for j in np.arange(0,n-1):
        a = np.copy(R[:,j][j:]).reshape(n-j,1) # spaltenvektor des neuen R's
        e = np.eye(n-j)[:,0].reshape(n-j,1) # spalte der einheitsmatrix
        length_a = np.linalg.norm(a) # länge des spalten vektors
        if a[0] >= 0: sig = 1
        else: sig = -1
        v = a + (sig * length_a * e)
        u = v/np.linalg.norm(v)
        H = np.eye(n-j) - (2 * np.matmul(u,np.transpose(u)))
        Qi = np.eye(n)
        Qi[j:,j:] = H
        R = np.matmul(Qi,R)
        Q = np.matmul(Q,np.transpose(Qi))
        
    return(Q,R)