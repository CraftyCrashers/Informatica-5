# Input
n = int(input('Aantal priemgetallen: ')) - 1

# Proces
huidigAantalPriemgetal, huidigPriemgetal, huidigDeler, somPriemgetallen, x = 0, 3, 2, 2, 0
while huidigAantalPriemgetal < n:
    while huidigDeler <= huidigPriemgetal:
        if huidigPriemgetal / huidigDeler == huidigPriemgetal // huidigDeler and huidigPriemgetal != huidigDeler:
            huidigDeler += huidigPriemgetal
        elif huidigDeler >= huidigPriemgetal // 2:
            huidigAantalPriemgetal += 1
            somPriemgetallen += huidigPriemgetal
            huidigDeler += huidigPriemgetal
        else:
            huidigDeler += 1
    huidigPriemgetal += 2
    huidigDeler = 2

# Output
print(somPriemgetallen)
