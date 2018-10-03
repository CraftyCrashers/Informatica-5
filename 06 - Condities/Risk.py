# 5 invoer??? Waarom?
a1 = int(input('Hoeveel ogen bij eerste worp? (aanvaller)'))
a2 = int(input('Hoeveel ogen bij tweede worp? (aanvaller)'))
a3 = int(input('Hoeveel ogen bij derde worp? (aanvaller)'))
v1 = int(input('Hoeveel ogen bij eerste worp? (verdediger)'))
v2 = int(input('Hoeveel ogen bij tweede worp? (verdediger)'))

# Sorteren
A1 = max(a1, a2, a3)
if A1 == a1:
    a1 = 0
    A2 = max(a2, a3)
elif max(a1, a2, a3) == a2:
    a2 = 0
    A2 = max(a1, a3)
else:
    A2 = max(a1, a2)
V1 = max(v1, v2)
V2 = min(v1, v2)

# Proces
if A1 > V1:
    AV1 = 0
    VV1 = 1
else:
    AV1 = 1
    VV1 = 0

if A2 > V2:
    AV2 = 0
    VV2 = 1
else:
    AV2 = 1
    VV2 = 0

# Paar variabelen
AV = AV1 + AV2
VV = VV1 + VV2

# Uitvoer
if AV == VV:
    print('aanvaller verliest {} leger, verdediger verliest {} leger'.format(AV, VV))
else:
    print('aanvaller verliest {} legers, verdediger verliest {} legers'.format(AV, VV))
