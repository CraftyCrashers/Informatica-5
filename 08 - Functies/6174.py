def splits(a):
    x = a // 1000
    y = (a // 100) % 10
    z = (a // 10) % 10
    u = a % 10
    return x, y, z, u


def oplopende_cijfers(a, b, c, d):
    x1 = min(a, b, c, d)
    x4 = max(a, b, c, d)
    k2 = max(min(a, b), min(a, c), min(b, c))
    k3 = a + b + c + d - x1 - k2 - x4
    x2 = min(k3, k2)
    x3 = max(k3, k2)
    return x1, x2, x3, x4

# Makkelijker
# k2 = max(min(a, b), min(a, c), min(b, c))
# k3 = a + b + c + d - x1 - k2 - x4
# x2 = min(k3, k2)
# x3 = max(k3, k2)


def op_af_getallen(a, b, c, d):
    x1 = str(a) + str(b) + str(c) + str(d)
    x2 = x1[::-1]
    return x1, x2

# Tip: gebruik stringfuncties


def verschil(a, b):
    return str(int(a) - int(b))


def kaprekar(a):
    bewerkingen = ''
    while a != 6174:
        x1, x2, x3, x4 = splits(a)
        x1, x2, x3, x4 = oplopende_cijfers(x1, x2, x3, x4)
        kleinste, grootste = op_af_getallen(x1, x2, x3, x4)
        a = int(verschil(grootste, kleinste))
        bewerkingen += str(grootste) + ' - ' + str(kleinste) + ' = ' + str(a) + '\n'
    return bewerkingen[:-1]
