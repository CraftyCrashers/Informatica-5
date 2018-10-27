from math import sqrt
# Input

a = float(input('Geef een getal: '))

# Format

if a < 2:
    print('{:.2f} ∉ dom(f)'.format(a))
elif a == 2:
    print('{:.2f} is nulpunt van f'.format(a))
else:
    b = sqrt(a - 2)
    print('f({:.2f}) = {:.2f}'.format(a, b))
