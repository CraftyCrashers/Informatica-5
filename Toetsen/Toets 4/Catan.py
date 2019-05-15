ruilmarkt = {'goud': {'wol', 'steen', 'erts'}, 'wol': {'hout', 'steen', 'erts'}, 'erts': {'hout', 'steen'},
                    'steen': {'hout', 'graan'}}


def wisselen_mogelijk(ruilmarkt, gevraagd, gegeven):
    check = True
    for i in ruilmarkt[gevraagd]:
        if i not in gegeven:
            check = False
    return check


def bereken_ruilmiddelen(ruilmarkt, gevraagd):
    kostprijs = {}
    for i in gevraagd:
        for j in ruilmarkt[i]:
            if j in kostprijs:
                kostprijs[j] += 1
            else:
                kostprijs[j] = 1
    return kostprijs


def wisselen(ruilmarkt, gevraagd, huidige_grondstoffen):
    if wisselen_mogelijk(ruilmarkt, gevraagd, huidige_grondstoffen):
        huidige_grondstoffen.append(gevraagd)
        for i in ruilmarkt[gevraagd]:
            huidige_grondstoffen.remove(i)
    return huidige_grondstoffen
