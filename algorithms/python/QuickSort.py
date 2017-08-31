def Exchange(A, i, j):
    if i == j:
        return
    x = a[j]
    a[j] = a[i]
    a[i] = x


def Partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if a[j] <= x:
            i += 1
            Exchange(A,i,j)
    Exchange(A,i+1,r)
    return i+1


def QuickSort(A, p, r):
    print (A, p, r)
    if p < r:
        q = Partition(A,p,r)
        QuickSort(A,p,q-1)
        QuickSort(A,q+1,r)


a = [2, 8, 7, 1, 3, 5, 6, 4]

QuickSort(a,0,7)

print(a)
