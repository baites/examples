#! /usr/bin/env python

import copy
import sys

class MetaBorg(type):
    _state = {"__skip_init__": False}
    def __call__(cls, *args, **kwargs):
        instance = object().__new__(cls, *args, **kwargs)
        instance.__dict__ = cls._state
        if not cls._state['__skip_init__']:
            instance.__init__(*args, **kwargs)
            cls._state['__skip_init__'] = True
        return instance

class A(metaclass=MetaBorg):
    def __init__(self, value):
        self.value = value

class B(A):
    def __init__(self, value):
        self.value = value


def init_A_before_B():
    print('Initialize A before B')

    # Initialize instance x of parent class A
    x = A('x')
    print(repr(x))
    print('_state in A: object at', hex(id(A._state)))
    print('_state in B: object at', hex(id(B._state)))

    # Initiale y of child class B affects value of A
    # because share same _state
    y = B('y')
    print(repr(y))
    print('_state in A: object at', hex(id(A._state)))
    print('_state in B: object at', hex(id(B._state)))

    print('x.value = {}'.format(x.value))
    print('y.value = {}'.format(y.value))


def init_B_before_A():
    print('Initialize B before A')

    # Initialize instance y of child class B
    y = B('y')
    print(repr(y))
    print('_state in A: object at', hex(id(A._state)))
    print('_state in B: object at', hex(id(B._state)))

    # Initialize x using parent class A does not affect value of y
    # because _instance has None value.
    x = A('x')
    print(repr(x))
    print('_state in A: object at', hex(id(A._state)))
    print('_state in B: object at', hex(id(B._state)))

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
