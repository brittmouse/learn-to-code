#!/usr/bin/python3
from math import pi as pi
print('CONE VOLUME CALCULATION PROGRAM')
r = int(input('Enter the radius of the base (between 1 and 100): '))
h = int(input('Enter the height of the cone (between 1 and 100): '))
volume = (pi * h * r**2) / 3
print(volume)
