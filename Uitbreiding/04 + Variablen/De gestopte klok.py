urenAndreaVertrek = int(input('In welk uur vertrekt Andrea?'))
minutenAndreaVertrek = int(input('In welk minuut vertrekt Andrea?'))
urenVriendinAankomst = int(input('In welk uur arriveert Andrea bij zijn vriendins huis?'))
minutenVriendinAankomst = int(input('In welk minuut arriveert Andrea bij zijn vriendins huis?'))
urenVriendinVertrek = int(input('In welk uur vertrekt Andrea terug naar huis?'))
minutenVriendinVertrek = int(input('In welk minuut vertrekt Andrea terug naar huis?'))
urenAndreaAankomst = int(input('In welk uur arriveert Andrea terug thuis?'))
minutenAndreaAankomst = int(input('In welk minuut arriveert Andrea terug thuis?'))

lunchTijd = (urenVriendinVertrek * 60 + minutenVriendinVertrek) - (urenVriendinAankomst * 60 + minutenVriendinAankomst)
totaalTijd = (urenAndreaAankomst * 60 + minutenAndreaAankomst) - (urenAndreaVertrek * 60 + minutenAndreaVertrek)
reisTijd = (totaalTijd - lunchTijd) / 2
reisUur = int(reisTijd / 60)
reis1 = reisTijd % 60
reisMinuut = int(reis1)
over = int((minutenVriendinVertrek + reisMinuut) / 60)
correctUur = int(urenVriendinVertrek + reisUur + over)
correctMinuut = (minutenVriendinVertrek + reisMinuut) % 60

print(lunchTijd)
print(totaalTijd)
print(reisTijd)
print(reisUur)
print(reisMinuut)
print(over)
print(correctUur)
print(correctMinuut)
6
32
14
14
17
21
13
29