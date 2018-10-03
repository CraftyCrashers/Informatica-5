# Invoer

codon = input('Geef een codon.')

# Heel wat mumbo jumbo

if len(codon) != 3:
    omschrijving = 'ongeldig'
elif codon == 'AUG':
    omschrijving = 'start'
elif codon == 'UAG' or codon == 'UGA' or codon == 'UAA':
    omschrijving = 'stop'
else:
    omschrijving = 'gewoon'

# Uitvoer
print('Het codon {} is een {} codon.'.format(codon, omschrijving))
