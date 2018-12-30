# Format
x = input('Graden celcius?: ')
y, z, X = 0, 0, 'stop'
aanwezigheid = 'geen hittegolf'
while x != 'stop':
    x = float(x)
    if x >= 25:
        y += 1
        if x >= 30:
            z += 1
        x = input('Graden celcius?: ')
        if y >= 5 and z >= 3:
            x, X = 'stop', 'null'
            aanwezigheid = 'hittegolf'
    else:
        y, z = 0, 0
        x = input('Graden celcius?: ')

while x == 'stop' and X != 'stop':
    X = input('Typ gewoon stop.')

# Uitvoer
print(aanwezigheid)

# FREAKING FINALLY
