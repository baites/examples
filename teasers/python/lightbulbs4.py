#! /usr/bin/env python

import math

NUMBER_OF_BULBS = 100

def isPerfectSQRT2(n):
    x = n // 2
    y = set([x])
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in y: return 0
        y.add(x)
    return n

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
    return isPerfectSQRT2(x)


bulbs = filter(lambda x: x != 0,
    map(isPerfectSQRT, range(1, NUMBER_OF_BULBS+1))
)

for bulb in bulbs:
    print(bulb)
