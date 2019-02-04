def dubbels(a):
    queue = []
    while a != []:
        b = a.pop(0)
        if b in a:
            queue += [b]
            a.remove(b)
    return queue