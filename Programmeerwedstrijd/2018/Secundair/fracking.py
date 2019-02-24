import sys
import io
inp = open('C:\data\\input.txt')
out = open('C:\data\\output.txt', 'w')
sys.stdin = inp
sys.stdout = out
def check_fracking(beeld):
    boven_ster, al_geplaatst, check = [], [], False
    for boven_check in range(len(beeld[0]) - 1):
        if beeld[0][boven_check] == '*' and beeld[0][boven_check + 1] != beeld[0][boven_check]:
            boven_ster += [boven_check]
    if beeld[0][-1] == '*':
        boven_ster += [len(beeld[0]) - 1]
    while boven_ster != [] and check == False:
        al_geplaatst, x = [], [[0, boven_ster[0]]]
        while x != [] and check == False:
            if x[0][1] != 0 and [x[0][0], x[0][1] - 1] not in al_geplaatst and\
                beeld[x[0][0]][x[0][1] - 1] == '*':
                    x.append([x[0][0], x[0][1] - 1])
            if x[0][1] != len(beeld[0]) - 1 and \
                    [x[0][0], x[0][1] + 1] not in al_geplaatst\
                and beeld[x[0][0]][x[0][1] + 1] == '*':
                    x.append([x[0][0], x[0][1] + 1])
            if x[0][0] != 0 and [x[0][0] - 1, x[0][1]] not in al_geplaatst\
                and beeld[x[0][0] - 1][x[0][1]] == '*':
                    x.append([x[0][0] - 1, x[0][1]])
            if beeld[x[0][0] + 1][x[0][1]] == '*' and\
                x[0][0] + 1 == len(beeld) - 1:
                check = True
            elif beeld[x[0][0] + 1][x[0][1]] == '*' and\
                [x[0][0] + 1, x[0][1]] not in al_geplaatst:
                x.append([x[0][0] + 1, x[0][1]])
            al_geplaatst.append([x[0][0], x[0][1]])
            x.pop(0)
        boven_ster.pop(0)
    return check


def volgende_dag(beeld):
    resultaat = []
    for i in range(len(beeld)):
        huidig_rij = beeld[i]
        check_rechts = True
        for j in range(len(huidig_rij) - 1):
            if check_rechts is True and huidig_rij[j + 1] == '.':
                huidig_rij[j] = '.'
                check_rechts = False
            elif check_rechts is False and huidig_rij[j] == '*':
                huidig_rij[j] = '.'
                check_rechts = True
        if huidig_rij[-2] == '.':
            huidig_rij[-1] = '.'
        resultaat += [huidig_rij]
    return resultaat

aantal = int(input())
for i in range(aantal):
    rooster, aantal_dagen = [], 0
    rij = int(input())
    kolom = int(input())
    for j in range(rij):
        rooster += [[]]
        rooster[j] += input()
    while check_fracking(rooster) is True:
        rooster = volgende_dag(rooster)
        aantal_dagen += 1
    print(i + 1, aantal_dagen)