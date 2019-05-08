from math import pow

min = float(input('Hoeveel minuten?'))

toeschouwers = 50000 / (pow(2, min))

print(int(toeschouwers))