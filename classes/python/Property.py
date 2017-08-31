#! /usr/bin/env python

class ObjectType:
    def __init__(self, value):
        self._propname = value

    @property
    def propname(self):
        """Propname docstring."""
        print('getting propname')
        return self._propname

    @propname.setter
    def propname(self, value):
        print('setting propname')
        self._propname = value

    @propname.deleter
    def propname(self):
        print('deleting propname')
        del self._propname


o = ObjectType('hola')
print(o.propname)

o.propname = 'chau'
print(o.propname)

del o.propname
print('Has attribute propname?', hasattr(o, 'propname'))
