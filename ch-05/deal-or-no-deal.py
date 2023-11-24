#!/usr/bin/python3
# CCC07J3 - Deal or No Deal Calculator

cases = [
    [1, 100],
    [2, 500],
    [3, 1_000],
    [4, 5_000],
    [5, 10_000],
    [6, 25_000],
    [7, 50_000],
    [8, 100_000],
    [9, 500_000],
    [10, 1_000_000]
]

openCases = int(input())
casesOpened = []
for i in range(openCases):
    case = int(input())
    casesOpened.append(case)
offer = int(input())

totalCaseValue = 0
closedCaseCount = 10
for i in range(len(cases)):
    if cases[i][0] not in casesOpened:
        totalCaseValue += cases[i][1]
    else:
        closedCaseCount -= 1

meanCaseValue = totalCaseValue / closedCaseCount
if meanCaseValue >= offer:
    print("NO")
else:
    print("YES")
