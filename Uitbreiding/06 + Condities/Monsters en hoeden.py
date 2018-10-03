# Invoer

p1 = input('Welke kleur heeft de hoed van persoon 1?')
p2 = input('Welke kleur heeft de hoed van persoon 2?')
kleurBlind = int(input('Welk persoon zegt de omgekeerde van wat hij ziet? 1 of 2?'))

# Paar variabelen

zwart = 'zwart'
wit = 'wit'

# Puzzelwerk

if kleurBlind == 1 and p2 == zwart:
    p2 = wit
elif kleurBlind == 1 and p2 == wit:
    p2 = zwart
elif kleurBlind == 2 and p1 == zwart:
    p1 = wit
else:
    p1 = zwart

#Wat zegt de mannen

print(p1, p2)
