rood_wit = int(input("Aantal rode en witte rozen: "))
blauw_wit = int(input("Aantal blauwe en witte rozen: "))
operator = input("rood groter/kleiner dan wit")
if (blauw_wit - 6 + blauw_wit == rood_wit):
    blauw, wit, rood = 2, blauw_wit - 2, blauw_wit - 4
elif blauw_wit - 6 + blauw_wit + 1 == rood_wit:
    blauw, wit, rood = 2, blauw_wit - 2, blauw_wit - 3
elif operator == '<':
    blauw, wit, rood = blauw_wit - rood_wit + 2, rood_wit - 2, 2
else:
    blauw, wit, rood = blauw_wit - 2, 2, rood_wit - 2
print(blauw)
print(wit)
print(rood)
