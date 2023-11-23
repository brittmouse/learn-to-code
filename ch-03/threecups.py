#!/usr/bin/python3
# COCI06C5P1 - Trik
def ballswitch(user_in):
  ball_location = 1
  for i in range(len(user_in)):
    swap = user_in[i].upper()
    if swap == 'A' and ball_location == 1:
      ball_location = 2
    elif swap == 'A' and ball_location == 2:
      ball_location = 1
    elif swap == 'B' and ball_location == 2:
      ball_location = 3
    elif swap == 'B' and ball_location == 3:
      ball_location = 2
    elif swap == 'C' and ball_location == 1:
      ball_location = 3
    elif swap == 'C' and ball_location == 3:
      ball_location = 1
  return ball_location

print(ballswitch('ABBCAB'))
print(ballswitch('Ab'))
print(ballswitch('CBABCACCC'))
