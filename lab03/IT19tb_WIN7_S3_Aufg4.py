import numpy as np
import matplotlib.pyplot as plt

def h(x):
    return np.sqrt(100.0*x**2-200*x+99)

def h_kondition(x):
    return (np.absolute(0.5*(200.0*x**2-200.0*x+99)**(-0.5)*200.0*x-200.0)*np.absolute(x))/(np.absolute(np.sqrt(200.0*x**2-200.0*x+99)))

# Aufgabe 4a
# Wenn man die Fuktion analytisch betrachtet müsste h(1.1) folgendes Resultat ergeben:
# sqrt(100 * (1.1)**2 - 200 * 1.1 + 99) = sqrt(0) = 0
# Führt man genau diese Rechnung mit Python aus erhält man jedoch folgendes Resultat:
# -1.4210854715202004e-14
# Es gibt bereits einen Fehler bei der Darstellung von 1.1 im IEEE 754
# Das führt dazu, dass das 1.1^2 sowie 1.1 beides nur angenähert werden und
# im IEEE 754 nicht exakt darstellbar sind.
# Die Subtraktion gleicht den Fehler leider nicht aus, da einmal der Wert im Quadrat kommt
# und einmal als einfache Zahl. Ein Rundungsfehler bleibt bestehen und die Funktion um 1.1 
# ergibt einen falschen Wert.

# Aufgabe 4b

x_interval = np.arange(1.1,1.3,10**-7)

plt.plot(x_interval, h_kondition(x_interval), label='h_kondititon(x)')
plt.legend()
plt.grid()
plt.show()

# Aufgabe 4c
# Die Kondition um die Stelle 1.1 ist nicht gut. Sie ist dort maximal hoch und ergibt den Wert 19.
# Die Fehlerentwicklung kann durch Umformung der Funktion nicht vermieden oder vermindert werden.

print('Kondition von h(x) beim Wert 1.1:', h_kondition(1.1))