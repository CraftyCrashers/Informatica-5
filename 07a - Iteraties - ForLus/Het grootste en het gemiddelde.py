# Invoer

aantal = int(input('Hoeveel getallen? : '))

# Format en 2de invoer

maximum, totaal = 0, 0
for i in range(aantal):
    getal = int(input('Geef het huidige getal. : '))
    if getal > maximum or maximum == 0:
        maximum = getal

    totaal += getal

gemiddelde = round(totaal / aantal, 2)

# Uitvoer

print('Het grootste getal is {} en het gemiddelde is {}'.format(maximum, gemiddelde))
