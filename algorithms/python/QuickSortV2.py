def swap(A, i, j):
    if i == j:
        return
    tmp = A[j]
    A[j] = A[i]
    A[i] = tmp

def partition(A, p, q):
    x = A[p]
    i = p+1
    for j in range(p+1, q):
        if A[j] <= x:
            swap(A, i, j)
            i += 1
    swap(A, p, i-1)
    return i-1

def sort(A, p, q):
    if p < q:
        m = partition(A, p, q)
        sort(A, p, m)
        sort(A, m+1, q)

A = [2, 8, 7, 1, 3, 5, 6, 4, 9]

#A = [2, 8, 7, 1]

print(A)

sort(A, 0, len(A))

print(A)
