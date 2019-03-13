from operator import itemgetter
aantal = int(input())
for i in range(aantal):
    geval = int(input())
    lijst, plaats = [], [1]
    for j in range(geval):
        sub = input()
        sub = [sub.split()]
        lijst.extend(sub)
        lijst[j][1] = int(lijst[j][1]) * -1
    lijst.sort(key=itemgetter(1))
    lijst[0][1] = lijst[0][1] * -1
    for j in range(geval - 1):
        lijst[j + 1][1] = lijst[j + 1][1] * -1
        if lijst[j][1] == lijst[j + 1][1]:
            plaats.append(plaats[j])
        else:
            plaats.append(j + 2)
        print(str(i + 1) + ' ' + str(plaats[j]) + ' ' + str(lijst[j][0]) + ' ' + str(lijst[j][1]))
    print(str(i + 1) + ' ' + str(plaats[-1]) + ' ' + str(lijst[-1][0]) + ' ' + str(lijst[-1][1]))
