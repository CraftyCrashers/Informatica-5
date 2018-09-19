t = float(input('Hoelang is de tijd in nanoseconden?'))
t = t * (10 ** -9)
c = 299792458
n = 1.000277

d = c * t
d /= (2 * n)
print(str(d), 'meter')
