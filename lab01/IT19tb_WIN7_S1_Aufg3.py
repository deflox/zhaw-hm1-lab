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

print('Die Funktion mit dem for-Loop ist schneller im Rechnen.')
print('Folgende Resultate kamen dabei raus: \n')

t1=timeit.repeat("fact_rec(500)", "from __main__ import fact_rec", number=100)
print('Die Zeiten für fact_rec(500) =', t1)
t2=timeit.repeat("fact_for(500)", "from __main__ import fact_for", number=100)
print('Die Zeiten für fact_for(500) =', t2, '\n')

#fact_rec(): [0.07653639999989537, 0.07627839999986463, 0.07724790000065695, 0.076621599997452, 0.07811709999805316]
#fact_for(): [0.006746099999872968, 0.006646099998761201, 0.006512300002214033, 0.0065288000005239155, 0.006515900000522379]
print('Dabei wurde 5 Mal die Funktion jeweils 100 Mal mit dem Parameterwert 500 aufgerufen und die beste Laufzeit berechnet.') 
print('Dabei ist die rekursive fact_rec() in jedem Fall langsamer als die For-Loop fact_for() Methode. \n')

print('Die zweite Frage bezüglich die maximale speicherbare Werte je nach Datentyp beantworten wir mittels folgende Aufrufe:')
print('fact_rec(190) =', fact_rec(190))
print('fact_rec(200) =', fact_rec(200))
print('fact_rec(170.0) =', fact_rec(170.0))
print('fact_rec(171.0) =', fact_rec(171.0))

print('Scheinbar lassen sich beim Datentyp Integer sehr grosse Zahlen speichern. Laut Onlinedokumentation gibt es für Integer keine obere Grenze.')
print('Beim Datentyp float ist die Grenze scheinbar bereits bei 170! erreicht.')
print('Das Resultat von 171! kann nicht mehr in einem float gespeichert werden.')