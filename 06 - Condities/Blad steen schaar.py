# Invoer
speler1 = input('Speler 1, blad, steen of schaar?')
speler2 = input('Speler 2, cheat niet hé...')

a = 'blad'
b = 'steen'
c = 'schaar'
o = 'onbeslist'
s1 = 'speler 1 wint'
s2 = 'speler 2 wint'

# True or False

if speler1 == a and speler2 == a:
    resultaat = o
elif speler1 == a and speler2 == b:
    resultaat = s1
elif speler1 == a and speler2 == c:
    resultaat = s2
elif speler1 == b and speler2 == b:
    resultaat = o
elif speler1 == b and speler2 == c:
    resultaat = s1
elif speler1 == b and speler2 == a:
    resultaat = s2
elif speler1 == c and speler2 == c:
    resultaat = o
elif speler1 == c and speler2 == a:
    resultaat = s1
else:
    resultaat = s2

#Uitvoer
print(resultaat)
