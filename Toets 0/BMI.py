lengte = float(input('Lengte?'))
naam_1 = input('Eerste naam?')
massa_1 = float(input('Massa eerste persoon?'))
naam_2 = input('Tweede naam?')
massa_2 = float(input('Massa tweede persoon?'))

BMI_1 = massa_1 / (lengte ** 2)
BMI_2 = massa_2 / (lengte ** 2)

hoogste_BMI = max(BMI_1, BMI_2)
if hoogste_BMI < 18.5:
    indicatie = 'ondergewicht'
elif hoogste_BMI < 25:
    indicatie = 'gezond gewicht'
elif hoogste_BMI < 30:
    indicatie = 'overgewicht'
else:
    indicatie = 'obees'

if hoogste_BMI == BMI_2:
    naam_hoogste_BMI = naam_2
else:
    naam_hoogste_BMI = naam_1

if indicatie == 'obees':
    print('{} heeft het hoogste BMI ({:.2f}) en is {}.'.format(naam_hoogste_BMI, hoogste_BMI, indicatie))
elif indicatie == 'gezond gewicht':
    print('{} heeft het hoogste BMI ({:.2f}) en heeft een {}.'.format(naam_hoogste_BMI, hoogste_BMI, indicatie))
else:
    print('{} heeft het hoogste BMI ({:.2f}) en heeft {}.'.format(naam_hoogste_BMI, hoogste_BMI, indicatie))
