#! /usr/bin/env python

def CreateClosure(context):
    """Create closure with default capture."""
    def method():
        return context
    return method

# Creating closure with a unmutable object (a string)
# This behaves as if context is captured by copy or value
unmutable = 'A'
closureA = CreateClosure(unmutable)
print('context in closureA: ', closureA())

# Creating closure with a mutable object (a list)
# This behaves as if context is captured by reference
mutable = ['B']
closureB = CreateClosure(mutable)
print('context in closureB: ', closureB())

# It is possible to change of the value of the context
mutable[0] = 'C'
print('context in closureB: ', closureB())
