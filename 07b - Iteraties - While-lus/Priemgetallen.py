# Input

getal = int(input('Geef een getal.: '))

# Format

deler = 2
while getal / deler != getal // deler and getal != 0 and getal != 1:
    deler += 1

# Uitvoer

if getal == deler:
    print(str(getal) + ' is een priemgetal')
else:
    print(str(getal) + ' is geen priemgetal')

# Beter oplossing
# while getal % deler != 0:
#   i +=
