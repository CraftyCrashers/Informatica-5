sol = float(input('Hoelang in sol?'))
uurSol = 24
minuutSol = 39
secondeSol = 35.244
aardeMars = ((uurSol * 60 * 60) + (minuutSol * 60) + secondeSol) / (24 * 60 * 60)
tijdMars = sol * aardeMars
dagenMars = int(tijdMars / 1)

mars1 = (tijdMars % 1) * 24
urenMars = int(mars1 / 1)
mars2 = (mars1 % 1) * 60
minutenMars = int(mars2 / 1)
mars3 = (mars2 % 1) * 60
secondenMars = int(mars3 / 1)

#Er zijn geen 3 Marsen

uitvoer = str(int(sol))
uitvoer += ' sol = '
uitvoer += str(dagenMars)
uitvoer += ' dagen, '
uitvoer += str(urenMars)
uitvoer += ' uren, '
uitvoer += str(minutenMars)
uitvoer += ' minuten en '
uitvoer += str(secondenMars)
uitvoer += ' seconden'
print(uitvoer)