#! /usr/bin/env python

class Core:
    def __init__(self):
        self._variable = None

    def get(self):
        return self._variable

    def put(self, value):
        self._variable = value
        return value


class Decorator1:
    def __init__(self, instance):
        self._instance = instance

    def get(self):
        print('get method 1')
        return self._instance.get()

    def put(self, value):
        print('put method 1')
        return self._instance.put(value)


class Decorator2:
    def __init__(self, instance):
        self._instance = instance

    def get(self):
        print('get method 2')
        return self._instance.get()

    def put(self, value):
        print('put method 2')
        return self._instance.put(value)


c = Core()
c.put('hola')
print(c.get())

d1 = Decorator1(c)
d1.put('chau')
print(d1.get())

d2 = Decorator2(c)
d2.put('ultimo')
print(d2.get())
