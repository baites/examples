#! /usr/bin/env python

context = 'method1 context'
def Method1():
    return context;

def CreateMethod1():
    context = 'method1 context?'
    return Method1

def CreateMethod2():
    context = 'method2 context'
    def Method2():
        return context
    return Method2

method1 = CreateMethod1()
print(method1())

method2 = CreateMethod2()
print(method2())
