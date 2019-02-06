def printbaar_rek(a):
    VISUALISERING = ''
    for i in a[-1:-(len(a)):-1]:
        VISUALISERING += ''.join(i) + '\n'
    VISUALISERING += ''.join(a[0])
    return VISUALISERING


def speel(kleur, kolom, rek):
    i = 0
    while rek[i][kolom] != 'O' and rek[i] != rek[-1]:
        i += 1
    if rek[i][kolom] == 'O':
        rek[i][kolom] = kleur
    return rek
