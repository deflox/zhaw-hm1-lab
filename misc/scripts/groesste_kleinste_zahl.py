
base = 2
groesse_mantisse = 5
groesse_exponent = 3

m = '0.'
for i in range(0,groesse_mantisse):
    m += str(base-1)

exp = ''
for i in range(0,groesse_exponent):
    exp += str(base-1)

print('Grösste Zahl: ' + m + ' * ' + str(base) + '^' + exp)
print('Kleinste Zahl: 0.1 * 2^-' + exp)