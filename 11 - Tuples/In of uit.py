def binnen_of_buiten(p, q, s):
    xp, yp = p
    xq, yq = q
    xs, ys = s
    straal = ((xp - xq) ** 2 + (yp - yq) ** 2) ** 0.5
    lengte_s = ((xp - xs) ** 2 + (yp - ys) ** 2) ** 0.5
    if straal < lengte_s:
        resultaat = 'buiten'
    elif straal > lengte_s:
        resultaat = 'binnen'
    else:
        resultaat = 'op'
    resultaat = resultaat, round(lengte_s, 4)
    return resultaat
