# Input

woord = input('Wat is het verborgen woord?: ')
geldbedrag = int(input('Wat is het prijs?: '))
letter = input('Welke letter bevat het woord?: ')

# Format

l, totaal, geraden_letters = 0, 0, ''
while letter in woord and l not in geraden_letters:
    totaal += geldbedrag
    geraden_letters += letter
    letter = input('Welke letter bevat het woord?: ')

# Uitvoer

print(totaal)
