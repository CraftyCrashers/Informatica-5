# Invoer in verband met https://youtu.be/bOpf6KcWYyw
x = input('Trek aan de hendel van de wissel?')
y = input('Man van de brug duwen?')

# Stroomdiagram vertaalt in codeertaal
if x == 'ja':
    if y == 'ja':
        print(2)
    elif y == 'nee':
        print(1)
elif x == 'nee':
    if y == 'ja':
        print(1)
    elif y == 'nee':
        print(5)
