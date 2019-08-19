#! /usr/bin/env python

def singleton(*args, **kwargs):
    def wrapper(cls):
        return cls(*args, **kwargs)
    return wrapper

@singleton(value = 'x')
class A:
    def __init__(self, value):
        self.value = value

# A is not a class but an instance!
print('A.value = {}'.format(A.value))
# Inspect
print(repr(A))

# Confusion, trying to inherent from an Object
class B(A):
    def __init__(self):
        super.__init__('y')
