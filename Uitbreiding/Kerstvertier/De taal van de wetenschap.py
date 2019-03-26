s1 = input("Eerste string: ")
s2 = input("Tweede string: ")
index = 0
lengte = max(len(s1), len(s2)) - 1
while lengte > index and s1[index] == s2[index]:
    index += 1
first_break = index
index = -1
lengte *= -1
while lengte <= index and s1[index] == s2[index]:
    index -= 1
if index == -1:
    last_break = (lengte * -1)
else:
    last_break = index

stam = max(len(s1[first_break:last_break + 1]), len(s2[first_break:last_break + 1]))
info = " " * first_break + "┏" + s1[first_break:last_break + 1].center(stam) + '┓\n'\
       + s1[:first_break] + '┫' + " " * stam + '┣' + s1[last_break + 1:] + "\n"\
       + " " * first_break + "┗" + s2[first_break:last_break + 1].center(stam) + '┛'
print(info)