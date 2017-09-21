#! /usr/bin/env python

import matplotlib.pyplot as plt

# Recursive algo

xr = (
        5,    20,     30,     35,     36,
       38,    40,     42,     44,     46,      48
)

## Using js
yrj = (
    0.152, 0.155,  0.192,  0.583,  0.844,
    1.966, 4.899, 12.548, 32.607, 85.352, 222.701
)

## Using C++
yrc = (
    0.004, 0.004,  0.034,  0.191,  0.279,
    0.653, 1.627,  4.177, 10.871, 28.356, 74.206
)

plt.semilogy(xr, yrj, label='javascript')
plt.semilogy(xr, yrc, label='C++')
legend = plt.legend(loc='upper left')
plt.title('Performance of Fibonacci recursive algorithm')
plt.xlabel('Fibonacci number index')
plt.ylabel('Execution time [s]')
plt.grid(True)
plt.show()
