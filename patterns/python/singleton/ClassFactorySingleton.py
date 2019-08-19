#! /usr/bin/env python

def staticvars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate

@staticvars(_instance=None)
def Singleton(*args):
    if Singleton._instance:
        return Singleton._instance
    class _:
        def __init__(self):
            self.value = args[0]
    Singleton._instance = _()
    return Singleton._instance

# Initialize instance x using parent class A
x = Singleton('x')
print('x.value = {}'.format(x.value))
# Initialize instance y using parent class A
y = Singleton()
print('y.value = {}'.format(y.value))
# Updating
x.value = 'y'
print('x.value = {}'.format(x.value))
print('y.value = {}'.format(y.value))

# Inspect
print(repr(x))
print(repr(y))
