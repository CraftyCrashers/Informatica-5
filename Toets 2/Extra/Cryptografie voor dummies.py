def versleutel_woord(woord, aantal):
    for i in range(len(woord)):
        woord = woord[:i] + chr(ord(woord[i].upper()) + aantal) + woord[i + 1:]
    return woord
print(versleutel_woord('van', 14))