# Input
n = int(input('Aantal priemgetallen: '))

# Proces
huidigAantalPriemgetal, huidigPriemgetal, huidigDeler, somPriemgetallen, x = 0, 2, 2, 0, 0
while huidigAantalPriemgetal < n:
    for i in range(1, huidigPriemgetal // 2):
        if huidigPriemgetal / i == huidigPriemgetal // i and x == 0:
            x = 1
    if x == 0:
        somPriemgetallen += huidigPriemgetal
        huidigAantalPriemgetal += 1
    else:
        x = 0
    huidigPriemgetal += 1

# Output
print(somPriemgetallen)
