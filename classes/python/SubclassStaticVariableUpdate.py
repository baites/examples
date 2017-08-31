#! /usr/bin/env python

class A(object):

    _variable = 'A implementation'

    @staticmethod
    def set_variable(value):
        A._variable = value

    @staticmethod
    def static_call():
        return A._variable

    @classmethod
    def class_call(cls):
        return cls._variable

    def object_call(self):
        return self._variable


class B(A):

    _variable = 'B Implementation'


class C(A):

    _variable = 'C Implementation'

    def __init__(self):
        A._variable = C._variable


class D(A):

    _variable = 'D Implementation'

    def __init__(self):
        super().set_variable(D._variable)


a = A()

print(A.static_call())
print(A.class_call())
print(a.object_call())
print(a.static_call())
print(a.class_call())
print(a.object_call())
print()

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
print()

d = D()

print(D.static_call())
print(D.class_call())
print(d.object_call())
print(d.static_call())
print(d.class_call())
print(d.object_call())
