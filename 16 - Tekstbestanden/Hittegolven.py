def bepaal_hittegolven(x):
    with open(x) as file:
        temperaturen = file.read().split()
    aantal_hittegolven = 0
    dagen = []
    huidige_dag = 0
    check_25 = 0
    check_30 = 0
    for i in temperaturen:
        i = int(i)
        huidige_dag += 1
        if i >= 30:
            check_30 += 1
            check_25 += 1
        elif i >= 25:
            check_25 += 1
        elif check_25 >= 5 and check_30 >= 3:
            aantal_hittegolven += 1
            check_30, check_25 = 0, 0
            dagen.append((begin_dag, huidige_dag - 1))
        else:
            check_25, check_30 = 0, 0
        if check_25 == 1:
            begin_dag = huidige_dag
    return aantal_hittegolven, dagen
