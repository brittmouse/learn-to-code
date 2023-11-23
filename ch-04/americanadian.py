#!/usr/bin/python3
# CCC02J2 - AmeriCanadian

wordList = []
vowels = ['a','e', 'i', 'o', 'u', 'y']
while True:
    word = input().lower()
    if word != 'quit!':
        wordList.append(word)
    else:
        break

for word in wordList:
    if len(word) > 4 and word[-2:] == 'or' and word[-3] not in vowels:
        word = word[:-2] + 'our'
    print(word)
