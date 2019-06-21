def faculteit(n):
    f = 1
    i = 2
    while i <= n:
        f *= i
        i += 1
    return f


def is_palindroom(woord):
    print(woord)
    if len(woord) <= 1:
        return True
    else:
        res = is_palindroom(woord[1: -1])
        return woord[0] == woord[-1] and res
print(is_palindroom('koortsmeetsysteemstrook'))