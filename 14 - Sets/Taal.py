def behoort_tot_taal(string, set_):
    string = set(string)
    string.discard(' ')
    return set_.issuperset(string)


def is_onleesbaar(string, set_):
    return len(set_.intersection(string)) == 0


def perfect_woord(string, set_):
    return set_.issubset(string)
