aantal = int(input())
for i in range(aantal):
    geval = int(input())
    cijfers, resultaat = len(str(geval)), 0
    resultaat += (geval - (10 ** cijfers / 10) + 1) * cijfers
    cijfers -= 1
    while cijfers != 0:
        resultaat += (((10 ** cijfers) - 1) - (10 ** cijfers / 10) + 1) * cijfers
        cijfers -= 1
    print(i + 1, int(resultaat))
