# Invoer
doel = int(input('Gewenste snelheid: '))
huidig = int(input('Huidige snelheid'))

# Proces
aantal = 0
while huidig >= doel:
    huidig = huidig - huidig * 0.3
    aantal += 1

# Uitvoer
print('na {} rembewegingen is de snelheid {:.2f}'.format(aantal, huidig))
