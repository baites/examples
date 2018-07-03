#! /usr/bin/env python

class A(object):
    def __new__(cls, *args, **kwargs):
        print('enter {}.__new__'.format(cls.__name__))
        instance = super().__new__(cls, *args, **kwargs)
        print('create {}'.format(instance))
        return instance

    def __init__(self, *args, **kwargs):
        print('enter __init__')
        print('initialize {}'.format(self))

    def __del__(self):
        print('enter __del__')
        print('delete {}'.format(self))        

a = A()
del a
