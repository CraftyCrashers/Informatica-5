def is_letter(a):
    a = str(a)
    a = ord(a)
    a = bool(64 < a < 91 or 96 < a < 123)
    return a


def positie_laagste_ascii(a):
    x, y, laagste = 0, 0, 200
    for i in a:
        if laagste > ord(i):
            laagste = ord(i)
            y = x
        x += 1
    return y


def teken_laagste_ascii(a):
    laagste = 200
    for i in a:
        if laagste > ord(i):
            laagste = ord(i)
    return chr(laagste)
