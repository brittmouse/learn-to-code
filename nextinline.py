#!/usr/bin/python3
# CCC13J1 - Next in line
# function takes two arguments for the ages of the two younger kids to calculate the age of the oldest
def oldest_age(child_a, child_b):
  return child_b + (child_b - child_a)

print('NEXT IN LINE')
a = int(input('Enter the age of the youngest child: '))
b = int(input('Enter the age of the middle child: '))
print(oldest_age(a, b))
