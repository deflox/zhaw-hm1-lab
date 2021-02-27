import sys
import numpy as np
import scipy.linalg

# from IT19tb_WIN7_S10_Aufg3 import IT19tb_WIN7_S10_Aufg3a

M = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
],dtype=np.float)

v = np.array([1,2,3],dtype=np.float)

# matrix operationen
# ----------------------

# elemente einer matrix selektieren
print('\nM[0,1]: \n', M[0,1])

# in jeder zeile das 0lte element selektieren (eine ganze spalte)
print('\nM[:,1]: \n', M[:,0])

# in jeder spalte das 0te element selektieren (eine ganze zeile)
print('\nM[1,:]: \n', M[0,:])

# diagonale einer nxn matrix
print('\nnp.diag(M,0): \n', np.diag(M,0))

# rechtsoberes dreieck einer nxn matrix
print('\nnp.triu(M,1): \n', np.triu(M,1))

# linksunteres dreieck einer nxn matrix
print('\nnp.tril(M,-1): \n', np.tril(M,-1))

# erstelle diagonalmatrix aus diagonaler einer bestehenden matrix
print('\nnp.diagflat(np.diag(M,0)): \n', np.diagflat(np.diag(M,0)))

# suche indexe im matrix welche der bedingung entsprechen
arr = np.array([12,32,12,43,14,2])
print('\nnp.where(arr > 4): \n', np.where(arr > 30))
print('\nnp.where(M > 5): \n', np.where(M > 5))

# ---------------------


# lineare algebra
# ---------------------

# inverse einer matrix berechnen
print('\nnp.linalg.inv(M): \n', np.linalg.inv(M))

# determinante einer matrix berechnen
print('\nnp.linalg.det(M): \n', np.linalg.det(M))

# eigenwerte berechnen
print('\nnp.linalg.eig(M): \n', np.linalg.eig(M))

# matrix transponieren
print('\nnp.transpose(M): \n', np.transpose(M))

# matrix-norm berechnen
print('\nnp.linalg.norm(M,1): \n', np.linalg.norm(M,1))
print('\nnp.linalg.norm(M,2): \n', np.linalg.norm(M,2))
print('\nnp.linalg.norm(M,np.inf): \n', np.linalg.norm(M,np.inf))

# vektor-norm berechnen
print('\nnp.linalg.norm(v,1): \n', np.linalg.norm(v,1))
print('\nnp.linalg.norm(v,2): \n', np.linalg.norm(v,2))
print('\nnp.linalg.norm(v,np.inf): \n', np.linalg.norm(v,np.inf))

# ---------------------


# verfahren
# ---------------------

# gauss-verfahren
print('\nnp.linalg.solve(M,v): \n', np.linalg.solve(M,v))

# qr-verfahren
print('\nnp.linalg.qr(M): \n', np.linalg.qr(M))

# lr-verfahren
print('\nscipy.linalg.lu(M) \n', scipy.linalg.lu(M))

# konditionszahl einer matrix
print('\nnp.linalg.cond(M): \n', np.linalg.cond(M))

# ---------------------


# polynomfunktionen
# ---------------------
# np.polyval
# np.polyfit

# reiner zahlenstuff
# ---------------------

# integer zahlen zu binär umrechnen
decimal = 10
binary = bin(decimal)

# binär zahlen zu integer zahlen umrechnen
binary = '0b1'
decimal = int(binary, 2)
print('Decimal:', decimal)

# grösst und kleinstmögliche nummern
biggest = sys.float_info.max
lowest = sys.float_info.min

x = 5.5

# nächsttiefere wert berechnen
print('\nnp.floor(x): \n', np.floor(x))

# nächsthöherer wert berechnen
print('\nnp.ceil(x): \n', np.ceil(x))