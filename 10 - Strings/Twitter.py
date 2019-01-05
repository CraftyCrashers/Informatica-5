# Invoer
tweet = input('Geef een tweet: ')

# Format
x, y = 0, 0
while y != -1:
    if tweet[x:].find('#') >= 0:
        x = tweet[x:].find('#') + 1
        print(tweet[x:tweet[x:].find(' ') + x])
        tweet, x = tweet[x:], 0
    else:
        y = -1
