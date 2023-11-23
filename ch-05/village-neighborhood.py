#!/usr/bin/python3
# CCC18S1 - Village Neighborhood
villageList = []
roadLen = int(input())
x = 0 while x < roadLen:
    villageList.append(int(input()))
    x += 1
villageList.sort()
sizeList = []
for i in range(1, roadLen - 2):
    currentVillage = villageList[i]
    prevVillage = villageList[i-1]
    nextVillage = villageList[i+1]
    sizeNeighborhood = ((currentVillage - prevVillage) + (nextVillage - currentVillage)) / 2
    sizeList.append(sizeNeighborhood)
print(min(sizeList))
