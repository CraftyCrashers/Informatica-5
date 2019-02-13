def doe_maar_gewoon(a):
    for i in range(0, len(a) - 2):
        if ord(a[i + 1]) - 32 == ord(a[i]):
            a = a[:i] + chr(ord(a[i]) + 32) + a[i + 1:]
    return a
