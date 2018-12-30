# Invoer
h = int(input('Geef een getal: '))

# Format
tienMacht, somDeler = 10, 0
while h > tienMacht / 10:
    somDeler += (h % tienMacht) / (tienMacht / 10) // 1
    tienMacht *= 10

# Uitvoer
if h % somDeler == 0:
    print(str(h) + ' is een Harshadgetal')
else:
    print(str(h) + ' is geen Harshadgetal')
