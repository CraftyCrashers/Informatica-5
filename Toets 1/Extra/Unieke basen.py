aantal = int(input('Hoeveel basen gelezen?: '))
y, z = '', 0
for i in range(aantal):
    x = input('Huidige base?: ')
    if x == 'A' and 'A' not in y:
        y += x + ' '
        z += 1
    elif x == 'T' and 'T' not in y:
        y += x + ' '
        z += 1
    elif x == 'G' and 'G' not in y:
        y += x + ' '
        z += 1
    elif x == 'C' and 'C' not in y:
        y += x + ' '
        z += 1
if z == 1:
    print('De DNA-keting bevat 1 soort base: {}'.format(y))
else:
    print('De DNA-keting bevat {} verschillende soorten basen: {}'.format(z, y))
