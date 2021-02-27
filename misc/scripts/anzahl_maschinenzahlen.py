stellen_mantisse = 15
stellen_exponent = 5
system = 2

print('Bei der Mantisse ist das Vorzeichen inkludiert, daher gibt es')
print(''+str(system)+' * '+str(system)+'^' + str(stellen_mantisse-1) + ' Möglichkeiten')

print('')

print('Beim Exponent ist das Vorzeichen nicht inkludiert, daher gibt es')
print('('+str(system)+' * '+str(system)+'^' + str(stellen_exponent) + ' - 1) Möglichkeiten. (-1 Abzug da Null doppelt gezählt)')

print('')

print('Und es muss noch 1 dazugezählt werden, weil die Zahl 0 seperat abgespeichert wird.')

print('')

tot = system * system**(stellen_mantisse-1) * (system * system**stellen_exponent - 1) + 1
print('Total Möglichkeiten: '+str(system)+' * '+str(system)+'^' + str(stellen_mantisse-1) + ' * ('+str(system)+' * '+str(system)+'^' + str(stellen_exponent) + ' - 1) + 1 =', tot)