#! /usr/bin/env python2

def FindArrayMatch(a,b):

    i = 0; j = 0

    prev = None;

    while i < len(a) and j < len(b):

        if a[i] < b[j]:
            i += 1
        elif a[i] > b[j]:
            j += 1

        if a[i] == b[j]:
            if not prev:
                print a[i]
            elif prev != a[i]:
                print a[i]
            prev = a[i]
            i += 1
            j += 1


a = [1,2,3,4,8,8,9,9,10,12]

b = [2,5,6,8,8,12]

FindArrayMatch(a,b)

