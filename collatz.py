#!usr/bin/python3
def collatz(num):
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        print(num)
print("Enter number:")
num = int(input())
collatz(num)
