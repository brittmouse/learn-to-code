#!/usr/bin/python3
# ccc18j1, Telemarketers
def telemarketer(num):
  # Checks 1) if the first number is either an '8' or '9',
  # 2) if the second and third numbers are the same, and
  # 3) if the fourth number is either an '8' or a '9'
  # and returns True if all conditions are met; otherwise it returns False
  return (num[0] == '8' or num[0] == '9') and (num[1] == num[2]) and (num[3] == '8' or num[3] == '9')
print('TELEMARKETER PHONE NUMBER CHECKER')
user_in = input('Enter the last 4 digits of the incoming phone number: ')
print(telemarketer(user_in))
