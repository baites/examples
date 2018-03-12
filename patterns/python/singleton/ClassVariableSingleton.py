#! /usr/bin/env python

import sys

class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

class A(Singleton):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return 'A:{}'.format(self.value)

class B(A):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return 'B:{}'.format(self.value)

def init_A_before_B():
    print('Initialize A before B')

    # Initialize instance x of parent class A
    x = A('x')
    print(A._instance)
    print(repr(A._instance))

    # Child class _instance comes from A
    print(B._instance)
    print(repr(B._instance))

    # Initiale y of child class B affects value of A
    # Because _instance already points to x
    y = B('y')
    print('x.value = {}'.format(x.value))
    print('y.value = {}'.format(y.value))

def init_B_before_A():
    print('Initialize B before A')

    # Initiale y of child class B
    y = B('y')
    print(B._instance)
    print(repr(B._instance))

    # Child class _instance cannot derive from B!
    print(A._instance)
    print(repr(A._instance))

    # Initiale x of parent class A does not affect value of B
    # Because _instance is not poiting to any object
    x = A('x')
    print(A._instance)
    print(repr(A._instance))

    print('x.value = {}'.format(x.value))
    print('y.value = {}'.format(y.value))

if len(sys.argv) == 2 and sys.argv[1] == 'A':
    init_A_before_B()
elif len(sys.argv) == 2 and sys.argv[1] == 'B':
    init_B_before_A()
else:
    print('Use {} A for init A before B or'.format(sys.argv[0]))
    print('Use {} B for init B before A or'.format(sys.argv[0]))
