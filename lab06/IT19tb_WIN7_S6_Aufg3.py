import numpy as np
from IT19tb_WIN7_S6_Aufg2 import IT19tb_WIN7_S6_Aufg

A = np.array(
[
  [200.,150.,100.], 
  [50.,30.,20.],
  [20.,10.,0],
]    
)

# Gleichungssystem 1
b1 = np.array([2150.,470.,150.])

print(IT19tb_WIN7_S6_Aufg(A,b1))
print(np.linalg.solve(A,b1))

# Gleichungssystem 2
b2 = np.array([1600.,350.,120.])

print(IT19tb_WIN7_S6_Aufg(A,b2))
print(np.linalg.solve(A,b2))

'''
Wir haben dasselbe Ergebnis erhalten wie numpy.linalg.solve.
'''