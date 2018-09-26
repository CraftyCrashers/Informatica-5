import math

#Invoer van 2 waarden
r = float(input('Afstand sateliet tot middenpunt aarde uitgedrukt in meter'))
v = float(input('Snelheid sateliet ten opzichte van de aarde in meter per seconde'))

#constante
u = 398600.4418 * (10 ** 9)
a = (u * r) / ((2 * u) - (r * v * v))
p = 2 * math.pi * (math.sqrt((a ** 3) / u))
dagen1 = int(p / (24 * 60 * 60))
dagen2 = p % (24 * 60 * 60)
uren1 =  int(dagen2 / (60 * 60))
uren2 = dagen2 % (60 * 60)
minuten = int(uren2 / 60)

#Uitvoer
print('grote as: ' + str(a) + ' meter')
print('periode: ' + str(p) + ' seconden')
print('periode: ' + str(dagen1) + ' dagen, ' + str(uren1) + ' uren en ' + str(minuten) + ' minuten')
