def kleur_toevoegen(lijst, kleur):
    cataloog = ['rood', 'groen', 'blauw']
    lijst[cataloog.index(kleur)] += 1
    return lijst


def is_wit(lijst):
    return lijst[0] == lijst[1] == lijst[2]


def verf_verzamelen(verzameling):
    huidig_positie, lijst = 0, [0, 0, 0]
    while len(verzameling) // 3 > huidig_positie and (is_wit(lijst) is False or lijst == [0, 0, 0]):
        huidig_positie += 1
        lijst = lijst[0] + verzameling[(huidig_positie - 1) * 3:huidig_positie * 3].count('rood'),\
            lijst[1] + verzameling[(huidig_positie - 1) * 3:huidig_positie * 3].count('groen'),\
            lijst[2] + verzameling[(huidig_positie - 1) * 3:huidig_positie * 3].count('rood')
    if is_wit(lijst) is False:
        resultaat = None
    else:
        resultaat = (huidig_positie * 3, list(lijst))
    return resultaat
