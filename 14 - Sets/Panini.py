def verzamel(huidig, set0, dubbels):
    dubbel_check, lijst = False, []
    if huidig in set0:
        for key, value in dubbels.items():
            if huidig in value and dubbel_check is False:
                dubbel_check = True
                if key + 1 in dubbels:
                    dubbels[key + 1].add(huidig)
                else:
                    dubbels[key + 1] = {huidig}
                dubbels[key].remove(huidig)
                if dubbels[key] == set():
                    dubbels.pop(key)
        if 1 in dubbels and dubbel_check is False:
            dubbels[1].add(huidig)
        elif dubbel_check is False:
            dubbels[1] = {huidig}
    else:
        set0.add(huidig)
    return set0, dubbels
