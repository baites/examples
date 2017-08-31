import math

def exchange(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

def parent(i):
    return int(math.floor(i/2))

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def maxheap(A, i, heapsize):
    l = left(i)
    r = right(i)
    largest = i
    if l < heapsize and A[l] > A[i]:
        largest = l
    if r < heapsize and A[r] > A[largest]:
        largest = r
    if largest != i:
        exchange(A, i, largest)
        maxheap(A, largest, heapsize)

def buildmaxheap(A):
    heapsize = len(A)
    start = int(math.floor(heapsize/2))
    for i in range(start-1,-1,-1):
        maxheap(A, i, heapsize)

def heapsort(A):
    buildmaxheap(A)
    heapsize = len(A)
    for i in range(heapsize-1, 0, -1):
        exchange(A, 0, i)
        heapsize -= 1
        maxheap(A, 0, heapsize)

a = [2, 8, 7, 1, 3, 5, 6, 4]

print(a)
heapsort(a)
print(a)
