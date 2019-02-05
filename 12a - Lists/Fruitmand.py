def fruitstuk_toevoegen(mand, additie):
    i = 0
    while len(additie) > len(mand[i]) and mand[i] != mand[-1]:
        i = i + 1
    if len(additie) > len(mand[i]):
        mand.append(additie)
    elif len(additie) == len(mand[i]):
        mand[i] = additie
    else:
        mand.insert(i, additie)
    return mand


def maak_fruitmand(lijst):
    gemaakte_mand = [lijst[0]]
    for j in lijst:
        gemaakte_mand = fruitstuk_toevoegen(gemaakte_mand, j)
    return gemaakte_mand
