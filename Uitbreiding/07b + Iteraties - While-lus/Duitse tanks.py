# Invoer
m = int(input('Eerste serienummer?: '))

# Format
n, grootsteSerieNummer = 0, 0
while m > 0:
    n += 1
    grootsteSerieNummer = max(m, grootsteSerieNummer)
    m = int(input('Volgende serienummer?: '))
schatting = round((((n + 1) * grootsteSerieNummer) / n) - 1)

# Uitvoer
print('Het aantal geproduceerde tanks wordt geschat op ' + str(schatting) + '.')
