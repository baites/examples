#! /usr/bin/env python

def ConstantSpace(**args):
    args['__slots__'] = ()
    cls = type('ConstantSpace', (), args)
    return cls()

cs = ConstantSpace(
    x = 2,
    y = {'name': 'y', 'value': 2}
)

print(cs.x) # print "2"
cs.x = 3 # raise "AttributeError: 'ConstantSpace' object attribute 'x' is read-only"
print(cs.y) # print "{'name': 'y', 'value': 2}"
cs.y['name'] = 'yprime' # mutable object can be changed
print(cs.y) # print "{'name': 'yprime', 'value': 2}"
cs.y = {} # raise "AttributeError: 'ConstantSpace' object attribute 'x' is read-only"
cs.z = 3 # raise "AttributeError: 'ConstantSpace' object has no attribute 'z'"
