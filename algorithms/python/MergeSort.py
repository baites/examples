#! /usr/bin/env python

def Merge(A, p, q, r):
    L = []
    for i in range(p,q):
        L.append(A[i]);
    lenL = len(L)
    R = []
    for i in range(q,r):
        R.append(A[i])
    lenR = len(R)
    i = 0
    j = 0
    for k in range(p,r):
        if i == lenL and j == lenR:
            return
        if i == lenL:
            A[k] = R[j]
            j += 1
            continue
        if j == lenR:
            A[k] = L[i]
            i += 1
            continue
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

import math

def MergeSort(A, p, r):
    if p < (r-1) :
        q = int(math.floor((p+r)/2))
        MergeSort(A, p, q)
        MergeSort(A, q, r)
        Merge(A, p, q, r)


a = [2, 8, 7, 1, 3, 5, 6, 4]

print('Before: ', a)
MergeSort(a,0,len(a))
print('After: ', a)
