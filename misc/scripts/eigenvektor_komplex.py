import numpy as np

M = np.array([
    [5.72458409e-01,-3.08294427e+00],
    [1.86680320e+00,4.27541591e-01],
],dtype=np.complex)

print('('+str(M[0][0])+'-lamda)*('+str(M[1][1])+'-lamda)-('+str(M[0][1])+'*'+str(M[1][0])+')')

a = 1.
b = (-1.*M[0][0])+(-1.*M[1][1])
c = (M[0][0]*M[1][1])-(M[0][1]*M[1][0])

x1 = (-b+(np.sqrt(b**2-(4*a*c))))/(2.*a)
x2 = (-b-(np.sqrt(b**2-(4*a*c))))/(2.*a)

print('x1:',x1)
print('x2:',x2)