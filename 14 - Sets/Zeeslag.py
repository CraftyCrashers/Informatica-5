def boot_overlappend(set1, set2):
    return len(set1.intersection(set2)) != 0


def boot_toevoegen(set1, set2):
    if boot_overlappend(set1, set2) is False:
        resultaat = set1.union(set2)
    else:
        resultaat = set2
    return resultaat


def vuur(string, set_):
    waarde, string = False, set([string])
    if string.isdisjoint(set_):
        set_.remove(string)
        waarde = True
    return waarde, set_
print(vuur('I7',{'E4', 'H8', 'I8', 'A2', 'G8', 'D4', 'C4', 'F8'}))