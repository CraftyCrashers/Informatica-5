# 5 invoer??? Waarom?
A1 = input(int('Hoeveel ogen bij eerste worp? (aanvaller)'))
A2 = input(int('Hoeveel ogen bij tweede worp? (aanvaller)'))
A3 = input(int('Hoeveel ogen bij derde worp? (aanvaller)'))
V1 = input(int('Hoeveel ogen bij eerste worp? (verdediger)'))
V2 = input(int('Hoeveel ogen bij tweede worp? (verdediger)'))

# Proces
if A1 >= V1:
    AV1 = 0
    VV1 = 1
elif A1 <= V1:
    AV1 = 1
    VV1 = 0
elif A1 == V1:
    AV1 = 1
    VV1 = 0

if A2 >= V2:
    AV2 = 0
    VV2 = 1
elif A2 <= V2:
    AV2 = 1
    VV2 = 0

if A2 == V2:
    if A1 == V1: