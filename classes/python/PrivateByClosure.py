#! /usr/bin/env python

class A:
    def __init__(self):
        counter = 0
        def tick():
            nonlocal counter
            counter += 1
        self.tick = tick
        def count():
            return counter
        self.counter = count

a = A()
a.tick()
a.tick()
a.tick()
print(a.counter())
