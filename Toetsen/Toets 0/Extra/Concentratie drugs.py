from math import pow, pi
# Invoer
t = float(input('Aantal uren: '))

# Uitvoer
print(round((pi * t) / (pow(t, 2) + 2), 4))