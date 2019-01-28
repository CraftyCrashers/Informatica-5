def geldige_zet(a):
    geldig = True
    if len(a) == 2 or len(a) == 3:
        pion_check, cijfer_check = False, False
        for i in a:
            if i in 'KDTLP' and pion_check is False and geldig is True:
                pion_check = True
            elif i in 'abcdefgh' and cijfer_check is False and geldig is True:
                pion_check, cijfer_check = True, True
            elif i in '12345678' and cijfer_check is True and geldig is True:
                geldig = True
            else:
                geldig = False
    else:
        geldig = False
    return geldig


def geldige_zetten(a):
    geldig = True
    for i in a:
        if geldige_zet(i) is False:
            geldig = False
    return geldig
