tjirps = int(input('Hoeveel aantal tjirps per minuut?'))
TF = tjirps - 40
TF /= 4
TF += 50
TC = tjirps - 40
TC /= 7
TC += 10
uitvoer1 = 'temperatuur (Fahrenheit): '
uitvoer1 += str(TF)
uitvoer2 = 'temperatuur (Celcius): '
uitvoer2 += str(TC)
print(uitvoer1)
print(uitvoer2)
