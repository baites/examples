#! /usr/bin/env python

inmutable = 1
global_inmutable = 1
mutable = [1]

def func():
    global global_inmutable
    inmutable = 1
    global_inmutable = 2
    mutable.append(2)

print('Initial inmutable: ', inmutable)
print('Initial global inmutable: ', global_inmutable)
print('Initial inmutable: ', mutable)
func()
print('Final inmutable: ', inmutable)
print('Final global inmutable: ', global_inmutable)
print('Final inmutable: ', mutable)
