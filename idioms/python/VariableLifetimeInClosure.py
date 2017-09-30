#! /usr/bin/env python
import copy

class LifetimeProbe(object):
    """Implement lifetime probes"""
    def __init__(self, pid=None):
        if not pid:
            print('...probe contructor {}'.format(self))
        else:
            print('...probe copy {} from {}'.format(self, pid))

    def __copy__(self):
        new = LifetimeProbe(self)
        return new

    def __deepcopy__(self, memo):
        new = LifetimeProbe(self)
        return new

    def __del__(self):
        print('...probe destruction {}'.format(self))

def main():
    """First scope where closure lives"""
    print('entering closure scope')
    def CreateClosure(value):
        """Create closure forcing capture by copy or value."""
        context = copy.deepcopy(value)
        def Method():
            return copy.deepcopy(context)
        return Method
    # Create lifetime probe
    print('create lifetime probe')
    probe = LifetimeProbe()
    # Create closure
    print('create closure')
    closure = CreateClosure(probe)
    # Print closure value
    print('context in closure: ', closure())
    print('exiting closure scope')
    return closure

print('Call closure scope')
main()
print('Return from closure scope')

print()

print('Call scope where closure is defined')
closure = main()
print('Return reference to closure')
