#! /usr/bin/env python2

def bitToInt(array):

    result = 0
    length = len(a)

    for i in range(length):
        if a[len(a)-i-1] == '1':
            result += 2**i

    return result


def countBits(number):

    counter = 0

    while number > 0:
        if (number & 1) == 1:
            counter += 1
        number = number >> 1

    return counter


a = '100001110'

print a
print countBits(bitToInt(a))

