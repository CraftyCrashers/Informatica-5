x1 = 100
x2 = 50
x3 = 20
x4 = 10
x5 = 5
x6 = 2
x7 = 1
centen = int(input('Hoeveel centen?'))
y1 = centen % x1
y2 = y1 % x2
y3 = y2 % x3
y4 = y3 % x4
y5 = y4 % x5
y6 = y5 % x6
y7 = y6 % x7
z1 = int(centen / x1)
z2 = int(y1 / x2)
z3 = int(y2 / x3)
z4 = int(y3 / x4)
z5 = int(y4 / x5)
z6 = int(y5 / x6)
z7 = int(y6 / x7)
wisselgeld = str(centen) + ' cent kan je omwisselen in ' + str(z1 + z2 + z3 + z4 + z5 + z6 + z7) + ' muntstukken'
print(wisselgeld)
