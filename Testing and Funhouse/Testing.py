lijst = [[],[],[]]
for i in range(3):
    huidig_regel = input()
    for j in range(26):
        lijst[i].append(huidig_regel[j * 2:(j * 2) + 2])
aantal_gevraagd = int(input())
for i in range(aantal_gevraagd):
    uitvoer = ''
    uitvoer_lijst = [[],[],[]]
    for j in range(3):
        sub = input()
        for k in range(len(sub) // 2):
            uitvoer_lijst[j].append(sub[k * 2:(k * 2) + 2])
    for l in range((len(uitvoer_lijst[0]) // 2) * 3):
        