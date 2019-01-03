# Format
verificatie = 0
kapitaal = int(input('Huidige bedrag?: '))
while kapitaal != 'stop':
    inzet = input('Hoeveel inzet?: ')
    if inzet != 'stop':
        verificatie = 2
    elif inzet != 'alles':
        inzet = int(inzet)
        if inzet > kapitaal:
            verificatie = 1
    else:
        inzet = kapitaal
    kapitaal -= inzet
    kleur = input('Zwart of wit?: ')
    showdown = input('Resultaat: ')
    if kleur == showdown and verificatie == 0:
        kapitaal += inzet * 2

if verificatie == 1:
    print('Je kunt geen {} dollar inzetten als je maar {} dollar hebt.'.format(inzet, kapitaal))
else:
    print('Je eindigt met '+ kapitaal +' dollar.')
