#! /usr/bin/env python

import numpy as np

def CreateP(a,b):
    if len(a) != len(b):
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

def CreateQ(a):
    q = np.zeros(len(a)+1)
    q[0] = 1
    for i in range(len(a)):
        q[i+1] = -a[i]
    return np.poly1d(q[::-1])

def GetCloseForm(P,Q):
    Qr = np.poly1d(Q.coeffs[::-1])
    r = Qr.roots
    if len(r) < Qr.order:
        raise ValueError('There is not trivial close form')
    dQ = np.polyder(Q)
    c = np.zeros(len(r), dtype=np.complex128)
    for k in range(len(c)):
        c[k] = -r[k] * np.polyval(P, 1/r[k]) / np.polyval(dQ, 1/r[k])
    return c, r

def EvalCloseForm(c, r, n, format='integer'):
    if len(c) != len(r):
        raise ValueError('Coeff and root arrays are not same size')
    f = 0
    for k in range(len(c)):
        f += c[k] * r[k]**n
    if format == 'integer':
        f = int(round(f.real))
    elif format == 'real':
        f = f.real
    return f

def LinearRecurrenceSequence(name, size, a, b):
    print('Name: {}\n'.format(name))
    print('Degree: {}'.format(len(a)))
    print()
    print('Recurrence coefficients')
    print('a: ', a)
    print('Initial conditions')
    print('b: ', b)
    print()
    P = CreateP(np.array(a),np.array(b))
    print('Generating function')
    print('P:')
    print(P)
    Q = CreateQ(np.array(a))
    print('Q:')
    print(Q)
    c, r = GetCloseForm(P,Q)
    print()
    print('Partial fraction expantion')
    print('coefficients (c)  : ')
    print(c)
    print('roots: (eta) : ')
    print(r)
    print()
    print('Sequence ({})'.format(size))
    for n in range(size):
        print(EvalCloseForm(c, r, n), end=', ')
    print()
    print()
    print('------------------------')
    print()

# Fibonacchi (A000045)
b = [0,1]
a = [1,1]
LinearRecurrenceSequence('Fibonacchi (A000045)', 20, a, b)

# Tribonacci (A000073)
b = [0,0,1]
a = [1,1,1]
LinearRecurrenceSequence('Tribonacci (A000073)', 20, a, b)

# Tetranacci (A000078)
b = [0,0,0,1]
a = [1,1,1,1]
LinearRecurrenceSequence('Tetranacci (A000078)', 20, a, b)

# Pentanacci (A001591)
b = [0,0,0,0,1]
a = [1,1,1,1,1]
LinearRecurrenceSequence('Pentanacci (A001591)', 20, a, b)

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
