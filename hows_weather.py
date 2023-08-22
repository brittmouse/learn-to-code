#!/usr/bin/python3
# WC17C1J2 - How's the Weather?
def c_to_f(cel):
  return (cel * 9 / 5) + 32

print('HOW\'S THE WEATHER?')
cel = int(input('What\'s the temperature in Celsius? '))
print(c_to_f(cel))
