aantal_regels = int(input())
for i in range(aantal_regels):
    aantal_waarden, lijst = int(input()), []
    for j in range(aantal_waarden):
        lijst.append(int(input()))
    lijst.sort()
    print(i + 1, lijst[0], lijst[-1])
