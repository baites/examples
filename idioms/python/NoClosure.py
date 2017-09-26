#! /usr/bin/env python

# Defining context and method in global namespace
context = 'A'
def Method():
    return context

def CreateMethodReference(value):
    """Return a reference to Method."""
    global context
    context = value
    return Method

# Print default initial value of context
print('context when calling Method(): ', Method())

# Create a reference to method setting context
method = CreateMethodReference('B')
print('context when calling method: ', method())
