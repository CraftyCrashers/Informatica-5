#Invoer 2 waarden
T = float(input('Luchttemperatuur in graden Celcius'))
W = (float(input('Windsnelheid in kilometer per uur')) / 3.6)

#Formule
gevoelstemperatuur = 13.12 + 0.6215 * T + ((0.3965 * T) - 11.37) * ((3.6 * W) ** 0.16)

#Uitvoer
print(gevoelstemperatuur)
