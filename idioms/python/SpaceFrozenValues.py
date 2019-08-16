#! /usr/bin/env python

from copy import deepcopy

def SpaceFrozenValues():
    cache = {}
    def setattr(self, name, value):
        nonlocal cache
        if name in cache:
            raise AttributeError(
                "Cannot reassign members"
            )
        cache[name] = deepcopy(value)
    def getattr(self, name):
        nonlocal cache
        if name not in cache:
            raise AttributeError(
                "Object has no attribute '{}'".format(name)
            )
        return deepcopy(cache[name])
    cls = type('SpaceFrozenValues', (),{
        '__getattr__': getattr,
        '__setattr__': setattr
    })
    return cls()

fv = SpaceFrozenValues()
print(fv.x) # AttributeError: Object has no attribute 'x'
fv.x = 2 # bind attribute x
print(fv.x) # print "2"
fv.x = 3 # raise "AttributeError: Cannot reassign members"
fv.y = {'name': 'y', 'value': 2} # bind attribute y
print(fv.y) # print "{'name': 'y', 'value': 2}"
fv.y['name'] = 'yprime' # mutable object can be changed
print(fv.y) # print "{'name': 'yprime', 'value': 2}"
fv.y = {} # raise "AttributeError: Cannot reassign members"
