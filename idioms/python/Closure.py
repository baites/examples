#! /usr/bin/env python
import copy

def CreateMethodWithContext(value):
    context = copy.copy(value)
    def Method():
        return context
    return Method

orig_method = CreateMethodWithContext('original value')
new_method = CreateMethodWithContext('new value')

print('context in orginal method: ', orig_method())
print('context in new method: ', new_method())
