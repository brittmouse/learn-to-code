#!/usr/bin/python3
# WC17C3J3 - Uncrackable
# This program checks whether a given string is:
# A) between 8 and 12 characters long (inclusive);
# B) how many lowercase letters, uppercase letters, and digits are present, and;
# C) determines whether the password is valid based on those parameters.

def passwdcheck(user_in):
    # This checks whether the password is too short or long
    if len(user_in) < 8 or len(user_in) > 12:
        return 'Invalid'
    # Each  count_xyz  var is used to hold how many lowercase letters,
    # uppercase letters, and numbers are present
    count_lower = 0
    count_upper = 0
    count_num = 0
    # for loop iterates over each character in the string and checks the char-type
    for i in range(len(user_in)):
        if user_in[i].isupper():
            count_upper += 1
        elif user_in[i].islower():
            count_lower += 1
        elif user_in[i].isdecimal():
            count_num += 1
    # If any of the values are too low, the program returns 'Invalid';
    # otherwise, all counts are fine and the program returns 'Valid'.
    if count_lower < 3 or count_upper < 2 or count_num < 1:
        return 'Invalid'
    return 'Valid'
print(passwdcheck('PassW0rd')) # Returns 'Valid'
print(passwdcheck('CorrectHourseBatteryStaple')) # Returns 'Invalid'
