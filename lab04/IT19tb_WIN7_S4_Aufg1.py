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

x_interval = np.arange(-1.5,1.5,0.01)

plt.plot(x_interval, f(x_interval))
plt.grid()
plt.show()

def fixpunktiteration(x):
    prev = F1(x)
    while True:
        neu = F1(prev)
        if np.abs(neu - prev) < 1e-6:
            return neu
        prev = neu

# x1:
# Nullstelle 1 liegt etwa bei -0.1
# Steigung ist < 1 somit divergiert die Funktion für -0.1 und der Fixpunkt ist anziehend
print("Punkt in Ableitung eingesetzt: ", F1_diff(-0.1))
print("Resultat der Fixpunktiteration: ", fixpunktiteration(-0.1))

# x2:
# Nullstelle 2 liegt etwa bei 0.9
# Annahme: Es ist möglich den Fixpunkt anzunähern, da keine Funktion divergiert.
# Banachscher Fixpunktsatz ist nicht erfüllt:

# Aufgabe 2b

x_interval = np.arange(-0.5,0.5,0.01)

plt.plot(x_interval, F1(x_interval))
plt.grid()
plt.ylim(-0.5, 0.5)
plt.show();

# Betrachtet man den Plot der Funktion F(x) dann stellt man fest, dass
# das Interval [-0.5,0.5] auf das gleiche Interval auf der y-Achse.
# Dann geben wir 0.5 in die Ableitungsfunktion rein, damit wir alpha
# ausrechnen können.
print('Alpha:', F1_diff(0.5))

# Alpha ist somit kleiner als 1 und der Satz ist erfüllt.

# Aufgabe 2c