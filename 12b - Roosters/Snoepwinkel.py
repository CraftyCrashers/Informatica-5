from operator import itemgetter


def bereken_prijs(a):
    prijs = 0
    for i in a:
        prijs += i[1]
    return prijs


def winkelbriefje(a):
    lijst = []
    for i in a:
        lijst += [i[0]]
    return lijst


def sorteer(a):
    a.sort(key=itemgetter(1))
    return a
