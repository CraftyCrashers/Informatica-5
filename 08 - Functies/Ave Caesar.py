def is_letter(a):
    a = ord(a)
    a = bool(64 < a < 91 or 96 < a < 123)
    return a


def roteer_letter(a, b):
    a = ord(a)
    if a < 91:
        x = 1
    else:
        x = 0
    if (a + b > 90 and x == 1) or a + b > 122:
        a -= 26 * ((b // 26.0001) + 1)
    return chr(int(a + b))


def versleutel(a, b):
    c = ''
    for i in a:
        if is_letter(i):
            c += roteer_letter(i, b)
        else:
            c += i
    return c
