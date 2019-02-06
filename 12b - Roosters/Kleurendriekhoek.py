#G 71 R 82 Y 89
def volgende_rij(a):
    nieuw_rij = []
    for i in range(1, len(a)):
        if a[i] == a[i - 1]:
            nieuw_rij += a[i]
        else:
            sub = abs(ord(a[i - 1]) - ord(a[i]))
            if sub == 11:
                nieuw_rij += ['Y']
            elif sub == 7:
                nieuw_rij += ['G']
            else:
                nieuw_rij += ['R']
    return nieuw_rij