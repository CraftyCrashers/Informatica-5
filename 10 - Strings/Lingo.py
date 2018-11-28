def hint(a, b):
    c = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            c += a[i].replace(b[i], b[i].upper())
        elif a[i] in b:
            c += a[i]
        else:
            c += '.'
    return c
