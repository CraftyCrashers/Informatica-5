# Input
n = int(input('Aantal priemgetallen: '))

# Proces
getal, resultaat = 2, 0
for i in range(n):
    deler = 1
    while getal / deler != getal // deler:
        getal += 1
    resultaat += getal