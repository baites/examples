#! /usr/bin/env python

class Borg(object):
    _state = {}
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.__dict__ = cls._state
        return instance

class A(Borg):
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return 'A:{}'.format(self.val)

class B(A):
    def __init__(self, val):
        self.val = val
    def __str__(self):
        return 'B:{}'.format(self.val)

def show(x, y, z):
    print(x, y, z)
    print('x == y?', x is y)
    print('y == z?', y is z)
    print('z == x?', z is x)


def order1():
    x = A('x')
    y = A('y')
    z = B('z')
    show(x, y, z)

def order2():
    y = A('y')
    x = A('x')
    z = B('z')
    show(x, y, z)

def order3():
    x = B('x')
    y = A('y')
    z = A('z')
    show(x, y, z)

#order1()
#order2()
order3()
