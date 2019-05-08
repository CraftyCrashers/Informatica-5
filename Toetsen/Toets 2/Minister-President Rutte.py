def tel_woorden(a):
    aantal_woorden = 1
    while a.find(' ') != -1:
        huidig_positie = a.find(' ')
        aantal_woorden += 1
        a = a[huidig_positie + 1:]
    return aantal_woorden


def langste_zin(a):
    maximaal_aantal_woorden = 0
    while a.find('.') != -1:
        huidig_positie_punt = a.find('.')
        huidig_aantal_woorden = tel_woorden(a[:huidig_positie_punt])
        maximaal_aantal_woorden = max(huidig_aantal_woorden, maximaal_aantal_woorden)
        a = a[huidig_positie_punt + 2:]
    return maximaal_aantal_woorden


# Andere optie
def tel_woorden_ander_optie(zin):
    lengte = len(zin)
    lengte_zonder_spaties = len(zin.replace(' ', ''))
    return lengte - lengte_zonder_spaties + 1