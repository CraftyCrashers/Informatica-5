from random import randint
from time import time
import matplotlib.pyplot as plt


def genereer_rij(aantal):
    rij = []
    for i in range(aantal):
        rij.append(randint(0, aantal))
    return rij


def insertion_sort(a):
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i >= 0 and a[i] > key:
            a[i + 1] = a[i]
            i = i - 1
        a[i + 1] = key
    return a


def bubble_sort(rij):
    for i in range(0, len(rij) - 1):
        for j in range(len(rij) - 1, i, -1):
            if rij[j] < rij[j - 1]:
                rij[j], rij[j - 1] = rij[j - 1], rij[j]
    return rij


def merge_sort1(l1, l2): # Van Dominiek
    index_1 = 0
    index_2 = 0
    res = []
    while index_1 < len(l1) and index_2 < len(l2):
        if l1[index_1] < l2[index_2]:
            res.append(l1[index_1])
            index_1 += 1
        else:
            res.append(l2[index_2])
            index_2 += 1
    if index_1 < len(l1):
        res += l1[index_1:]
    else:
        res += l2[index_2:]
    return res

def merge_sort2(l1, l2): # Van mij
    res = []
    min_length = min(len(l1), len(l2))
    for i in range(min_length):
        if l1[i] < l2[i]:
            res.append(l1[i])
            res.append(l2[i])
        else:
            res.append(l2[i])
            res.append(l1[i])
    if min_length < len(l1):
        res += l1[min_length:]
    else:
        res += l2[min_length:]
    return res

def merge_sort(l):
    if len(l) > 1:
        mid = len(l) // 2
        s1 = merge_sort(l[:mid])
        s2 = merge_sort(l[mid:])
        return merge_sort1(s1, s2)
    else:
        return l

n, t_insertion, t_bubble, t_python, t_merge1, t_merge2 = [], [], [], [], [], []

i = 10
while i < 1000:

    rij_1 = genereer_rij(i)
    rij_2 = rij_1.copy()
    rij_3 = rij_1.copy()
    rij_4 = rij_1.copy()
    rij_5 = rij_1.copy()
    start = time()
    insertion_sort(rij_1)
    stop = time()

    t_insertion.append(stop - start)

    start = time()
    bubble_sort(rij_2)
    stop = time()

    t_bubble.append(stop - start)

    start = time()
    rij_3.sort()
    stop = time()

    t_python.append(stop - start)

    start = time()
    merge1(rij_4)
    stop = time()

    t_merge1.append(stop - start)
    n.append(i)

    start = time()
    merge2(rij_5)
    stop = time()

    t_merge2.append(stop - start)
    i += 50

plt.plot(n, t_insertion)
plt.plot(n, t_bubble)
plt.plot(n, t_python)
plt.plot(n, t_merge1)
plt.plot(n, t_merge2)
plt.xlabel('N')
plt.ylabel('t')
plt.gca().legend(('Insertion sort', 'Bubble sort', 'Python sort', 'Merge sort'))
plt.gcf().canvas.set_window_title('VinnyAndEli')
plt.title('Tijdsmeting')
plt.show()

