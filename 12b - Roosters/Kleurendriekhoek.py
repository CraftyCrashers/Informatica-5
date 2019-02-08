#G 71 R 82 Y 89
def volgende_rij(a):
    nieuw_rij = []
    for i in range(1, len(a)):
        sub = abs(ord(a[i - 1]) - ord(a[i]))
        if a[i] == a[i - 1]:
            nieuw_rij += a[i]
        elif sub == 11:
            nieuw_rij += ['Y']
        elif sub == 7:
            nieuw_rij += ['G']
        else:
            nieuw_rij += ['R']
    return nieuw_rij


def driehoek(a):
    geen_VISUALISATIE = [a]
    for i in range(len(a) - 1):
        geen_VISUALISATIE = volgende_rij(geen_VISUALISATIE)
        a += geen_VISUALISATIE
    return a