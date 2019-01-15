def is_letter(a):
    a = str(a)
    a = ord(a)
    a = bool(64 < a < 91 or 96 < a < 123)
    return a


# Invoer
amino_zuur = input('Geef de aminozuur met de opeenvolgende atomen: ')
m = int(input('Positief bij hoeveel afwijkingen?: '))
n = int(input('Maximale aantal controles: '))

# Format
check_m = 0
for i in range(n):
    x, huidig_positie, huidig_atomen = 0, '', ''
    controle = input('Eerst nummer dan letters: ')
    while controle[-1] != controle[x]:
        if is_letter(controle[x]):
            huidig_atomen += controle[x]
        else:
            huidig_positie += str(controle[x])
        x += 1
    huidig_atomen += controle[x]
    if amino_zuur[int(huidig_positie) - 1] in huidig_atomen:
        check_m += 1
# Uitvoer
if check_m >= m:
    print('positief (' + str(check_m) + ')')
else:
    print('negatief (' + str(check_m) + ')')
