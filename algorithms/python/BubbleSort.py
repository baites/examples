#! /usr/bin/env python2

def BubbleSort(a):
    flag = True;
    while flag:
        flag = False
        for i in range(len(a)):
            if i+1 < len(a) and a[i] > a[i+1]:
                tmp = a[i+1]
                a[i+1] = a[i]
                a[i] = tmp
                flag = True

a = [5, 2, 4, 6, 1, 3, 9, 4, 5]

BubbleSort(a)

print a

