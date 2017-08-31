#! /usr/bin/env python

class StaticVarTest(object):
    _statvar = 'None'
    def __init__(self, statvar):
        StaticVarTest._statvar = statvar


t = StaticVarTest('hi')
p = StaticVarTest('bye')
print(t._statvar)
print(p._statvar)
