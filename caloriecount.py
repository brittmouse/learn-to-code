#!/usr/bin/python3
# CCC06J1 - Canadian Calorie Counting
def caloriecount(burger, side, drink, dessert):
  # All the 'menu_xyz' arrays hold the calorie values of the menu items at the appropriate index
  # I would have preferred to store those values in dicts but it was not working with my code
  menu_burger = [461, 431, 420, 0]
  menu_side = [100, 57, 70, 0]
  menu_drink = [130, 160, 118, 0]
  menu_dessert = [167, 266, 75, 0]
  # The 'order_xyz' vars store the value of the related array at the index 'xyz - 1' because inputs range 1-4 but indexes range 0-3
  order_burger = menu_burger[burger-1]
  order_side = menu_side[side-1]
  order_drink = menu_drink[drink-1]
  order_dessert = menu_dessert[dessert-1]
  # Used a f-string so it could return the sum wrapped inside the string
  return f'Your total calorie count is {order_burger + order_side + order_drink + order_dessert}'

print('CHIP\'S FAST FOOD EMPORIUM CALORIE COUNT')
# Each 'xyz' takes an integer 1-4 as an input with the associated menu items shows
burger = int(input('Choose your burger: cheeseburger (1), fish burger (2), veggie burger (3), or none (4): '))
side = int(input('Choose your side: fries (1), baked potato (2), chef salad (3), or none (4): '))
drink = int(input('Choose your drink: soft drink (1), orange_juice (2), milk (3), or none (4): '))
dessert = int(input('Choose your dessert: apple pie (1), sundae (2), fruit cup (3), or none (4): '))
print(caloriecount(burger, side, drink, dessert))
