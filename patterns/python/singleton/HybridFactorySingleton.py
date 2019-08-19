#! /usr/bin/env python

def singleton(*args, **kwargs):
    def wrapper(baseclass):
        instantiated = False
        def new(cls, *a, **k):
            nonlocal instantiated
            if instantiated:
                raise TypeError(
                    'a singleton instance cannot be reinstantiated'
                )
            instantiated = True
            return super(baseclass, cls).__new__(cls, *a, **k)
        def init(self):
            baseclass.__init__(self, *args, **kwargs)
        _ = type(
            '{}_singleton'.format(baseclass.__name__),
            (baseclass,), {
                '__init__': init,
                '__new__': new
            }
        )
        return _()
    return wrapper

@singleton(value = 'x')
class A:
    def __init__(self, value):
        self.value = value

# A is not a class but an instance!
print('A.value = {}'.format(A.value))
# Inspect
print(repr(A))

# Confusion, trying to inherent from an Object
class B(A):
    def __init__(self):
        super.__init__('y')
