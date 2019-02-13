def gift_inschrijven(nieuw, dic):
    if dic.get(nieuw[0]) is not None:
        dic[nieuw[0]] += nieuw[1]
    else:
        dic[nieuw[0]] = nieuw[1]
    return dic
