#! /usr/bin/env python

import random
import matplotlib.pyplot as plt
from PisanoLookup import lookup

# Sampling probability
prob = 0.05

xm = lookup.index(max(lookup))

## Sampling modulo index
x = []
for i in range(100001):
    if i == xm:
        x.append(i)
    elif random.random() <= prob:
        x.append(i)

## Sampling Pisano value vs sampled index
y = []
for i in x:
    y.append(lookup[i])

plt.scatter(x, y, s=1)
plt.title('Pisano periods vs modulo')
plt.xlabel('Modulo index')
plt.ylabel('Pisano period')
plt.grid(True)
plt.savefig("PisanoPeriods.svg")
