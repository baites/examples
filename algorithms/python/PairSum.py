#! /bin/env python

def PairSumSort(A, x):
    A.sort()
    i = 0
    j = len(A) - 1
    while i<j:
        s = A[i]+A[j]
        if s == x:
            print('Pair found [{},{}] with sum {}'.format(
                A[i], A[j], x
            ))
            return
        elif s > x:
            j -= 1
        else:
            i += 1

    print('No pair found with sum == {}'.format(s))


def PairSumHash(A, x):
    S = set()
    for i in range(len(A)):
        d = x - A[i]
        if d in S:
            print('Pair found [{},{}] with sum {}'.format(
                d, A[i], x
            ))
            return
        else:
            S.add(A[i])
    print('No pair found with sum == {}'.format(x))


x = 16
A = [1, 4, 45, 6, 10, -8]

print('Running sorting method')
PairSumSort(A, x)
print()
print('Running hash method')
PairSumHash(A, x)
