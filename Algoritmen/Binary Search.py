from time import time
from random import randint
import matplotlib.pyplot as plt
def genereer_rij(aantal):
    rij = []
    for i in range(aantal):
        rij.append(randint(0, aantal))
    return rij

def lineair_search(lijst, getal):
    index = 0
    while index < len(lijst) and lijst[index] != getal:
        index += 1
    return index < len(lijst)

def binaire_search(lijst, low, high, getal):
    if low > high:
        return False
    mid = (low + high) // 2
    if lijst[mid] == getal:
        return True
    elif getal > lijst[mid]:
        return binaire_search(lijst, low, mid - 1, getal)
    else:
        return binaire_search(lijst, mid + 1, high, getal)

n, t_bs, t_ls = [], [], []
i = 10
while i < 1000:
    rij_1 = genereer_rij(i)
    rij_1.sort()
    rij_2 = rij_1.copy()
    getal = rij_1[len(rij_1) // 2]
    start = time()
    print(binaire_search(rij_1, 0, len(rij_1) - 1, getal), 0)
    stop = time()
    t_bs.append(stop - start)
    start = time()
    print(lineair_search(rij_2, getal), 1)
    stop = time()
    t_ls.append(stop - start)
    n.append(i)
    i += 50

plt.plot(n, t_bs)
plt.plot(n, t_ls)
plt.gca().legend(('Binaire Search', 'Lineaire Search'))
plt.show()