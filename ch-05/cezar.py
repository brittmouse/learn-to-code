#!/usr/bin/python3
# COCI17C1P1 - Cezar

hand = []
deck = [
    [2, 4],
    [3, 4],
    [4, 4],
    [5, 4],
    [6, 4],
    [7, 4],
    [8, 4],
    [9, 4],
    [10, 16],
    [11, 4],
]

cardsInHand: int = int(input())
for i in range(cardsInHand):
    card: int = int(input())
    while hand.count(card) > 4:
        print("You have too many of those cards!")
        card: int = int(input())
        if hand.count(card) <= 4:
            break
    hand.append(card)

for i in range(len(deck)):
    cardValue: int = deck[i][0]
    cardCount: int = deck[i][1]
    if hand.__contains__(cardValue):
        cardCount -= hand.count(cardValue)

difference: int = 21 - sum(hand)
sumOfGreaterValues: int = 0
sumOfLesserValues: int = 0
for i in range(len(deck)):
    cardValue: int = deck[i][0]
    cardCount: int = deck[i][1]
    if cardValue <= difference:
        sumOfLesserValues += cardCount
    else:
        sumOfGreaterValues += cardCount

if sumOfGreaterValues >= sumOfLesserValues:
    print("DOSTA")
else:
    print("VUCI")
