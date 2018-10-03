# Invoer
e = int(input('Hoeveel elektronen?'))

# Bepalen van de schil
if e <= 2:
    schil = 'K'
elif e <= 10:
    schil = 'L'
elif e <= 28:
    schil = 'M'
elif e <= 60:
    schil = 'N'
elif e <= 92:
    schil = 'O'
elif e <= 124:
    schil = 'P'
else:
    schil = 'Q'

# Uitvoer
print('De {}-schil is de buitenste schil van een stabiel atoom met {} elektronen.'.format(schil, e))
