#!/usr/bin/python3
# ECOO17R3P1 - Baker Bonus

for dataset in range(10):
    f_d = input().split()
    franchises = int(f_d[0])
    days = int(f_d[1])

    performace = []
    bonuses = 0

    for i in range(days):
        row = input().split()
        for j in range(franchises):
            row[j] = int(row[j])
        performace.append(row)

    for row in performace:
        total = sum(row)
        if total % 13 == 0:
            bonuses += total / 13

    for col_index in range(franchises):
        total = 0
        for row_index in range(days):
            total += performace[row_index][col_index]
        if total % 13 == 0:
            bonuses += total / 13

    print(bonuses)
