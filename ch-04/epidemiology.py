#!/usr/bin/python3
# CCC20J2 - Epidemiology
pop = int(input())
infected = int(input())
vectors = int(input())
infectedSum = infected
day = 0
while infectedSum <= pop:
    day += 1
    infected *= vectors
    infectedSum += infected
print(day)
