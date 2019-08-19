#! /usr/bin/env python

def SpaceConstants():
    def setattr(self, name, value):
        if hasattr(self, name):
            raise AttributeError(
                "Cannot reassign members"
            )
        self.__dict__[name] = value
    cls = type('SpaceConstants', (), {
        '__setattr__': setattr
    })
    return cls()

sc = SpaceConstants()

print(sc.x)
sc.x = 2 # bind attribute x
print(sc.x) # print "2"
sc.x = 3 # raise "AttributeError: Cannot reassign members"
sc.y = {'name': 'y', 'value': 2} # bind attribute y
print(sc.y) # print "{'name': 'y', 'value': 2}"
sc.y['name'] = 'yprime' # mutable object can be changed
print(sc.y) # print "{'name': 'yprime', 'value': 2}"
sc.y = {} # raise "AttributeError: Cannot reassign members"
