def is_palindroom(a):
    x, y, parameter, verificatie = 0, -1, len(a), 'True'
    while parameter > x and verificatie == 'True':
        if a[x] != a[y]:
            verificatie = 'False'
        x, y = x + 1, y - 1
    x, y = x - 1, y + 1
    return a[x] == a[y]
