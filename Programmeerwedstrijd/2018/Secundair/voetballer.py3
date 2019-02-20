aantal = int(input())
for i in range(aantal):
    resultaat, x1, y1 = 0, 0, 0
    for j in range(int(input())):
        x2, y2 = input().split()
        x2 = int(x2)
        y2 = int(y2)
        resultaat += abs(x2 - x1) + abs(y2 - y1)
        x1, y1 = x2, y2
    print(i + 1, resultaat)