#!/usr/bin/python3
# CCC00S1 - Slot Machines
# import time (used to help debug program)
quarters = int(input())
slot1_runs = int(input())
slot2_runs = int(input())
slot3_runs = int(input())
plays = 0
next_play = 'first'
while quarters > 0:
    # print(plays, quarters, next_play, slot1_runs, slot2_runs, slot3_runs)
    quarters -= 1
    if next_play == 'first':
        slot1_runs += 1
        next_play = 'second'
        if slot1_runs == 35:
            quarters += 30
            slot1_runs = 0
    elif next_play == 'second':
        slot2_runs += 1
        next_play = 'third'
        if slot2_runs == 100:
            quarters += 60
            slot2_runs = 0
    elif next_play == 'third':
        slot3_runs += 1
        next_play = 'first'
        if slot3_runs == 10:
            quarters += 9
            slot3_runs = 0
    plays += 1
    # time.sleep(0.5)
print(f'Martha plays {plays} times before going broke.')
