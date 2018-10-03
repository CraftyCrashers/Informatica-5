# Invoer
x = int(input('Wat is de windsnelheid?'))

# Schaal
if x < 119:
    c = 'geen orkaan'
elif x <= 153:
    c = 'categorie 1'
elif x <= 177:
    c = 'categorie 2'
elif x <= 209:
    c = 'categorie 3'
elif x <= 249:
    c = 'categorie 4'
else:
    c = 'categorie 5'

# Uitvoer
print(c)
