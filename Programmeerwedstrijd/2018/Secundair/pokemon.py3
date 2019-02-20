aantal = int(input())
for i in range(aantal):
    lijst = input()
    lijst = lijst.split()
    lijst = [int(x) for x in lijst]
    resultaat = int((lijst[0] * (lijst[1] ** (1 / 2)) * (lijst[2] ** (1 / 2)) * 0.7903 ** 2) / 10)
    print(i + 1, max(10, resultaat))
