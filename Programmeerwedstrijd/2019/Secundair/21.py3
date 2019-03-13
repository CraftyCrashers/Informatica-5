aantal_testgevallen = input()

for testgeval in range(int(aantal_testgevallen)):
    kaarten = input().replace("10", "hulp").replace("1", "11").replace("hulp", "10").replace("H", "10").replace("D", "10").replace("B", "10").split()
    kaarten_ints, check = [], True
    kaarten = [int(x) for x in kaarten]
    for i in range(len(kaarten)):
        kaarten_ints.append(int(kaarten[i]))
    kaartlist = []

    for i in range(len(kaarten)):
        if sum(kaartlist) < 17:
            kaartlist.append(kaarten[i])
        if sum(kaartlist) > 21 and (11 in kaartlist or check == True):
            kaartlist = [int(str(x).replace("11", "1")) for x in kaartlist]
            check = False

    print("{} {} {}".format(testgeval + 1, len(kaartlist), sum(kaartlist)))