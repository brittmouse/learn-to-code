#!/usr/bin/python3
# COCI12C5P1 - Ljestvica
# Given a string as input, determine
# whether the tones within the string indicate
# either a key of C-major or A-minor.
aMinor, cMajor = 0, 0
sequence = input()
sequenceList = sequence.split('|')
for measure in sequenceList:
    if measure[0] in ['A', 'D', 'E']:
        aMinor += 1
    elif measure[0] in ['C', 'F', 'G']:
        cMajor += 1
if aMinor > cMajor or (aMinor == cMajor and sequenceList[-1][0] in ['A', 'D', 'E']):
    print('A-mol')
else:
    print('C-dur')
