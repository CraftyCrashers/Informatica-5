def hoogtemeters(a):
    for i in range(len(a) - 1):
        a[i] = a[i + 1] - a[i]
    a.pop(-1)
    return a


def dalen_en_stijgen(a):
    dalen, stijgen = 0, 0
    for i in a:
        if i < 0:
            dalen -= i
        else:
            stijgen += i
    return dalen, stijgen
