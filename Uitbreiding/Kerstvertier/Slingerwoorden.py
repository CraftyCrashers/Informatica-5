def graad(a):
    welk_graad = 0
    for i in range(len(a) - 1):
        if a[:i + 1] == a[-i - 1:]:
            welk_graad = i + 1
    return welk_graad


def slinger(woord, aantal):
    if graad(woord) == 0:
        resultaat = woord * aantal
    elif aantal != 0:
        resultaat = woord[:-graad(woord)] * aantal + woord[-graad(woord):]
    else:
        resultaat = ''
    return resultaat
