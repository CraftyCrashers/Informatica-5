def versleutel_woord(woord, aantal):
    resultaat = ''
    for i in woord:
        resultaat += chr(ord(i.upper()) + aantal)
    return resultaat


def versleutel_zin(zin, aantal):
    zin = versleutel_woord(zin, aantal)
    zin = zin.replace('@', ' ').replace(chr(32 + aantal), '@')
    return zin
