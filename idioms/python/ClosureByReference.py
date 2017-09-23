#! /usr/bin/env python
import copy

def CreateMethods():
    context = 'original value'
    def GetContext():
        return context
    def SetContext(value):
        nonlocal context
        context = value
    return GetContext, SetContext

get_context, set_context = CreateMethods()

print('get context original value: ', get_context())
print('set context value: "new value"')
set_context('new value')
print('get context value: ', get_context())
