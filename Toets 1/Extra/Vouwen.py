papier = int(input('Dikte papier?: '))
afstand = int(input('Afstand aarde-maan in mm: '))
aantal = 0
while papier < afstand:
    papier = papier * 2
    aantal += 1
print('Na {} keer vouwen bedraagt de dikte van het papier {} mm.'.format(aantal, papier))
