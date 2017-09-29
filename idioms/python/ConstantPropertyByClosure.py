#! /usr/bin/env python

import copy
import pprint
import types
import sys

def ConstantProperty(value):
    """Create a closure protected constant copy of value."""
    cache = copy.deepcopy(value)
    return property(
        lambda self: copy.deepcopy(cache)
    )

class A(object):
    def __init__(self, value):
        """Class constructor."""
        A.constant = ConstantProperty(value)

    def set_constant(self, value):
        """A non property setter for constant."""
        self.constant = value

mutable = {
    'A': [1, 2],
    'B': 'cannot be change'
}

# Initialize object with a mutable object
a = A(mutable)
# Print object
pprint.pprint(a.constant)

# Try to change constant property
# by updating object referred by "value"
mutable['B'] = 'can be changed'
pprint.pprint(a.constant)

# Try to change constant property
# by updating object return by a.constant
a.constant['B'] = 'can be changed'
pprint.pprint(a.constant)

# Try to modify constant property
try:
    a.constant = { 'A': 'new' }
    pprint.pprint(a.constant)
except Exception as error:
    print(error)

# Try to modify constant property
# from a class member function
try:
    a.set_constant({ 'A': 'new' })
    pprint.pprint(a.constant)
except Exception as error:
    print(error)
