#!/usr/bin/python3
# CCC15J1 - Special Day
def specialday(month, day):
  if month > 2 or (month == 2 and day > 18):
    return 'After'
  elif month == 1 or (month == 2 and day < 18):
    return 'Before'
  return 'Special'

print(specialday(1, 7))
print(specialday(10, 26))
print(specialday(2, 17))
print(specialday(2, 18))
print(specialday(2, 19))
