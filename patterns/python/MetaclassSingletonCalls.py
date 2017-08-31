#! /usr/bin/env python

class Singleton(type):
    _instance = None
    def __call__(cls, *args, **kwargs):
        print('Singleton.__call__')
        if not cls._instance:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class A(metaclass=Singleton):
    def __init__(self, val):
        print('A.__init__')
        self.val = val
    def __str__(self):
        print('A.__str__')
        return 'A:{}'.format(self.val)

class B(A):
    def __init__(self, val):
        print('B.__init__')
        self.val = val
    def __str__(self):
        print('B.__str__')
        return 'B:{}'.format(self.val)

def order1():
    x = A('x')
    y = A('y')
    z = B('z')

def order2():
    y = A('y')
    x = A('x')
    z = B('z')

def order3():
    x = B('x')
    y = A('y')
    z = A('z')

#order1()
order3()
