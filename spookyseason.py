#!/usr/bin/python3
# WC16C1J1 - A Spooky Season
def spooky(s):
  return 'sp' + (s * 'o') + 'ky'
print('WELCOME TO SPOOPOWEEN!!')
num = int(input('On a scale of 2 to 20, how spooky are you feeling? '))
print(spooky(num))
