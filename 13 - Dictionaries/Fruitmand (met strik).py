def fruitmand_maken(lis):
    dic = {}
    for i in lis:
        dic[len(i)] = i
    return dic


def fruitmand_inpakken(dic):
    lis, resultaat = [], []
    lis += dic.keys()
    lis.sort()
    for i in lis:
        resultaat += [dic.get(i)]
    return resultaat
