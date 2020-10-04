import numpy as np
import matplotlib.pyplot as plt

# Aufgabe 2a
# Bei der f2() ist der Plot genauer als bei der f1().
# f1() berrechnet den Wert indem mehrere Werte addiert und subtrahiert werden.
# Die Terme welche subtrahiert werden, sind ähnlich gross wenn der x Wert 
# klein ist, und erzeugen dadurch eine grosse Fehlerfortpflanzung.
# Das Phänomen der Auslöschung tritt auf, und die Resultate von f1() 
# werden sehr ungenau und chaotisch.
# Für f2() wird die Rechnung (x-2)^7 ausgeführt. Dabei wird nur 
# (x-2) mehrmals mit sich selber multipliziert. In diesem Fall ist die Rechnung
# weniger Fehleranfällig, da die Multiplikation wie mehrfaches Addieren ist. 

# Beispiel für f1(x): y = f1(5)
def f1(x):
    return x**7 - 14*x**6 + 84*x**5 - 280*x**4 + 560*x**3 - 672*x**2 + 448*x - 128

# Beispiel für f2(x): y = f2(5)
def f2(x):
    return (x-2)**7

x_interval = np.linspace(1.99, 2.01, 501)

plt.plot(x_interval, f1(x_interval), color = 'blue', label='f1(x)')
plt.plot(x_interval, f2(x_interval), color = 'red', label='f2(x)')

plt.ylim(-5*10**(-15), 5*10**(-15))

plt.legend()
plt.grid()
plt.show()

# Aufgabe 2b
# Die Stabilität beschreibt die Robustheit eines numerischen Verfahrens 
# gegenüber Störungen und Rundungsfehler. Wenn wir den Plot betrachten,
# stellen wir fest, dass als sich der Wert von x 0 nähert, weichen die
# Funktionswerte g(x) immer mehr von einander ab. Sie konvergieren nicht.
# Deshalb ist die Berechnung des limes von g(x) für x->0 auf diese Weise
# nicht stabil.

# Beispiel für g1(x): y = g1(5)
def g1(x):
    return x/(np.sin(1.0+x)-np.sin(1.0))

x_interval = np.arange(-10**-14, 10**-14, 1*10**-17)

plt.plot(x_interval, g1(x_interval), label='g(x)=x/(sin(1+x)-sin(1))')
plt.legend()
plt.grid()
plt.show()

# Aufgabe 2c
# Wir stellen fest, dass diese Funktion nun stabil ist um den Wert x = 0 herum.
# Bei der ersten Variante haben wir eine Subtraktion im Nenner, und der Wert
# als sich der Nenner dem Wert 0 nähert wird die Funktion immer ungenauer.
# Bei der zweiten Variante haben wir nur Multiplikationen im Nenner.
# Es entstehen weniger Störungen. Da die Funktion auf beiden Seiten von 0
# relativ stabil und stetig aussieht, können wir diese Funktion für die
# Approximation vom limes von g(x) für x->0 verwenden.
# Der Wert vom limes von g(x) für x->0 ist ungefähr 1.85

# Beispiel für g2(x): y = g2(5)
def g2(x):
    return x / (2.0 * np.cos( (2.0+x) / 2.0 ) * np.sin( x / 2.0 ))

plt.plot(x_interval, g1(x_interval), label='g(x)=x/(sin(1+x)-sin(1))')
plt.plot(x_interval, g2(x_interval), label='g2(x)=x/(2*cos((2+x)/2)*sin(x/2))')
plt.ylim(1.5, 2)
plt.legend()
plt.grid()
plt.show()
