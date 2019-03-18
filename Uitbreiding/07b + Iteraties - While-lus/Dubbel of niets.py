# Format
verificatie, inzet = 0, 0
kapitaal = int(input('Huidige bedrag?: '))
while verificatie == 0:
    inzet = input('Hoeveel inzet?: ')
    if inzet == 'stop' and verificatie == 0:
        verificatie = 2
    elif inzet != 'alles' and verificatie == 0:
        inzet = int(inzet)
        if inzet > kapitaal:
            verificatie = 1
    elif verificatie == 0:
        inzet = kapitaal
    if verificatie == 0:
        kapitaal -= int(inzet)
        kleur = input('Zwart of wit?: ')
        showdown = input('Resultaat: ')
        if kleur == showdown:
            kapitaal += inzet * 2

if verificatie == 1 and kapitaal != 0:
    print('Je kunt geen {} dollar inzetten als je maar {} dollar hebt.'.format(str(inzet), str(kapitaal)))
else:
    print('Je eindigt met ' + str(kapitaal) + ' dollar.')
