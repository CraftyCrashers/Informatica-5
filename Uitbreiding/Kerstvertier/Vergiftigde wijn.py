# Format
aantal_dood = int(input('Hoeveel gevangenen is dood?: '))
bepaling_wijn = 0
for i in range(aantal_dood):
    huidig_dode_gevangene = ord(input('Welke gevangene is dood?: ')) - 65
    bepaling_wijn += 2 ** huidig_dode_gevangene
print('Fles #' + str(bepaling_wijn) + ' is vergiftigd.')
