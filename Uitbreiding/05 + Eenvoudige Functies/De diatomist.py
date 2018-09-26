#Invoer 2 stralen
r = float(input('Geef de straal van de kleine cirkel'))
R = float(input('Geef de straal van de grote cirkel'))

#Formule voor maximaal aantal kleine cirkels
n = int(0.83*((R * R) / (r * r)) - 1.9)

#Bedekkingsgraad
bedekkingsgraad = ((r * r * n) / (R * R) * 100)

#Uitvoer
print('{:.0f} kleine cirkels bedekken {:.2f}% van de grote cirkel'.format(n, bedekkingsgraad))
