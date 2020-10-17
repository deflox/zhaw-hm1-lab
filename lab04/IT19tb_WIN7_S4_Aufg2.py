import numpy as np
import matplotlib.pyplot as plt

def ausbreitung(k, alpha):
    return alpha * k * (1 - k);

def fixpunktiteration(k, alpha):
    prev = ausbreitung(k, alpha)
    for i in range (1, 10000):
        neu = ausbreitung(prev, alpha)
        if np.abs(neu - prev) < 1e-6:
            return neu;
        prev = neu
    return "Nicht anziehend"
        
        
# Aufgabe 2a
# Fixpunktiterationen mit verschiedenen Werten für alpha
alpha_werte = np.arange(0,4,0.1)
for i in range(0, len(alpha_werte)):
    print("alpha =", alpha_werte[i])
    print(fixpunktiteration(0.1, alpha_werte[i]))

# Aufgabe 2b

# Aufgabe 2c