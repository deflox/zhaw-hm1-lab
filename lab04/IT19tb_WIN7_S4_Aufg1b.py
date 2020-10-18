import numpy as np
import matplotlib.pyplot as plt

# Funktion für Fixpunktiteration
def F1(x):
    return (230.*x**4 + 18.*x**3 + 9.*x**2 - 9)/221.

# Ableitung der Funktion für Fixpunktiteration
def F1_diff(x):
    return (920./221.)*x**3 + (54./221)*x**2 + (18./221.)*x

# Aufgabe 2b

x_interval = np.arange(-0.5,0.5,0.01)

plt.plot(x_interval, F1(x_interval))
plt.ylim(-0.5, 0.5)
plt.grid()
plt.show();

# Betrachtet man den Plot der Funktion F(x) dann stellt man fest, dass
# das Interval [-0.5,0.5] auf das gleiche Interval auf der y-Achse abgebildet ist.
# Dann geben wir 0.5 in die Ableitungsfunktion rein, damit wir alpha
# ausrechnen können.
print('Alpha:', np.abs(F1_diff(0.5)))

# Alpha ist somit kleiner als 1 und der Satz ist erfüllt.

# Aufgabe 2c