import numpy as np
import timeit

def fact_rec(n):
    if n < 0 or np.trunc(n) != n:
        raise Exception('The factorial is defined only for positive integers')
    if n <= 1:
        return 1
    else:
        return n*fact_rec(n-1)
    
def fact_for(n):
    if n <= 1:
        return 1
    result = 1
    for i in range (2, n+1):
        result = result * i
    return result

#t1=timeit.repeat("fact_rec(500)", "from __main__ import fact_rec", number=100)
#print(t1)
#t1=timeit.repeat("fact_for(500)", "from __main__ import fact_for", number=100)
#print(t1)

# Die Funktion mit dem for-Loop ist schneller im Rechnen.

print(fact_rec(190))
print(fact_rec(200))
print(fact_rec(170.0))
print(fact_rec(171.0))

# Scheinbar lassen sich beim Datentyp Integer sehr grosse Zahlen speichern, 
# beim Datentyp float ist die Grenze scheinbar bereits bei 171! erreicht.