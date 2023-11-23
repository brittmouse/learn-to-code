#!/usr/bin/python3
# DMOPC16C1P0 - C.C. & Cheese-kun

# Function approach
def pizza_satisfaction(width, cheese):
  if (width == 3) and (cheese >= 95):
    satisfaction = 'absolutely'
  elif (width == 1) and (cheese <= 50):
    satisfaction = 'fairly'
  else:
    satisfaction = 'very'
  return f'C.C. is {satisfaction} satisfied with her pizza'

print(pizza_satisfaction(2, 40)) # returns 'very'
print(pizza_satisfaction(3, 97)) # returns 'absolutely'
print(pizza_satisfaction(1, 10)) # returns 'fairly'


