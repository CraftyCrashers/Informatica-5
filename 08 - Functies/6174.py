def splits(a):
    x, y, a = '', 0, str(a)
    for i in a:
        if y != len(a) - 1:
            x, y = x + i + ', ', y + 1
        else:
            x += i
    return x


def oplopende_cijfers(a, b, c, d):
    x1 = min(a, b, c, d)
    x4 = max(a, b, c, d)
    if a == x1 or a == x4:
        a = 0
    if b == x1 or b == x4:
        b = 0
    if c == x1 or c == x4:
        c = 0
    if d == x1 or d == x4:
        d = 0
    x2 = min(a, b, c, d)
    x3 = max(a, b, c, d)
    return '({}, {}, {}, {})'.format(x1, x2, x3, x4)


def op_af_getallen(a, b, c, d):
    return"('{}{}{}{}', '{}{}{}{}')".format(a, b, c, d, d, c, b, a)


def verschil(a, b):
    a, b = int(a), int(b)
    return a - b


def kaprekar(a):
    b = oplopende_cijfers(splits(a))
    c = op_af_getallen(splits(b))
    grootste, kleinste = max(b, c), min(b, c)
    return '{} - {} = {}'.format(grootste, kleinste, verschil(max, min))


print(kaprekar(2741))
