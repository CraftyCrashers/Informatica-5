from math import sqrt as vierkantswortel

#Invoer lengte en breedte
l = float(input('Geef de lengte van het driehoek'))
b = float(input('Geef de breedte van het driehoek'))

#Uitkomst schuine zijde
s = vierkantswortel(l ** 2 + b ** 2)

#Uitvoer
print('In een rechthoekige driehoek met rechthoekszijden a = {:.2f} en b = {:.2f} is de schuine zijde {:.2f}'.format(l, b, s))
