a = input()
b = input()
c = input()
dic = {}
for i in range(26):
    dic[a[i * 2:(i * 2) + 2] + b[i * 2:(i * 2) + 2] + c[i * 2:(i * 2) + 2]] = chr(65 + i)
for i in range(int(input())):
    resultaat = ''
    a = input()
    b = input()
    c = input()
    for j in range(len(a) // 2):
        resultaat += dic.get(a[j * 2:(j * 2) + 2] + b[j * 2:(j * 2) + 2] + c[j * 2:(j * 2) + 2])
    print(i + 1, resultaat)
