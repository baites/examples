#! /usr/bin/env python

import copy
import pprint
import types
import sys

def FreezeMutable(value):
    """Create a closure protected constant copy of value."""
    cache = copy.deepcopy(value)
    return lambda: copy.deepcopy(cache)

# Initialize mutable object
mutable = {
    'A': [1, 2],
    'B': 'cannot be change'
}

# Create a frozen version of mutable
frozen = FreezeMutable(mutable)
# Print object
pprint.pprint(frozen())

# Try to change constant property
# by updating object referred by mutable
mutable['B'] = 'can be changed'
pprint.pprint(frozen())

# Try to change constant property
# by updating object return by a.constant
frozen()['B'] = 'can be changed'
pprint.pprint(frozen())
