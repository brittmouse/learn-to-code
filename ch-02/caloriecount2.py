#!/usr/bin/python3
# CCC006J1 - Canadian Calorie Counting
def caloriecount(burger, side, drink, dessert):
  menu = [[461, 431, 420, 0], [100, 57, 70, 0], [130, 160, 118, 0], [167, 266, 75, 0]]
  return f'Your total calorie count is {menu[0][burger-1] + menu[1][side-1] + menu[2][drink-1] + menu[3][dessert-1]}'

print('CHIP\'S FAST FOOD EMPORIUM CALORIE COUNT')
burger = int(input())
side = int(input())
drink = int(input())
dessert = int(input())
print(caloriecount(burger, side, drink, dessert))
