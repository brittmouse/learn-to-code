#!/usr/bin/python3
# COCI08C1P2 - Ptice

num = int(input())
correctAnswers = input()
patternA = 'ABC'
patternB = 'BABC'
patternC = 'CCAABB'
correctA, correctB, correctC = 0, 0, 0
i = 0
while i < num:
    ansA = patternA[i % 3]
    ansB = patternB[i % 4]
    ansC = patternC[i % 6]
    ansTrue = correctAnswers[i]
    if ansTrue == ansA:
        correctA += 1
    if ansTrue == ansB:
        correctB += 1
    if ansTrue == ansC:
        correctC += 1
    i += 1
player = ['Adrian', 'Bruno', 'Goran']
scores = [correctA, correctB, correctC]
best = max(scores)
print(best)
for x in range(3):
    if scores[x] == best:
        print(player[x])
