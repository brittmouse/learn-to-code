#!/usr/bin/python3
# ECOO17R1P1 - School Trip

YEAR_COSTS = [12, 10, 7, 5]
for dataset in range(10):
    cost = int(input())
    s = input()
    studentsCount = int(input())
    
    proportions = s.split()
    for i in range(len(proportions)):
        proportions[i] = float(proportions[i])

    studentsPerYear = []
    for num in proportions:
        studentsPerYear.append(int(studentsCount * num))
    if sum(studentsPerYear) < studentsCount:
        remainder = studentsCount - sum(studentsPerYear)
        maxYear = max(studentsPerYear)
        studentsPerYear[maxYear] += remainder

    totalRaised = 0
    for i in range(len(studentsPerYear)):
        totalRaised += (studentsPerYear[i] * YEAR_COSTS[i])

    if totalRaised / 2 < cost:
        print('YES')
    else:
        print('NO')
