# Input
d_1 = float(input('Verkeersdichtheid eerste rijvak: '))
v_1 = float(input('Snelheid eerste rijvak: '))
d_2 = float(input('Verkeersdichtheid tweede rijvak: '))
v_2 = float(input('Snelheid tweede rijvak: '))

# Format
p_1 = min((d_1 * v_1) / 40, 1)
p_2 = min((d_2 * v_2) / 40, 1)

# Uitvoer
if min(p_1, p_2) > 0.7:
    print('zwart')
elif abs(p_1 - p_2) < 0.2:
    print('rood')
elif abs(p_1 - p_2) > 0.7:
    print('geel')
else:
    print('groen')