# Format

nummer = 1
totaal = 0
while nummer != 0 and totaal < 21:
    nummer = int(input('Waarde kaart?: '))
    totaal += nummer

# Resultaat

if totaal == 21:
    print('Gewonnen!')
elif totaal > 21:
    print('Verbrand ({})'.format(totaal))
else:
    print('Voorzichtig gespeeld ({})'.format(totaal))
