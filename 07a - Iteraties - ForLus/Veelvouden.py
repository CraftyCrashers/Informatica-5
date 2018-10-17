# Invoer

getal = int(input('Geef een getal kleiner dan 100 en groter dan 0: '))

# Format

uitkomst = 0
for i in range(1, 101):
    if i / getal == i // getal:
        uitkomst += i

# Uitvoer

print(uitkomst)