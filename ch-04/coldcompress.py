#!usr/bin/python3
# CCC19J3 - Cold Compress

n = int(input())
inputList = []
for i in range(n):
    inputList.append(input())

for item in inputList:
    itemLen = len(item) - 1
    i = 0
    charCount = 1
    while i < itemLen:
        char = item[i]
        if char == item[i+1] and i != (itemLen - 1):
            charCount += 1
        else:
            print(f'{char} {charCount} ', end='')
            charCount = 1 
        i += 1
    print()
