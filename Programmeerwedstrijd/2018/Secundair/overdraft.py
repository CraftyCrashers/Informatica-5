import sys
import io
inp = open('C:\data\\input.txt')
out = open('C:\data\\output.txt', 'w')
sys.stdin = inp
sys.stdout = out

aantal = int(input())
for i in range(aantal):
    saldo = int(input())
    sub = input().split()
    sub = [int(x) for x in sub]
    aantal_transacties = sub.pop(0)
    sub.sort()
    for j in range(aantal_transacties):
        storting = sub[j]
        saldo += storting
        if saldo < 0:
            saldo -= 35
    print(i + 1, saldo)
