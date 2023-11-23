#!/usr/bin/python3
# CCC18J2 - Occupied Spaces
def parking(n, park_1, park_2):
  spaces_taken = 0
  for index in range(0, n):
    if park_1[index] == 'C' and park_2[index] == 'C':
      spaces_taken += 1
  return spaces_taken

print(parking(3, 'CC.', '.C.')) # returns 1
print(parking(7, '...CCC.', 'C.CC..C')) # returns 1
print(parking(8, 'CCCCC.CC', 'CC.CC.CC')) # returns 6
