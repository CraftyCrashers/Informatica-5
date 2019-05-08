def ontdubbelen(a):
    i, x = 0, len(a) - 1
    while i != x:
        if a[i] == a[i + 1]:
            a, x = a[:i] + a[i + 1:], x - 1
        else:
            i += 1
    return a
