import numpy as np
import matplotlib.pyplot as plt

def ausbreitung(k, alpha):
    return alpha * k * (1 - k)

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
    
# Ab Alphawerten >= 3 divergiert der Fixpunkt bzw. der Fixpunkt ist abstossend.

# Aufgabe 2b
# Der Fixpunkt ist das stabile Verhältnis zwischen gesunden und kranken 
# Kindern bei einer gegeben Ansteckungsrate alpha. Falls alpha dabei zu gross
# ist, heisst das auch, dass der Fixpunkt abstossen ist, was heisst, es gibt kein
# solches stabiles Verhältnis.

# Aufgabe 2c
def fixpunkt_fuer_alpha(alpha):
    return -(1./alpha) + 1

# Unsere Formel funktioniert nur mit Alpha-Werten > 1, wir sind uns aber nicht sicher
# ob dies auch so gewollt ist, da in der Aufgabenstellung gesagt wird, dass die
# Alphawerte > 1 sein sollen.
print(fixpunkt_fuer_alpha(1.0))