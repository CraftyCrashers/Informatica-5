# Input
thuis = int(input('Punten thuisploeg: '))
uit = int(input('Punten uitploeg'))

# Format
puntenverschil = abs(thuis - uit)
winnaar = thuis - uit
if puntenverschil < 10:
    punten = 600
elif puntenverschil < 20:
    punten = 700
else:
    punten = 800

# Uitvoer
if winnaar > 0:
    print('thuisploeg: {:.2f}'.format(punten - 70))
    print('  uitploeg: {:.2f}'.format(1070 - punten))
else:
    print('thuisploeg: {:.2f}'.format(930 - punten))
    print('  uitploeg: {:.2f}'.format(punten + 70))