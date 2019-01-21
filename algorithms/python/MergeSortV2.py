
def Merge(A, p, m, q):
    L = [A[i] for i in range(p,m)]
    R = [A[i] for i in range(m,q)]
    sL = len(L)
    sR = len(R)
    pL = 0
    pR = 0
    while pL < sL or pR < sR:
        if pL == sL:
            A[p] = R[pR]
            pR += 1
        elif pR == sR:
            A[p] = L[pL]
            pL += 1
        elif L[pL] < R[pR]:
            A[p] = L[pL]
            pL += 1
        else:
            A[p] = R[pR]
            pR += 1
        p += 1

def Sort(A, p, q):
    if q-p <= 1:
        return
    m = (p+q)//2
    Sort(A, p, m)
    Sort(A, m, q)
    Merge(A, p, m, q)

a = [2, 8, 7, 1, 3, 6, 4 , 3, 5, 6, 4]

print('Before: ', a)
Sort(a, 0, len(a))
print('After: ', a)
