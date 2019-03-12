import sys
import io
inp = open('C:\data\\input.txt')
out = open('C:\data\\output.txt', 'w')
sys.stdin = inp
sys.stdout = out
def check_fracking(beeld):
    boven_ster, al_geplaatst, check, placeholder = [], [], False, []
    for i in beeld:
        placeholder += [i]
    for boven_check in range(len(beeld[0]) - 1):
        if beeld[0][boven_check] == '*' and beeld[0][boven_check + 1] != beeld[0][boven_check]:
            boven_ster += [boven_check]
    if placeholder[0][-1] == '*':
        boven_ster += [len(placeholder[0]) - 1]
    while boven_ster != [] and check == False:
        x = [[0, boven_ster[0]]]
        while x != [] and check == False:
            if placeholder[x[0][0]][x[0][1]] == '.':
                x.pop(0)
            else:
                if x[0][1] != 0 and [x[0][0], x[0][1] - 1] and placeholder[x[0][0]][x[0][1] - 1] == '*':
                        x.append([x[0][0], x[0][1] - 1])
                if x[0][1] != len(placeholder[0]) - 1 and \
                    [x[0][0], x[0][1] + 1] and placeholder[x[0][0]][x[0][1] + 1] == '*':
                        x.append([x[0][0], x[0][1] + 1])
                if x[0][0] != 0 and [x[0][0] - 1, x[0][1]] and placeholder[x[0][0] - 1][x[0][1]] == '*':
                        x.append([x[0][0] - 1, x[0][1]])
                if placeholder[x[0][0] + 1][x[0][1]] == '*' and x[0][0] + 1 == len(placeholder) - 1:
                        check = True
                elif placeholder[x[0][0] + 1][x[0][1]] == '*':
                        x.append([x[0][0] + 1, x[0][1]])
                placeholder[x[0][0]][x[0][1]] = '.'
        boven_ster.pop(0)
    return check


def volgende_dag(beeld):
    lijst_sterren, lijst_punten, rij, kolom = [], [], len(beeld), len(beeld[0])        
    for x in range(rij * kolom):
        if beeld[x % rij][x // rij] == '*':
            lijst_sterren += [[x % rij, x // rij]]
    for x in lijst_sterren:
        if [x[0], x[1] + 1] not in lijst_sterren or [x[0], x[1] - 1] not in lijst_sterren \
            or [x[0] + 1, x[1]] not in lijst_sterren or [x[0] - 1, x[1]] not in lijst_sterren:
            lijst_punten += [x]
    for x in lijst_punten:
        beeld[x[0]][x[1]] = '.'
    return beeld

aantal = int(input())
for i in range(aantal):
    rooster, aantal_dagen = [], 0
    rij = int(input())
    kolom = int(input())
    for j in range(rij):
        rooster += [[]]
        rooster[j] += input()
    while check_fracking(rooster) is True:
        rooster, aantal_dagen = volgende_dag(rooster), aantal_dagen + 1
    print(i + 1, aantal_dagen, rooster)