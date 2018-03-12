#! /usr/bin/env python

import sys

class Borg(object):
    _state = {}
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.__dict__ = cls._state
        return instance

class A(Borg):
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
    print(repr(x))
    print('_state value in A: ', A._state)
    # Child class _state comes from A
    print('_state value in B: ', B._state)

    # Initiale y of child class B affects value of A
    # Because share same _state
    y = B('y')
    print(repr(y))
    print('_state value in A: ', A._state)
    print('_state value in B: ', B._state)


    print('x.value = {}'.format(x.value))
    print('y.value = {}'.format(y.value))

def init_B_before_A():
    print('Initialize B before A')

    # Initialize instance y of child class B
    y = B('y')
    print(repr(y))
    print('_state value in A: ', hex(id(A._state)))
    # Child class _state comes from A
    print('_state value in B: ', hex(id(B._state)))

    # Initiale y of child class B affects value of A
    # Because share same _state
    x = B('x')
    print(repr(x))
    print('_state value in A: ', A._state)
    print('_state value in B: ', B._state)

    print('x.value = {}'.format(x.value))
    print('y.value = {}'.format(y.value))

if len(sys.argv) == 2 and sys.argv[1] == 'A':
    init_A_before_B()
elif len(sys.argv) == 2 and sys.argv[1] == 'B':
    init_B_before_A()
else:
    print('Use {} A for init A before B or'.format(sys.argv[0]))
    print('Use {} B for init B before A or'.format(sys.argv[0]))
