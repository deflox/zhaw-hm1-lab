import numpy as np
import matplotlib.pyplot as plt

#number of pixels in x and y direction
detail = 1000
#maximum n for iterations
maxit  = 70
#minimim value of x-interval
x_min  = -2
#maximum value of x-interval
x_max  = 0.7
#minimim vale of y-interval
y_min  = -1.4
#minimim vale of y-interval
y_max  = 1.4

#define real axis [x_min,x_max]
a = np.linspace(x_min,x_max,detail,dtype=np.float64)
#define imaginary axis [y_min,y_max]
b = np.linspace(y_min,y_max,detail,dtype=np.float64)

#for color valzues n (creates detailxdetail grid)
B = np.zeros((detail,detail))

#to create the complex plane with the axes defined by a and b
[x,y] = np.meshgrid(a,b)
#creating the plane
C = x+y*1j
#initial conditions (first iteration), Z has same dimension as C
Z = np.zeros((len(C),len(C)), np.complex64)

for n in np.arange(1,maxit+1):
  #calculating new Z
  Z = Z**2+C
  #finding exploded values (i.e. with an absolute value > 2)
  expl = np.where(abs(Z) > 2)
  #removing from iteration
  Z[expl] = 0
  #removing from plane           
  C[expl] = 0
  #saving color value n
  B[expl] = n

plt.figure(1)

#deviding by max value for correct color
B = B/np.max(np.max(B))
#display image
plt.imshow(B,extent=[x_min,x_max,y_min,y_max],origin='lower',interpolation='bilinear')