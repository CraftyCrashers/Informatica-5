def dagprijs(a):
    prijslijst, totaleprijs = ['middagmaal', 5.3, 'soep', 1.7, 'vieruurtje', 2.3], 0
    a = list(a)
    for i in range(len(a) // 2):
        totaleprijs += prijslijst[prijslijst.index(a[i * 2]) + 1] * a[i * 2 + 1]
    return totaleprijs


def weekprijs(a):
    totaleprijs = 0
    for i in a:
        totaleprijs += dagprijs(i)
    return totaleprijs
