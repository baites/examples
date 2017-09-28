#! /usr/bin/env python
import copy

def CreateClosures(value):
    """Create two closures with share context."""
    context = copy.deepcopy(value)
    def GetContext():
        return copy.deepcopy(context)
    def SetContext(value):
        context = copy.deepcopy(value)
    return GetContext, SetContext

# Creating closures with protective share context
# Object mutability is irrelevant because context is
# protected by the closure (capture by copy and unreachable)
get_context, set_context = CreateClosures('A')

# Print original context value
print('get context value: ', get_context())

# Set new context value
set_context('B')
print('set and get context value: ', get_context())
