# Aufgabe 4 Teil 1
# Wir berechnen den kleinstmöglichen Wert von eps je nach der Basis 2 und 10.
# Wir dividieren den Wert immer jeweils um die entsprechende Basis und prüfen
# ob noch die Summe (1 + eps) noch verschieden von 1 ist.
# Die Variante mit dem kleinsten eps am Schluss ist diejenige Variante
# mit dem unser Rechner ebenfalls rechnet. Die andere Variante wird schneller
# ungenau, weil die Basis noch umgerechnet werden muss.
# Weiterhin schliessen wir auf ein Dualsystem, da der berechnete eps Wert mit 
# der angenommene Basis 2 der gleiche Wert wie dem der IEEE double Precision
# Gleitkommazahl entspricht. Diese ist in der Basis 2. 

print('Aufgabe 4 Teil 1:')
eps_bin = 1.0
stellen_bin = 0
while ((1+eps_bin) != 1):
    eps_bin = eps_bin/2
    stellen_bin += 1

eps_bin *= 2
stellen_bin -= 1
    
print('eps_bin =',eps_bin)
print('1 + eps_bin =', 1+eps_bin)
print('stellen_bin =',stellen_bin)

eps_dez = 1.0
stellen_dez = 0
while((1+eps_dez) != 1):
    eps_dez = eps_dez/10
    stellen_dez += 1
    
eps_dez *= 10
stellen_dez -= 1    
    
print('eps_dez =',eps_dez)
print('1 + eps_dez =', 1+eps_dez)
print('stellen_dez =',stellen_dez)

if (eps_dez < eps_bin):
    print('Rechner rechnet mit Basis 10 genauer, es ist ein Dezimalsystem')

if (eps_bin < eps_dez):
    print('Rechner rechnet mit Basis 2 genauer, es ist ein Dualsystem')

if (eps_bin == eps_dez):
    print('Rechner rechnet sowohl mit Basis 2 als auch mit Basis 10 genau gleich präszise.')
    print('Wir können anhand vom eps nicht bestimmen auf welche Basis gerechnet wird.')


# Aufgabe 4 Teil 2

print('Aufgabe 4 Teil 2:')
maxx = 1.0
while ((1.0+maxx)!=maxx):
    maxx=maxx*2
    
print(maxx)