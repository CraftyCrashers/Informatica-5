def is_letter(a):
    a = ord(a)
    a = bool(64 < a < 91 or 96 < a < 123)
    return a


def decodeer(message, positie1, positie2):
    if is_letter(positie1):
        message += positie2.upper()
    elif positie1 in "0123456789":
        message += positie2.lower()
    else:
        message += positie2
    return message


aantal_regels = int(input("Aantal Regels: "))
code = []
message = ""
for i in range(aantal_regels):
    code.append(input())
lengte = len(code[0])

if aantal_regels > 1 and lengte > 2:
    positie1 = None
    positie2 = code[0][0]
    sub = 0
    check = False
    for i in code[0][1:]:
        if i == positie1 == code[1][sub]:
            message = decodeer(message, positie1, positie2)
        sub += 1
        positie1, positie2 = positie2, i

if aantal_regels > 1 and lengte > 2:
    for i in range(aantal_regels - 2):
        i += 1
        positie1 = None
        positie2 = code[i][0]
        positie_onder = code[i + 1][1]
        positie_boven = code[i - 1][1]
        sub = code[i][1]
        if code[i - 1][0] == code[i + 1][0] == sub:
            message = decodeer(message, sub, positie2)
        sub = 0
        for j in code[i][1:]:
            if (j == positie1 and (j == positie_boven or j == positie_onder)) or \
               (positie1 == positie_onder == positie_boven) or (j == positie_boven == positie_onder != positie1):
                lijst = [positie1, j, positie_onder, positie_boven]
                if lijst.count(positie1) == 1:
                    parameter = j
                elif lijst.count(positie1) == 3:
                    parameter = positie1
                else:
                    check = True
                if is_letter(parameter) and check is False:
                    message += positie2.upper()
                elif parameter in "0123456789" and check is False:
                    message += positie2.lower()
                elif check is False:
                    message += positie2
                check = False
            sub += 1
            positie1, positie2, positie_onder, positie_boven = positie2, j, code[i + 1][sub], code[i - 1][sub]
        if positie1 == positie_onder == positie_boven:
            message = decodeer(message, positie1, positie2)


if aantal_regels > 1 and lengte > 2:
    positie1 = None
    positie2 = code[-1][0]
    sub = 0
    for i in code[-1][1:]:
        if i == positie1 == code[-2][sub]:
            message = decodeer(message, positie1, positie2)
        sub += 1
        positie1, positie2 = positie2, i

print(message)
