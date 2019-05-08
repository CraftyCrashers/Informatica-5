def beweeg(positie, beweging):
    lijst_bewegingen, lijst_waarden = ['<', '^', '>', 'v'], [(-1, 0), (0, 1), (1, 0), (0, -1)]
    volgend_positie = positie[0] + lijst_waarden[lijst_bewegingen.index(beweging)][0],\
        positie[1] + lijst_waarden[lijst_bewegingen.index(beweging)][1]
    return volgend_positie


def teruggekeerd(a):
    horizontaal, verticaal, check = ['<', '>'], ['^', 'v'], False
    if ((a[0] in horizontaal and a[1] in horizontaal) or (a[0] in verticaal and a[1] in verticaal)) and a[0] != a[1]:
        check = True
    return check


def laatste_levende_positie(bewegingen):
    i, positie = 2, beweeg((0, 0), bewegingen[0])
    while teruggekeerd(bewegingen[i - 2:i]) is False and i != len(bewegingen):
        positie = beweeg(positie, bewegingen[i - 1])
        i += 1
    if teruggekeerd(bewegingen[i - 2:i]) is True:
        i -= 1
    else:
        positie = beweeg(positie, bewegingen[-1])
    return i, positie[0], positie[1]
