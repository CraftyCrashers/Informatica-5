Q1 = 2.0 * (10 ** -6)
Q2 = 1.0 * (10 ** -6)
r = float(input('Geef de straal in cm'))
r = r * (10 ** -2)
k = 8.99 * (10 ** 9)
FC = k
FC *= ((Q1 * Q2) / (r * r))
print(FC)
