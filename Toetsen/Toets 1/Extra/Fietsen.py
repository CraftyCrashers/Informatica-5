x, y, z = int(input('Snelheid Stijn?: ')), int(input('Snelheid Kaat?: ')), int(input('Afstand tussen zijn huizen?: '))
seconden = 0
while z > 0:
    z, seconden = z - (x + y), seconden + 1
print('Na {} s hebben Stijn en Kaat elkaar ontmoet.'.format(seconden))
