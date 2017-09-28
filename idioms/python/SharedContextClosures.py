#! /usr/bin/env python
import copy

def CreateClosure(value):
    """Create two closures with share context."""
    context = copy.deepcopy(value)
    def GetContext():
        return copy.deepcopy(context)
    def SetContext(value):
        nonlocal context
        context = copy.deepcopy(value)
    return GetContext, SetContext

# Creating closures with protective share context
# Object mutability is irrelevant because context is
# protected by the closure (capture by copy and unreachable)
get_context, set_context = CreateClosure(['A'])

# Print original context value
print('get context value: ', get_context())

# Set new context value
set_context(['B'])
print('set and get context value: ', get_context())

# It is not possible to get a refence to context
context = get_context()
context[0] = 'C'
print('get context value: ', get_context())
