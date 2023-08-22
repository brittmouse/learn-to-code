#!/usr/bin/python3
# ECOO13R1P1
total = int(input())
take, serve = 0, 0
lineList = []
while True:
    ticket = input().upper()
    if ticket == 'TAKE':
        take += 1
    elif ticket == 'SERVE':
        serve += 1
    elif ticket == 'CLOSE':
        total += take
        lineList.append([take, take-serve, total])
        take, serve = 0, 0
    elif ticket == 'EOF':
        break

for line in lineList:
    print(line[0], line[1], line[2])
