x = int(input('Aantal stappen?: '))
y, z = 0, 0
for i in range(x):
    if i / 2 == i // 2:
        y += 2 + i
    else:
        z += 1
        y -= z
print(y)
