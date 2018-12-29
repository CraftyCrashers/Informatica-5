# Invoer
n = int(input('Aantal lifters?: '))

# Format
maximumScore, huidigeLifter, s = 0, 0, 0
for i in range(n):
    s = float(input('Score lifter?: '))
    if huidigeLifter == 0:
        if (i + 1) > (n / 2) and maximumScore < s:
            huidigeLifter = s
        elif maximumScore < s:
            maximumScore = s

if huidigeLifter == 0:
    huidigeLifter = s

# Uitvoer
print(huidigeLifter)