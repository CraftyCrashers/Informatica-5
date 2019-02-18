def woord_frequentie(a):
    dic = {}
    while a.find(' ') != -1:  # While tot er geen tekst meer is
        sub = a[:a.find(' ')].lower().replace('.', '').replace(',', '')  # Vervangt alle nodige punten en komma's
        if sub in dic:  # Voegt het aan een dictionary
            dic[sub] += 1
        else:  # Voegt een extra waarde aan het bestaande woord
            dic[sub] = 1
        a = a[a.find(' ') + 1:]  # Verandert de tekst voor de volgende
    sub = a.lower().replace('.', '').replace(',', '').replace(' ', '')  # Herhaal voor de tweede
    if sub in dic:
        dic[sub] += 1
    else:
        dic[sub] = 1
    return dic


def woorden_per_frequentie(a):
    lis, dic, a = [], {}, woord_frequentie(a)
    lis += a.keys()
    for i in lis:
        if a.get(i) in dic:
            dic[a.get(i)] += [i]
        else:
            dic[a.get(i)] = [i]
    return dic


def meest_gebruikte_woorden(a):
    a, lis, sub = woorden_per_frequentie(a), [], []
    sub += a.keys()
    sub.sort()
    lis = a.get(sub[-1])
    return lis
