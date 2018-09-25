b = float(input('Wat is het breedte van het graanveld?'))
l = float(input('Wat is het lengte van het graanveld?'))
c = float(input('Hoeveel graan in kubieke meter per hectare?'))
r = float(input('Wat is de straal van de graansilo?'))
h = float(input('Wat is de hoogte van de graansilo?'))

hectare = (b * l) * (10 ** -4)
aantalGraan = c
aantalGraan *= hectare
capaciteitSilo = 3.1415926535897931
capaciteitSilo *= r
capaciteitSilo *= r
capaciteitSilo *= h
voldoendeSilo = int(aantalGraan / capaciteitSilo)
overigGraan = (aantalGraan % capaciteitSilo)
overigGraan /= capaciteitSilo
overigGraan *= h

print(voldoendeSilo)
print(overigGraan)
print(aantalGraan)
print(capaciteitSilo)