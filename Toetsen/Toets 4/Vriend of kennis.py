kennissen = {'Eva': {'Margaux', 'Arno'}, 'Arno': {'Eva', 'Jens'}, 'Jens': {'Margaux', 'Eva'}, 'Margaux': set()}
def vriend_of_kennis(kennissen, persoonA, persoonB):
    connectieA = kennissen[persoonA]
    connectieB = kennissen[persoonB]
    if persoonB in connectieA and persoonA in connectieB:
        resultaat = "{} en {} zijn vrienden".format(persoonA, persoonB)
    elif persoonB in connectieA:
        resultaat = "{} kent {}".format(persoonA, persoonB)
    elif persoonA in connectieB:
        resultaat = "{} kent {}".format(persoonB, persoonA)
    else:
        resultaat = "{} en {} kennen elkaar niet".format(persoonA, persoonB)
    return resultaat


def unieke_kennissen(kennissen, persoonA, persoonB):
    resultaat = kennissen[persoonA].difference(kennissen[persoonB])
    resultaat.update(kennissen[persoonB].difference(kennissen[persoonA]))
    resultaat.discard(persoonA)
    resultaat.discard(persoonB)
    return resultaat


def bekendheid(kennissen):
    lijst = []
    resultaat = {}
    for i in kennissen.values():
        lijst.extend(list(i))
    for i in lijst:
        if i in resultaat.keys():
            resultaat[i] += 1
        else:
            resultaat[i] = 1
    return resultaat


def meest_gekende(kennissen):
    resultaat = []
    grootste_aantal = 0
    for i in kennissen.keys():
        connectie = kennissen[i]
        if connectie > grootste_aantal:
            resultaat = [i]
            grootste_aantal = connectie
        elif connectie == grootste_aantal:
            resultaat.append(i)
    return resultaat
