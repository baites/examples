#! /usr/bin/env python2

def InsertionSort(a):

    for i in range(1,len(a)):
        j = i
        k = i
        while j > 0:
            j -= 1
            if a[j] > a[k]:
                tmp = a[j]
                a[j] = a[k]
                a[k] = tmp
            k -= 1

a = [5, 2, 4, 6, 1, 3]

InsertionSort(a)

print a

