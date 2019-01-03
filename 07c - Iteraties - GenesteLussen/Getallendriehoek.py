# Input
getal = int(input('Kies een getal tussen 1 en 9: '))

# Format
x, z, tien = getal, getal, 10
while x >= 1 and z <= 9:
    print('{:^9d}'.format(getal))
    getal, tien, x, z = (x - 1) * tien ** 2 + getal * 10 + (z + 1), tien * 10, x - 1, z + 1
