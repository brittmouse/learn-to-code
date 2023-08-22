#!/usr/bin/python3
# COCI08C3P2 - Kemija
# Given a coded string where each vowel is followed by a p and the vowel again, decode the string.

codedMessage = input().lower()
vowels = ['a', 'e', 'i', 'o', 'u']
decodedMessage = ''
index = 0
while index < len(codedMessage):
    decodedMessage += codedMessage[index]
    if codedMessage[index] in vowels: index += 3
    else: index += 1
print(decodedMessage)
