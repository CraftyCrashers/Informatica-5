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


def sorteer(a):
    x, b = 0, a
    for i in a:
        y = positie_laagste_ascii(b) + x  # Bepaalt plaats voor tweede vervanging
        a = a[:x] + teken_laagste_ascii(b) + a[x + 1:]  # Eerste vervanging
        a = a[:y] + b[:1] + a[y + 1:]
        # Tweede vervanging waarvan de positie van de laagste ascii vervangen word de oorspronkelijke eerste ascii
        b = a[x + 1:]  # Voorwaarde vervangen voor tweede ascii
        x += 1
    return a


def is_alfabetisch(a):
    return sorteer(a) == a
