#!/usr/bin/python3
# CCC15J1 - Calorie Count (Darael's Approach)

menu = [[461, 431, 420, 0], [100, 57, 70, 0], [130, 160, 118, 0], [167, 266, 75, 0]]
c = 0
for s in menu:
  c += s[int(input())-1]
print(f'Your total calorie count is {c}')
