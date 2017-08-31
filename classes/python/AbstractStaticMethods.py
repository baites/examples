#! /usr/bin/env python

import abc

class A(abc.ABC):

    @staticmethod
    @abc.abstractmethod
    def _exe():
        return 'A implementation'

    @staticmethod
    def static_call():
        return A._exe()

    @classmethod
    def class_call(cls):
        return cls._exe()

    def object_call(self):
        return self._exe()


class B(A):

    @staticmethod
    def _exe():
        return 'B implementation'


class C(A):

    @staticmethod
    def _exe():
        return 'C implementation'

    @staticmethod
    def __init__():
        A._exe = C._exe

b = B()

print(B.static_call())
print(B.class_call())
print(b.object_call())
print(b.static_call())
print(b.class_call())
print(b.object_call())
print()

c = C()

print(C.static_call())
print(C.class_call())
print(c.object_call())
print(c.static_call())
print(c.class_call())
print(c.object_call())
