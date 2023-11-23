#!/usr/bin/python3
# WC15C2J1 - A New Hope
def new_hope(n):
  # Takes an integer 'num' from 1 to 5 and repeats the word 'far' that many times
  farfar = ''
  i = 1
  while i <= n:
    farfar += 'far'
    if i != n:
      farfar += ', '
      i += 1
    else: break
  return f'A long time ago in a galaxy {farfar} away...'
print('A NEW HOPE')
num = int(input('Enter a number between 1 and 5: '))
print(new_hope(num))
