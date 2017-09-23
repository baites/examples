#! /usr/bin/env python

import types
import sys

def readonly(value):
    return property(lambda self: value)

class A(object):
    def __init__(self, value):
        A.constant = readonly(value)

a = A('constant value')
print(a.constant)

a.constant = 'new value'
