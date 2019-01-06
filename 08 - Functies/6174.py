def splits(a):
    x = a // 1000
    y = (a // 100) % 10
    z = (a // 10) % 10
    u = a % 10
    return x, y, z, u


def oplopende_cijfers(a, b, c, d):
    x2, x3 = 0, 10
    x1 = min(a, b, c, d)
    x4 = max(a, b, c, d)
    for i in a, b, c, d:
        if x1 < i < x4 and i < x3 and x2 == 0:
            x2 = i
        elif x1 < i < x4 and i < x2:
            x3 = x2
            x2 = i
        elif x1 < i < x4 and i > x2:
            x3 = i
    return x1, x2, x3, x4


def op_af_getallen(a, b, c, d):
    x1 = a * 1000 + b * 100 + c * 10 + d
    x2 = d * 1000 + c * 100 + b * 10 + a
    return x1, x2


def verschil(a, b):
    a, b = int(a), int(b)
    return a - b


def kaprekar(a):
    x1 ,x2, x3, x4 = splits(a)
    x1, x2, x3, x4 = oplopende_cijfers(x1, x2, x3, x4)
    kleinste, grootste = op_af_getallen(x1, x2, x3, x4)
    a = verschil(grootste, kleinste)
    return'{} - {} = {}\n'.format(grootste, kleinste, a)


print(kaprekar(5342))