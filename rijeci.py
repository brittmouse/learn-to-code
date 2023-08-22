#!/usr/bin/python3
# COCI13C3P1 - Rijeci
# After trying to replace characters within the string, I realized that
# the string followed a Fibonacci sequence, where the number of A's and B's
# corresponded to the Fibonacci value at k-1 and k.

k = int(input())
fib = [0, 1]
for i in range(2, k+1):
    fib.append(fib[i-1] + fib[i-2])
print(fib[k-1], fib[k]) # Using fib[-2], fib[-1] would also work as both return the last two array elements

# Here is an alternate solution more in line with the premise of the problem.

machineStr = ['A', 'B']
count_a, count_b = 0, 0
for i in range(2, k+1):
    machineStr.append(machineStr[i-1] + machineStr[i-2])
for char in machineStr[k]:
    if char == 'A': count_a += 1
    elif char == 'B': count_b +=1
print(count_a, count_b)
