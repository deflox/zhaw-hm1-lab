import numpy as np

def f(phi):
    return 0.5*np.pi+np.sin(phi)



def fixpunktiteration(phi):
    prev = f(phi)
    print("x_1", prev)
    for i in range (1, 10000):
        neu = f(prev)
        print("x_", i+1, neu)
        if np.abs(neu - prev) < 1e-3:
            return neu
        prev = neu
    return "Nicht anziehend"

def bogenmass(x):
    return x*360./(2*np.pi)

wert = fixpunktiteration(3.*(np.pi/4.))
print("Fixpunktiteration mit Startwert 3.*(np.pi/4.)", wert)
print("In Bogenmass:", bogenmass(wert))