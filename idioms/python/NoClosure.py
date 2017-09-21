#! /usr/bin/env python

context = 'original value'
def Method():
    return context;

def CreateMethodWithContext(value):
    global context;
    context = value
    return Method

new_method = CreateMethodWithContext('new value')

print('context in orginal method: ', Method())
print('context in new method: ', new_method())
