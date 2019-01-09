# D, C, B, A = 4 * A, B, C, D
# print(A, B, C, D)
A, B, C, D = 1, 0, 2, 3
while D * 1000 + C * 100 + B * 10 + A != 4 * (A * 1000 + B * 100 + C * 10 + D) or A == B or A == C or A == D\
        or B == C or B == D or C == D:
    while D < 9 and (D * 1000 + C * 100 + B * 10 + A != 4 * (A * 1000 + B * 100 + C * 10 + D) or A == B or A == C
                     or A == D or B == C or B == D or C == D):
        D += 1
    if C != 9 and (D * 1000 + C * 100 + B * 10 + A != 4 * (A * 1000 + B * 100 + C * 10 + D) or A == B or A == C
                   or A == D or B == C or B == D or C == D):
        C += 1
    elif B != 9 and C == 9 and (D * 1000 + C * 100 + B * 10 + A != 4 * (A * 1000 + B * 100 + C * 10 + D) or A == B or
                                A == C or A == D or B == C or B == D or C == D):
        C, B = 0, B + 1
    elif B != 9 and (D * 1000 + C * 100 + B * 10 + A != 4 * (A * 1000 + B * 100 + C * 10 + D) or A == B or A == C
                     or A == D or B == C or B == D or C == D):
        B += 1
    elif A != 9 and C == 9 and (D * 1000 + C * 100 + B * 10 + A != 4 * (A * 1000 + B * 100 + C * 10 + D) or A == B or
                                A == C or A == D or B == C or B == D or C == D):
        C, B, A = 0, 0, A + 1
    elif A != 9 and (D * 1000 + C * 100 + B * 10 + A != 4 * (A * 1000 + B * 100 + C * 10 + D) or A == B or A == C
                     or A == D or B == C or B == D or C == D):
        A += 1
    if D * 1000 + C * 100 + B * 10 + A != 4 * (A * 1000 + B * 100 + C * 10 + D) or (A == B or A == C or A == D
                                                                                    or B == C or B == D or C == D):
        D = 3
print(str(A) + str(B) + str(C) + str(D))
