# 5 invoer??? Waarom?
A1 = int(input('Hoeveel ogen bij eerste worp? (aanvaller)'))
A2 = int(input('Hoeveel ogen bij tweede worp? (aanvaller)'))
A3 = int(input('Hoeveel ogen bij derde worp? (aanvaller)'))
V1 = int(input('Hoeveel ogen bij eerste worp? (verdediger)'))
V2 = int(input('Hoeveel ogen bij tweede worp? (verdediger)'))

# Proces
if A1 > V1:
    AV1 = 0
    VV1 = 1
elif A1 < V1:
    AV1 = 1
    VV1 = 0
elif A1 == V1:
    AV1 = 1
    VV1 = 0

if A2 > V2:
    AV2 = 0
    VV2 = 1
elif A2 < V2:
    AV2 = 1
    VV2 = 0
elif A2 == V2 and A1 == V1:
    AV2 = 2
    VV2 = 0
elif not A2 == V2 and A1 == V1:
    AV2 = 1
    VV2 = 0

# Paar variabelen
AV = AV1 + AV2
VV = VV1 + VV2

# Uitvoer
print('aanvaller verliest {} legers, verdediger verliest {} legers'.format(AV, VV))
