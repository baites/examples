#! /usr/bin/env python

import math

NUMBER_OF_BULBS = 100

def isPerfectSQRT(x):
    root = math.sqrt(x)
    return x if x == int(root + 0.5)**2 else 0

bulbs = filter(lambda x: x != 0,
    map(isPerfectSQRT, range(1, NUMBER_OF_BULBS+1))
)

for bulb in bulbs:
    print(bulb)
