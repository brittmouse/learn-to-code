#!/home/brittmouse/miniconda3/bin/python
print('LOCAL AMATEUR BASKETBALL LEAGUE: APPLES VS BANANAS')

apple_3pointers = int(input('3-pointers for the Apples: ')) * 3
apple_2pointers = int(input('2-pointers for the Apples: ')) * 2
apple_freethrows = int(input('Free-throws for the Apples: '))

banana_3pointers = int(input('3-pointers for the Bananas: ')) * 3
banana_2pointers = int(input('2-pointers for the Bananas: ')) * 2
banana_freethrows = int(input('Free-throws for the Bananas: '))

apple_score = apple_3pointers + apple_2pointers + apple_freethrows
banana_score = banana_3pointers + banana_2pointers + banana_freethrows

print(f'Apples: {apple_score}')
print(f'Bananas: {banana_score}')

if (apple_score > banana_score): print('A')
elif (banana_score > apple_score): print('B')
else: print('T')
