def dronken_voeren(woord):
    x, resultaat, hoofdletter_klinker_check = 0, '', 0
    for i in woord:
        if hoofdletter_klinker_check == 1:
            resultaat += str.upper(i)
            hoofdletter_klinker_check = 0
        elif x / 2 == x // 2 and x != 0:
            if str.upper(i) in 'AEOUI':
                hoofdletter_klinker_check = 1
            resultaat += str.upper(i)
        elif x == 0:
            if str.upper(i) in'AEOUI':
                hoofdletter_klinker_check = 1
            resultaat += i
        else:
            resultaat += str.lower(i)
        x += 1
    return resultaat
