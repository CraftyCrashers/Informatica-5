# Invoer
n = int(input('Aantal gebouwen?: '))

# Format
zichtbaarGedeelte = 0
for i in range(n):
    naam = input('Naam gebouw?: ')
    hoogte = int(input('Hoogte gebouw in meter?: '))
    if hoogte > zichtbaarGedeelte:
        if zichtbaarGedeelte == 0:
            print('{} is zichtbaar van het gelijkvloers tot {} meter.'.format(naam, hoogte))
        else:
            print('{} is zichtbaar van {} meter tot {} meter.'.format(naam, zichtbaarGedeelte, hoogte))
        zichtbaarGedeelte = hoogte
