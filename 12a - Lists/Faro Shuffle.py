from math import floor


def nieuw_kaartspel(a, b):
    nieuw_lijst = []
    for i in range(1, len(a) * len(b) + 1):
        nieuw_lijst.append(a[floor((i - 1) / len(b))] + b[(i - 1) % len(b)])
    return nieuw_lijst


def splits_kaartspel(a):
    a, b = a[0:floor(len(a) / 2)], a[floor(len(a) / 2):]
    return a, b


def faro_shuffle(a, b):
    nieuw_lijst = []
    for i in range(len(a)):
        nieuw_lijst.append(a[i]), nieuw_lijst.append(b[i])
    if len(b) > len(a):
        nieuw_lijst.append(b[-1])
    return nieuw_lijst
