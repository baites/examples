#! /usr/bin/env python

import math

NUMBER_OF_BULBS = 100

def isPerfectSQRT1(x):
    root = math.sqrt(x)
    return x if x == int(root + 0.5)**2 else 0

def isPerfectSQRT(x):

    # Trivial check
    if x == 1:
        return 1

    # Number ends in 2, 3, 7, 8
    ld = x % 10
    if ld in (2, 3, 7, 8):
        return 0

    # Digital root is not 1, 4, 7, 9
    dr = x % 9
    if x == 0:
        dr = 0
    elif x != 0 and dr == 0:
        dr = 9
    if dr not in (1, 4, 7, 9):
        return 0

    # Default rule
    return isPerfectSQRT1(x)

bulbs = filter(lambda x: x != 0,
    map(isPerfectSQRT, range(1, NUMBER_OF_BULBS+1))
)

for bulb in bulbs:
    print(bulb)
