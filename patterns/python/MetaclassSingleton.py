#! /usr/bin/env python

class Singleton(type):
    _instance = None
    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class A(metaclass=Singleton):
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
    print(repr(x))
    print(repr(y))
    print(repr(z))
    print('x == y?', x is y)
    print('y == z?', y is z)
    print('z == x?', z is x)
    print()

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
#order3()
order3()
order2()
order1()
