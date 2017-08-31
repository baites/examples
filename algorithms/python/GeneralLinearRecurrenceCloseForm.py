#! /usr/bin/env python

import numpy as np
import scipy.signal as signal
from scipy.special import binom

def CreatePO(a,b):
    if len(a) > len(b):
        raise ValueError('Array a should be longer than b')
    p = np.zeros(len(b))
    for n in range(len(b)):
        if n == 0:
            p[n] = b[0]
            continue
        p[n] = b[n]
        for m in range(1, n+1):
            p[n] -= a[m-1] * b[n-m]
    return np.poly1d(p[::-1])

def CreateQO(a):
    q = np.zeros(len(a)+1)
    q[0] = 1
    for i in range(len(a)):
        q[i+1] = -a[i]
    return np.poly1d(q[::-1])

def CreateQI(c):
    return np.poly1d(c[::-1])

def CreatePI(d):
    return np.poly1d(d[::-1])

def CreateG(a, b, c=[1], d=[]):
    QO = CreateQO(a)
    PO = CreatePO(a,b)
    QI = CreateQI(c)
    PI = CreatePI(d)
    zM = np.zeros(len(b)+1)
    zM[0] = 1.0
    P = PO * QI + np.poly1d(zM)*PI
    Q = QO * QI
    return P, Q

def EvalCloseForm(r, p, h, n, format='integer'):
    if len(r) != len(p):
        raise ValueError('Residuo array and poles should be same length')
    f = 0
    k = 0
    pold = None
    for i in range(len(r)):
        if k == 0:
            k = 1
        elif p[i] != pold:
            k = 1
        else:
            k += 1
        f += (-1)**k * binom(k+n-1, n) * r[i] * p[i]**-(n+k)
        f += h[i] if i == n and n < len(h) else 0.0
        pold = p[i]
    if format == 'integer':
        f = int(round(f.real))
    elif format == 'real':
        f = f.real
    return f

def LinearRecurrenceSequence(name, size, a, b, c=[1], d=[]):
    print('Name: {}\n'.format(name))
    print('Type: {}'.format(
        'non-homogeneous' if len(d) > 0 else 'homogeneous'
    ))
    print('Degree: {}'.format(len(a)))
    print()
    print('Recurrence coefficients')
    print('a: ', a)
    print('Initial conditions')
    print('b: ', b)
    print()
    if len(d) != 0:
        print('Non-homogeneous rational polynomials')
        print('QI:')
        print(np.poly1d(c))
        print('PI:')
        print(np.poly1d(d))
        print()
    P, Q = CreateG(a, b, c, d)
    print('Generating function')
    print('P:')
    print(P)
    print('Q:')
    print(Q)
    r, p, h = signal.residue(P.c,Q.c)
    print()
    print('Partial fraction expantion')
    print('residue (r)  : ', r)
    print('poles: (eta) : ', p)
    print('remainder (h): ', h)
    print()
    if len(d) > 0 and len(h) == 1 and h[0] == 0:
        print('Can be reduce to homogeneous type')
        print('Recurrence coefficients')
        print('a: ', [-x for x in Q.c[-2::-1]])
        print('Initial conditions')
        print('b: ', [
            EvalCloseForm(r, p, h, n, format='real') for n in range(len(p))
        ])
    print()
    print('Sequence ({})'.format(size))
    for n in range(size):
        print(EvalCloseForm(r, p, h, n), end=', ')
    print()
    print()
    print('------------------------')
    print()

# Natural sequence
b = [0,1]
a = [2,-1]
LinearRecurrenceSequence('Positive integers (A000027)', 20, a, b)

# Natural sequence
b = [0]
a = [1]
c = [1, -1]
d = [1]
LinearRecurrenceSequence('Non-homogeneous positive interngers (A000027)', 20, a, b, c, d)

# Fibonacchi sequence
b = [0,1]
a = [1,1]
LinearRecurrenceSequence('Fibonacchi (A000045)', 20, a, b)

# Tribonacci A000073
b = [0,0,1]
a = [1,1,1]
LinearRecurrenceSequence('Tribonacci (A000073)', 20, a, b)

# Tetranacci A000078
b = [0,0,0,1]
a = [1,1,1,1]
LinearRecurrenceSequence('Tetranacci (A000078)', 20, a, b)

# Pentanacci A001591
b = [0,0,0,0,1]
a = [1,1,1,1,1]
LinearRecurrenceSequence('Pentanacci (A001591)', 20, a, b)

# A006904 sequence
b = [1, 1]
a = [1, 2]
c = [1, 1]
d = [1]
LinearRecurrenceSequence('Non-homogeneous A006904', 20, a, b, c, d)

# (P,Q)-Fibonacchi
P = 1
Q = 2
b = [0,1]
a = [P,Q]
LinearRecurrenceSequence('(1,2)-Fibonacchi: Jacobsthal (A001045)', 20, a, b)

# (P,Q)-Lucas of second kind
P = 2
Q = 1
b = [2,P]
a = [P,Q]
LinearRecurrenceSequence('(2,1)-Lucas: Companion Pell (A002203)', 20, a, b)
