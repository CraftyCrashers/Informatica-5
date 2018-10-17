# Invoer

n = int(input('Geef de n-de getal : '))
if n <= 2:
    print(1)
    exit()
# Format

f_1, f_2 = 1, 1
if n > 2:
    for i in range(n - 2):
        uitkomst = f_1 + f_2
        f_2 += f_1
        f_1, f_2 = f_2, f_1
else:
    print(1)

# Uitvoer

print(uitkomst)
