#! /usr/bin/env python

import numpy as np

def CreateP(a,b):
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

def CreateQs(a):
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

def EvalCloseForm(c, r, n):
    if len(c) != len(r):
        raise ValueError('Coeff and root arrays are not same size')
    f = 0
    for k in range(len(c)):
        f += c[k] * r[k]**n
    return f


# Fibonacchi sequence
# b = np.array([0,1])
# a = np.array([1,1])
# Tribonacci A000073 in the OEIS
b = np.array([0,0,1])
a = np.array([1,1,1])
# Tetranacci A000078 in the OEIS
# b = np.array([0,0,0,1])
# a = np.array([1,1,1,1])
# Pentanacci A001591 in the OEIS
# b = np.array([0,0,0,0,1])
# a = np.array([1,1,1,1,1])
# (P,Q)-Fibonacchi sequence
# P = 1
# Q = 2
# b = np.array([0,1])
# a = np.array([P,Q])
# (P,Q)-Lucas sequence of second kind
# P = 2
# Q = 1
# b = np.array([2,P])
# a = np.array([P,Q])

P = CreateP(a,b)
Q = CreateQs(a)

c, r = GetCloseForm(P,Q)
for n in range(20):
   print(EvalCloseForm(c, r, n),end=', ')
print()
