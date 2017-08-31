#! /usr/bin/env python

import types
import sys

def readonly(value):
    return property(lambda self: value)

class ReadOnly(object):
    def __init__(self):
        ReadOnly.constant = readonly('victor')

sys.modules[__name__] = ReadOnly()
print(constant)
