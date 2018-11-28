def germaniseer(a):
    b = 0
    for i in range(len(a)):
        if a[i] == ' ':
            b = 1
        if b == 1:
            a = a[:i + 1] + a[i + 1].upper() + a[i + 2:]
            b = 0
    return a

