#!/usr/bin/python3
# COCI18C4P1 - Elder

owner = str(input())
count_own = [owner] 
n = int(input())
for i in range(n):
    duel = input().split(' ')
    if duel[1] == owner:
        owner = duel[0]
        if owner not in count_own:
            count_own.append(owner)
print(owner)
print(len(count_own))
