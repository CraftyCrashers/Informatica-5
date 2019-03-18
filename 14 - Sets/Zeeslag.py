def boot_overlappend(set1, set2):
    return len(set1.intersection(set2)) != 0


def boot_toevoegen(set1, set2):
    if boot_overlappend(set1, set2) is False:
        resultaat = set1.union(set2)
    else:
        resultaat = set2
    return resultaat


def vuur(string, set_):
    check = False
    if string in set_:
        set_.remove(string)
        check = True
    return check, set_
