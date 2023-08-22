#!/usr/bin/python3
# CCC11S2 - Multiple Choice
# Checks how many correct guesses a student 
# gives for  n  number of questions
# where the first  n  inputs are student's answers
# and the second  n  inputs are the correct answers
n = int(input())
ans_std, ans_crt = [], [] # ans_std  &  ans_crt store student answer
                          # and correct answers in two separate lists for later comparison
count_crt = 0 #  count_crt  stores how many correct answers a student gave
for x in range(n): # takes the first  n  inputs and appends them to the student list
    ans_std.append(input().upper())
for i in range(n): # takes the second  n  inputs and appends them to the correct list
    ans_crt.append(input().upper())
for i in range(n): # compares each value in ans_std & ans_crt and increments count_crt if they match
    if ans_std[i] == ans_crt[i]:
        count_crt += 1
print(count_crt)
