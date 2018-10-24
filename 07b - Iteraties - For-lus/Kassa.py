# Format

prijs = float(input('Prijs?: '))
totaal = 0
while prijs != 0:
    totaal += prijs
    prijs = float(input('Prijs?: '))

print('De totale prijs is € {:.2f}'.format(totaal))