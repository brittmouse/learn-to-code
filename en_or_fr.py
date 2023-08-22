#!/usr/bin/python3
# CCC11S1 - English or French
# Determines whether input/s from the user is more likely English or French
count_t, count_s = 0, 0
loop = int(input())
for i in range(loop):
    user_in = input()
    for x in range(len(user_in)):
        if user_in[x].lower() == 't':
            count_t += 1
        elif user_in[x].lower() == 's':
            count_s += 1
if count_t <= count_s:
    print('French')
else:
    print('English')
