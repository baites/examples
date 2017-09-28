#! /usr/bin/env python
import copy

def CreateClosure(value):
    """Create closure forcing capture by copy or value."""
    context = copy.deepcopy(value)
    def Method():
        return copy.deepcopy(context)
    return Method

# Creating closure with a unmutable object (a string)
# This behaves as if context is captured by copy or value
unmutable = 'A'
closureA = CreateClosure(unmutable)
print('context in closureA: ', closureA())

# Creating closure with a mutable object (a list)
# This also behaves as if context is captured by copy or value
mutable = ['B']
closureB = CreateClosure(mutable)
print('context in closureB: ', closureB())

# It is NOT possible to change of the value of the context
mutable[0] = 'C'
print('context in closureB: ', closureB())

# It is not event possible to get a refence to context
mutable = closureB()
mutable[0] = 'C'
print('context in closureB: ', closureB())
