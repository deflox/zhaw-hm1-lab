import numpy as np

# fehlerentwicklung bei funktionen
# -------------------

def f(x)  : return x**2
def df(x) : return 2*x

korrektes_x = 2
fehlerhaftes_x = 2.5

# absolute fehlerentwicklung
abs_err = np.abs(df(korrektes_x)) * np.abs(fehlerhaftes_x - korrektes_x)
print('Absolute Fehlerentwicklung bei Funktionen:', abs_err)

# relative fehlerentwicklung
rel_err = (np.abs(df(korrektes_x))*np.abs(korrektes_x))/(np.abs(f(korrektes_x))) * (np.abs(fehlerhaftes_x-korrektes_x))/(np.abs(korrektes_x))
print('Relative Fehlerentwicklung bei Funktionen', rel_err)

# fehlerabschätzung bei fixpunktiteration
# -------------------
print()

def F(x):  return (1./(np.cos(x+(np.pi/4.)) - 1)) + 2.
def dF(x): return (np.sin(x+(np.pi/4.)))/((np.cos(x+(np.pi/4.))-1)**2)
lipschitz_const = 0.6640946355544965

# a-priori abschätzung
x0 = 1.3
x1 = 1.35
n = 12
apri = (lipschitz_const)**n/(1-lipschitz_const)-np.abs(x1-x0)
print('Fixpunktiteration: Laut A-Priori Abschätzung ist der Fehler maximal:', apri)

# abschätzung der schritte mit a-priori abschätzung
abs_err = 1e-9
steps = np.log((abs_err*(1-lipschitz_const))/(np.abs(x1-x0)))/np.log(lipschitz_const)
print('Fixpunktiteration: Anzahl geschätzter Schritte laut A-Priori Abschätzung:', np.ceil(steps))

# a-posteriori abschätzung
xn_1 = 1.3441
xn = 1.3376
apost = (lipschitz_const)/(1-lipschitz_const) * np.abs(xn-xn_1)
print('Fixpunktiteration: Laut A-Posteriori Abschätzung ist der Fehler maximal:', apost)

# fehlerabschätzung bei direkten lösungsverfahren von linearen gl systemen
# -------------------
print()

norm = np.inf

A = np.array([
    [2,1,0],
    [4,0,-2],
    [1,2,4],
],dtype=np.float)

b = np.array([
    [1],
    [1],
    [0],
],dtype=np.float)

cond_A = np.linalg.cond(A,norm)

# abschätzung fehler bei gestörtem b
b_ = np.array([
    [1.2],
    [1.2],
    [0],
],dtype=np.float)

err_b_abs = np.linalg.norm(np.linalg.inv(A),norm) * np.linalg.norm(b_-b,norm)
err_b_rel = cond_A * (np.linalg.norm(b_-b,norm))/(np.linalg.norm(b,norm))

print('Direkte Lösungsverfahren: Absoluter Fehler bei gestörtem b:', err_b_abs)
print('Direkte Lösungsverfahren: Relativer Fehler bei gestörtem b:', err_b_rel)

# abschätzung fehler bei gestörtem A und b
A_ = np.array([
    [2.1,1.1,0],
    [4.1,0,-2.1],
    [1.1,2.1,4.1]
],dtype=np.float)

bedingung = cond_A * (np.linalg.norm(A_-A,norm))/(np.linalg.norm(A,norm))
if (bedingung < 1):
    err_b_A_abs = (cond_A)/((1-cond_A)*(np.linalg.norm(A_-A,norm))/(np.linalg.norm(A,norm))) * ((np.linalg.norm(A_-A,norm))/(np.linalg.norm(A,norm))+(np.linalg.norm(b_-b,norm))/(np.linalg.norm(b,norm)))
    print('Direkte Lösungsverfahren: Relativer Fehler bei gestörtem b und A:', err_b_A_abs)
else:
    print('Abschätzung bei gestörtem A und b nicht möglich da Bedingung < 1')

# fehlerabschätzung bei iterativen lösungsverfahren von linearen gl systemen
# -------------------

# a-priori abschätzung

# a-posteriori abschätzung