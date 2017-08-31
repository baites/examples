#! /bin/env python

M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

M = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

M = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]


def print_matrix(M):
    for i in range(len(M)):
        string = ''
        for j in range(len(M[i])):
            string += '{} '.format(M[i][j])
        print(string)

import math

def rotate_matrix(M):
    n = len(M)
    m = math.ceil(n/2)
    for i in range(m):
        for j in range(i,n-1-i):
            t1 = M[n-1-i][j]
            M[n-1-i][j] = M[j][i]
            t2 = M[n-1-j][n-1-i]
            M[n-1-j][n-1-i] = t1
            t1 = M[i][n-1-j]
            M[i][n-1-j] = t2
            M[j][i] = t1

print_matrix(M)
print()
rotate_matrix(M)
print_matrix(M)
