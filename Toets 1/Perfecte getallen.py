# Invoer
getal = int(input('Geef een getal: '))

# Proces
v, a = 0, ''
for i in range(1, (getal // 2) + 1):
    if getal / i == getal // i:
        v += i
        a += str(i) + ' '

# Uitvoer
if getal == v:
    print('{} is een perfect getal en de delers zijn {}'.format(getal, a))
else:
    print('{} is geen perfect getal'.format(getal))