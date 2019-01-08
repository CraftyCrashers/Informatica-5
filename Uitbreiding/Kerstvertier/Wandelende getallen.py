from math import sin, cos, radians
# Invoer
invoer = input('Geef een getal: ')

# Format
puntcheck, beginsituatie, x, y = 0, invoer, 0, 0
if '.' in invoer:
    while '.' in invoer:
        if invoer[puntcheck] == '.':
            invoer = invoer[:puntcheck] + invoer[puntcheck + 1:]
        puntcheck += 1
for i in invoer:
    i = radians(int(i) * 36)
    x, y = x + sin(i), y + cos(i)

# Uitvoer
print('Getal {} wandelt naar positie ({:.2f}, {:.2f}).'.format(beginsituatie, x, y))
