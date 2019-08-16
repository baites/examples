#! /usr/bin/env python

from copy import deepcopy

def FreezeProperty(value):
    """Create a closure protected constant copy of value."""
    cache = deepcopy(value)
    return property(
        lambda self: deepcopy(cache)
    )

def FrozenSpace(**args):
    args = {k: FreezeProperty(v) for k, v in args.items()}
    args['__slots__'] = ()
    cls = type('FrozenSpace', (), args)
    return cls()

fs = FrozenSpace(
    x = 2,
    y = {'name': 'y', 'value': 2}
)

print(fs.x) # print "2"
fs.x = 3 # raise "AttributeError: 'ConstantSpace' object attribute 'x' is read-only"
print(fs.y) # print "{'name': 'y', 'value': 2}"
fs.y['name'] = 'yprime' # try to change mutable object
print(fs.y) # print "{'name': 'y', 'value': 2}"
fs.y = {} # raise "AttributeError: 'ConstantSpace' object attribute 'x' is read-only"
fs.z = 3 # raise "AttributeError: 'ConstantSpace' object has no attribute 'z'"
