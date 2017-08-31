#! /usr/bin/env python

import copy

def readonly(value):
    return property(lambda self: value)

class A:
    def __init__(self, value):
        _value = copy.deepcopy(value)
        A.readonly = readonly(_value)

class B:
    def __init__(self, value):
        self._readonly = copy.deepcopy(value)
    @property
    def readonly(self):
        return self._readonly

a = A(42)
print(a.readonly)
A.readonly2 = readonly(1)
print(a.readonly2)

b = B(42)
print(b.readonly)
b._readonly = 43
print(b.readonly)

a.readonly = 43
print(a.readonly)
