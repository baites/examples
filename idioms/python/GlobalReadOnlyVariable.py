#! /usr/bin/env python

import sys

def readonly(value):
    return property(lambda self: value)

module = sys.modules[__name__]
module = staticmethod('x')

print(module.x)
