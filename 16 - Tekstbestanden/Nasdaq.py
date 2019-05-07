def just_for_this(nummer):
    if nummer % 1 == 0:
        nummer = int(nummer)
    else:
        nummer = float(nummer)
    return nummer


def lees_aandeel(file):
    resultaat = []
    with open(file) as file:
        content = file.read()
    content = content.strip()
    content = content.replace(',', '').split('\n')
    for i in content:
        resultaat.append(i.split(';'))
    return resultaat


def selecteer_kolom(criteria, file):
    resultaat = []
    content = lees_aandeel(file)
    index = content[0].index(criteria)
    content.pop(0)
    if criteria == 'Date':
        for i in content:
            resultaat.append(i[index])
    else:
        for i in content:
            resultaat.append(round(just_for_this(float(i[index])), 2))
    return resultaat


def hoogste_koers(lijst):
    return max(lijst)
