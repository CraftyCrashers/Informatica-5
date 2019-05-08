def bereken_prijs(a):
    prijs_per_letter = float(a[a.find('<') + 1:a.find('>')])
    return a[:a.find('<')], prijs_per_letter * a.find('<')


def toon_boodschappen(a):
    prijs, boodschap = 0, ''
    while a.find('>') != -1:
        prijs += float(a[a.find('<') + 1:a.find('>')]) * a.find('<')
        boodschap += a[:a.find('<')] + '\n'
        a = a[a.find('>') + 1:]
    boodschap = str(prijs) + '\n' + boodschap[:len(boodschap) - 1]
    return boodschap
