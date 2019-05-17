kaart = {'Brugge': {'Gent', 'Antwerpen'}, 'Kortrijk': {'Gent'}, 'Gent': {'Antwerpen', 'Kortrijk', 'Brugge'}, 'Antwerpen': {'Gent', 'Brussel', 'Brugge'}, 'Brussel': {'Hasselt', 'Antwerpen'}, 'Hasselt': {'Brussel'}}


def bestaat_weg(stad1, stad2, kaart):
    return stad1 in kaart[stad2]


def geen_dubbelburen(stad1, stad2, kaart):
    connectie1 = kaart[stad1]
    connectie2 = kaart[stad2]
    set = connectie1.difference(connectie2)
    set.update(connectie2.difference(connectie1))
    set.discard(stad1)
    set.discard(stad2)
    return set


def bereikbaarheid_meest_afgelegen_stad(kaart):
    resultaat = 999
    for i in kaart.values():
        if resultaat > len(i):
            resultaat = len(i)
    return resultaat


def bestaat_route(route, kaart):
    resultaat = True
    for i in range(0, len(route) - 1):
        if not bestaat_weg(route[i], route[i + 1], kaart):
            resultaat = False
            break
    return resultaat
