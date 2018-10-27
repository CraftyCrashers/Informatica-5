from random import randint, seed
seed(1)

# Geen Input

juistgetal = int(randint(1, 100))
getal, aantal, laagstegetal, hoogstegetal = 0, 0, 1, 100
while getal != juistgetal:
    getal = int(randint(laagstegetal, hoogstegetal))
    aantal += 1
    print('[{},{}] --> computer gokt {}'.format(laagstegetal, hoogstegetal, getal))
    if getal < juistgetal:
        laagstegetal = getal + 1
    else:
        hoogstegetal = getal - 1

# Uitvoer
print('computer had {} pogingen nodig om het getal {} te raden.'.format(aantal, juistgetal))
