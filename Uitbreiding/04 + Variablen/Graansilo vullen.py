b = float(input('Wat is het breedte van het graanveld?'))
l = float(input('Wat is het lengte van het graanveld?'))
c = float(input('Hoeveel graan in kubieke meter per hectare?'))
r = float(input('Wat is de straal van de graansilo?'))
h = float(input('Wat is de hoogte van de graansilo?'))

aantalGraan = c * b * l
capaciteitSilo = r * r * 3.1415926535897931 * 10000
voldoendeSilo = int((aantalGraan / (capaciteitSilo * h)) + 0.999999999)
overigGraan = (aantalGraan / capaciteitSilo) % h

print(voldoendeSilo)
print(overigGraan)
