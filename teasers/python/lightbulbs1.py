#!/usr/bin/env python

NUMBER_OF_BULBS = 100

bulbs = [0 for x in range(0, NUMBER_OF_BULBS)]

for i in range(len(bulbs)):
    for j in range(i, len(bulbs), i + 1):
        bulbs[j] = 1 - bulbs[j]

for number, bulb in enumerate(bulbs):
    if bulb == 1:
        print(number + 1)
