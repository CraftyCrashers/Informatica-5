urenAndreaVertrek = int(input('In welk uur vertrekt Andrea?'))
minutenAndreaVertrek = int(input('In welk minuut vertrekt Andrea?'))
urenVriendinAankomst = int(input('In welk uur arriveert Andrea bij zijn vriendins huis?'))
minutenVriendinAankomst = int(input('In welk minuut arriveert Andrea bij zijn vriendins huis?'))
urenVriendinVertrek = int(input('In welk uur vertrekt Andrea terug naar huis?'))
minutenVriendinVertrek = int(input('In welk minuut vertrekt Andrea terug naar huis?'))
urenAndreaAankomst = int(input('In welk uur arriveert Andrea terug thuis?'))
minutenAndreaAankomst = int(input('In welk minuut arriveert Andrea terug thuis?'))

lunchTijd = (urenVriendinVertrek - urenVriendinAankomst) * 60 + (minutenVriendinVertrek - minutenVriendinAankomst)
totaalTijd = ((urenVriendinAankomst - urenAndreaVertrek) + (urenVriendinVertrek - urenAndreaAankomst)) * 60 + ((minutenVriendinAankomst - minutenAndreaVertrek) + (minutenVriendinVertrek - minutenAndreaAankomst)) + lunchTijd
reisTijd = (totaalTijd / lunchTijd) / 2 #Heen OF weer
reisTijdUur = int(reisTijd / 1)
reis1 = int(reisTijd % 1)
reisTijdMinuut = int(reis1 / 1)

correctUur = urenVriendinVertrek + reisTijdUur
correctMinuut = minutenVriendinVertrek + reisTijdMinuut
print(correctUur)
print(correctMinuut)
