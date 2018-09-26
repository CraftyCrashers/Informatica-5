#Invoer voor 2 termen
x = float(input('Eerste term'))
y = float(input('Tweede term'))

#Uitkomst som van 2 termen
z = x + y

aantalTekens = len('^{:f} + ^{:f} = {:f}'.format(x, y, z))
print('{:>6.0f} + {:<6.0f} = {:.0f}'.format(x, y, z))
print('{:>6.0f} + {:<6.0f} = {:.0f}'.format(x * 10, y * 10, z * 10))
print('{:>6.0f} + {:<6.0f} = {:.0f}'.format(x * 100, y * 100, z * 100))
print('{:>6.0f} + {:<6.0f} = {:.0f}'.format(x * 1000, y * 1000, z * 1000))
print('{:>6.0f} + {:<6.0f} = {:.0f}'.format(x * 10000, y * 10000, z * 10000))
