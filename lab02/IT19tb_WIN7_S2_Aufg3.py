import numpy as np
import matplotlib.pyplot as plt

# Aufgabe 3a
# Für grössere Werte wird pi genauer jedoch wird es danach wieder ungenauer.

def s1(x):
    if x < 6:
        return 1
    return np.sqrt(2.0-2.0*np.sqrt(1.0-((s1(x/2)**2)/4.0)))

x_s1_values = np.zeros(22)
y_s1_values = np.zeros(22)

value = 12.0
for i in range (0, 22):
    x_s1_values[i] = value
    y_s1_values[i] = value * s1(value)
    value = 2 * value
    
plt.plot(x_s1_values, y_s1_values, color='red')

# Aufgabe 3b
def s2(x):
    if x < 6:
        return 1
    return np.sqrt( s1(x/2)**2.0 / (2 * (1 + np.sqrt(1 - ( (s1(x/2)**2)/4.0 )) ) ) )

x_s2_values = np.zeros(22)
y_s2_values = np.zeros(22)

value = 12.0
for i in range (0, 22):
    x_s2_values[i] = value
    y_s2_values[i] = value * s2(value)
    value = 2 * value

plt.plot(x_s2_values, y_s2_values, color='blue')

plt.show()