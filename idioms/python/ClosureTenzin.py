#! /usr/bin/env python

def sum(x):
    return lambda y: x+y

print(sum(10)(1))
