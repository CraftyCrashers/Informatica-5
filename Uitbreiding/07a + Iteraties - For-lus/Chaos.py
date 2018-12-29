# Input

d = float(input('Initiele populatiedichtheid?: '))
r = float(input('Vruchtbaarheidsparameter?: '))
s = int(input('Aantal tijdstappen?: '))

# Format

for i in range(s):
    print(d)
    d = r * d * (1 - d)
