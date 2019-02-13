def synoniemen(zin, dic):
    uitkomst = ''
    while zin.find(' ') != -1:
        if dic.get(zin[:zin.find(' ')]) is not None:
            uitkomst += dic.get(zin[:zin.find(' ')]) + ' '
        else:
            uitkomst += zin[:zin.find(' ') + 1]
        zin = zin[zin.find(' ') + 1:]
    if dic.get(zin) is not None:
        uitkomst += dic.get(zin)
    else:
        uitkomst += zin
    return uitkomst
