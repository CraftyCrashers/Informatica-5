# Input

d = float(input('Initiele populatiedichtheid?: '))
r = float(input('Vruchtbaarheidsparameter?: '))
s = int(input('Aantal tijdstappen?: '))

# Format

formule = r * d * (1 - d)
for i in range(s):
    print(i * formule)
