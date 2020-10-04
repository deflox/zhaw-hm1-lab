import numpy as np
import matplotlib.pyplot as plt

# Aufgabe 3a
# Für grössere Werte wird 2*pi genauer jedoch wird es danach wieder ungenauer.
# Ab 10^7 werden die Werte wieder ungenauer. Je mehr Eckpunkte auf dem Kreis
# zur Annäherung erwendet werden, desto kleiner ist der Beitrag zum Umfang
# je Dreieck. Wenn zu viele Eckpunkte betrachtet werden, wird die 
# Seitenlänge der Dreiecke zu klein und zu ungenau, die resultierende
# Summe wird ebenfalls ungenau.

# Beispiel für s1(x): y = s1(12)
def s1(x):
    if x <= 6:
        return 1
    return np.sqrt(2.0-2.0*np.sqrt(1.0-((s1(x/2)**2)/4.0)))

# Wir können vals ändern um kleinere oder grössere Wertebereiche zu prüfen
vals = 25
x_s1_values = np.zeros(vals)
y_s1_values = np.zeros(vals)

value = 6.0
for i in range (0, vals):
    x_s1_values[i] = value
    y_s1_values[i] = value * s1(value)
    value = 2 * value
    
plt.plot(x_s1_values, y_s1_values, color='red', label='Variante 3a)')

# Aufgabe 3b
# Bei der zweiten Variante beobachten wir, dass für grosse x-Werte die
# resultierende Summe länger genau bleibt, bzw. weniger schnell vom erwarteten
# Wert abweicht.
# Wir vermuten, dass weil s_n^2 sowohl im Zähler als auch im Nenner auftaucht,
# es zu einer kleinen Fehlerbereinigung kommt, und die Werte etwas länger
# genau bleiben, und weniger stark abweichen als die Variante 3a).

# Beispiel für s2(x): y = s2(12)
def s2(x):
    if x <= 6:
        return 1
    return np.sqrt( s1(x/2)**2.0 / (2 * (1 + np.sqrt(1 - ( (s1(x/2)**2)/4.0 )) ) ) )

x_s2_values = np.zeros(vals)
y_s2_values = np.zeros(vals)

value = 6.0
for i in range (0, vals):
    x_s2_values[i] = value
    y_s2_values[i] = value * s2(value)
    value = 2 * value

plt.plot(x_s2_values, y_s2_values, color='blue', label='Variante 3b)')
plt.grid()
plt.legend()
plt.show()