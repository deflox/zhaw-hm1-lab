import numpy as np
import matplotlib.pyplot as plt

# Aufgabe 1a

# Original Funktion
def f(x):
    return 230.*x**4 + 18.*x**3 + 9.*x**2 - 221.*x - 9

# Funktion für Fixpunktiteration
def F1(x):
    return (230.*x**4 + 18.*x**3 + 9.*x**2 - 9)/221.

# Ableitung der Funktion für Fixpunktiteration
def F1_diff(x):
    return (920./221.)*x**3 + (54./221)*x**2 + (18./221.)*x

def F2_diff(x):
    return 0.5 * ((((920./-9.)*x**3 + (54./-9.)*x**2 + (18./-9.)*x))/(np.sqrt((230.*x**4 + 18.*x**3 - 221.*x - 9.)/-9.)))

x_interval = np.arange(-0.1,0.1,0.01)

plt.plot(x_interval, F1(x_interval))
plt.grid()
plt.show()

def fixpunktiteration(x):
    prev = F1(x)
    iteration = 0
    #print("Iteration_neu:", prev)
    while True:
        iteration += 1
        neu = F1(prev)
        #print("Iteration_neu:", neu)
        if np.abs(neu - prev) < 1e-6:
            #print("Iterations: ", iteration)
            return neu
        prev = neu

# x1:
# Nullstelle 1 liegt etwa bei -0.1
# Steigung ist < 1 somit divergiert die Funktion für -0.1 und der Fixpunkt ist anziehend
print("Punkt in Ableitung eingesetzt: ", F1_diff(-0.1))
print("Resultat der Fixpunktiteration: ", fixpunktiteration(-0.1))

# x2:
# Nullstelle 2 liegt etwa bei 0.9
# Annahme: Es ist möglich den Fixpunkt anzunähern, da die Fixpunktiteration nicht konvergiert.
# Wenn man 0.9 in die Ableitung einsetzt, dann erhält man einen Wert > 1
print("Ableitung für 0.9 in F1:", np.abs(F1_diff(0.9)))
print("Ableitung für 0.9 in F2:", np.abs(F2_diff(0.9)))

# Aufgabe 2b

x_interval = np.arange(-0.5,0.5,0.01)

#plt.plot(x_interval, F1(x_interval))
#plt.grid()
#plt.ylim(-0.5, 0.5)
#plt.show();

# Betrachtet man den Plot der Funktion F(x) dann stellt man fest, dass
# das Interval [-0.5,0.5] auf das gleiche Interval auf der y-Achse.
# Dann geben wir 0.5 in die Ableitungsfunktion rein, damit wir alpha
# ausrechnen können.
# print('Alpha:', F1_diff(0.5))

# Alpha ist somit kleiner als 1 und der Satz ist erfüllt.

# Aufgabe 2c