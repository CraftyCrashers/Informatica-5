# Input

woord = input('Wat is het verborgen woord?: ')
geldbedrag = int(input('Wat is het prijs?: '))
letter = input('Welke letter bevat het woord?: ')

# Format

l, totaal = 0, 0
while letter in woord and l != letter:
    totaal += geldbedrag
    l = letter
    letter = input('Welke letter bevat het woord?: ')

# Uitvoer

print(totaal)
