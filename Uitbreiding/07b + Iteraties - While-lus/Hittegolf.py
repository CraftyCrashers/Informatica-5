# Format
x = input('Graden celcius?: ')
y = 0
aanwezigheid = 'geen hittegolf'
while x != 'stop':
    x = float(x)
    if x >= 25:
        y += 1
        if y >= 5:
            aanwezigheid = 'hittegolf'
    else:
        y = 0
    x = input('Graden celcius?: ')

# Uitvoer
print(aanwezigheid)
