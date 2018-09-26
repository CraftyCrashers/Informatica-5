#Geef waarden van x en y

x = float(input('Geef de eerste waarde'))
y = float(input('Geef de tweede waarde'))

#Berekening voor linker- en rechterlid
linkerlid = abs(x) - abs(y)
rechterlid = abs(x - y)

#uitvoer
print('{:.4f} ≤ {:.4f}'.format(linkerlid, rechterlid))
