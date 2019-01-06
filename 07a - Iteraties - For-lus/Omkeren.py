# Invoer
woord = input('Geef een woord: ')

# Format
x = ''
for i in woord[::-1]:
    x += i
print(x)
