# Invoer 2 waarden

T = float(input('Geef de temperatuur in kelvin.'))
L = float(input('Geef de lichtkracht relatief ten opzichte van de zon'))

# Voorwaarden grafiek

if L > 10000:
    klassSter = 'superreuzen (a)'
elif L > 1000:
    klassSter = 'superreuzen (b)'
elif L > 100 and T < 7500:
    klassSter = 'heldere reuzen'
elif L > 10 and T < 6000:
    klassSter = 'reuzen'
elif (L < 0.01 and T > 5000) or (L < 0.0001 and T > 3000):
    klassSter = 'witte dwergen'
else:
    klassSter = 'hoofdreeks'

# Uitvoer

print(klassSter)
