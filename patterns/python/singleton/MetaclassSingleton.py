#! /usr/bin/env python

import sys

class MetaclassSingleton(type):
    _instance = None
    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class A(metaclass=MetaclassSingleton):
    def __init__(self, value):
        self.value = value

class B(A):
    def __init__(self, value):
        self.value = value


def init_A_before_B():
    print('Initialize A before B')

    # Initialize instance x using parent class A
    x = A('x')
    print(repr(A._instance))
    print(repr(x))

    # Child class _instance inherent
    # value after x initialization
    print(repr(B._instance))

    # Initialize y using child class B affects value of x
    # because _instance has a value inherent from A.
    y = B('y')
    print(repr(y))
    print('x.value = {}'.format(x.value))
    print('y.value = {}'.format(y.value))


def init_B_before_A():
    print('Initialize B before A')

    # Initialize instance y using parent class B
    y = B('y')
    print(repr(B._instance))
    print(repr(y))

    # Parent class _instance is still None!
    print(repr(A._instance))

    # Initialize x using parent class A does not affect value of y
    # because _instance has None value.
    x = A('x')
    print(repr(x))

    print('x.value = {}'.format(x.value))
    print('y.value = {}'.format(y.value))


def init_A_twice():
    print('Initialize A twice')

    # Initialize instance x using parent class A
    x = A('x')
    # Initialize instance y using parent class A
    y = A('y')
    print('x.value = {}'.format(x.value))
    print('y.value = {}'.format(y.value))


if len(sys.argv) == 2 and sys.argv[1] == 'A':
    init_A_before_B()
elif len(sys.argv) == 2 and sys.argv[1] == 'B':
    init_B_before_A()
elif len(sys.argv) == 2 and sys.argv[1] == 'I':
    init_A_twice()
else:
    print('Use {} A for init A before B'.format(sys.argv[0]))
    print('Use {} B for init B before A'.format(sys.argv[0]))
    print('Use {} I for init A twice'.format(sys.argv[0]))
