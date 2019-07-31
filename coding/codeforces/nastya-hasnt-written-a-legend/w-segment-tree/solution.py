# python3

import math
import threading
import sys

# max depth of recursion
sys.setrecursionlimit(10**7)

# new thread will get stack of such size
threading.stack_size(2**27)


def BuildTree(a):
    """Create a segment tree in arrays."""

    # One array per node fields
    asize = len(a)
    height = int(math.ceil(math.log2(asize)))
    aval = [None]*(2**(height+1) - 1)
    asum = [None]*(2**(height+1) - 1)

    tree = (aval, asum)

    def _build(node, start, end):
        """Create the tree recursively."""
        nonlocal aval, asum

        if start == end:
            aval[node] = a[start]
            asum[node] = a[start]
        else:
            mid = (start + end)//2
            _build(2*node+1, start, mid)
            _build(2*node+2, mid+1, end)
            asum[node] = asum[2*node+1] + asum[2*node+2]

    # Create the tree
    _build(0, 0, asize-1)
    # Return tree arrays
    return tree


Sk = []
SSk = []


def IntVal(a, start, end):
    global Sk
    val = a
    if end > start:
        val += Sk[end-1]
        if start > 0:
            val -= Sk[start-1]
    return val


def IntSum(a, start, end):
    global Sk, SSk
    val = a*(end-start+1)
    if end > start:
        val += SSk[end-1]
        if start > 0:
            val -= (Sk[start-1]*(end-start) + SSk[start-1])
    return val


def Update(tree, left, right, x):
    """Update interval value."""
    aval, asum = tree

    end = len(k)

    counter = 0

    def _update(node, start, end, x, y = None):
        """Update interval value recursively."""
        nonlocal counter
        counter += 1

        # Interval [left,right] is totally out of segment
        if right < start or end < left:
            if y is not None:
                sy, y = y
                aval[node] = IntVal(y, sy, start)
                asum[node] = IntSum(aval[node], start, end)
            return

        # Interval [left,right] covers the whole segment
        if left <= start and end <= right:
            sx, x = x
            aval[node] = IntVal(x, sx, start)
            asum[node] = IntSum(aval[node], start, end)
            return

        # Interval [left,right] is covered by the whole segment
        if start <= right and left <= end and aval[node] is not None:
            y = (start, aval[node]) if y is None else y
            aval[node] = None

        mid = (start + end)//2
        _update(2*node+1, start, mid, x, y)
        _update(2*node+2, mid+1, end, x, y)
        asum[node] = asum[2*node+1] + asum[2*node+2]

    _update(0, 0, end, (left, x))
    print('Update: ', counter)
    return tree


def Query(tree, left, right):
    """Update interval value."""
    aval, asum = tree
    end = len(k)

    #counter = 0

    def _query(node, start, end):
        """Update interval value recursively."""
        #nonlocal counter
        #counter += 1

        # Interval [left,right] is totally out of segment [start,end]
        if right < start or end < left:
            return 0

        # Interval [left,right] covers the whole segment [start,end]
        if left <= start and end <= right:
            return asum[node]

        # Segment [start,end] covered interval [left,right]
        if start <= right and left <= end and aval[node] is not None:
            b = min(end, right)
            value = IntSum(aval[node], start, b)
            a = max(start, left)
            if a > 0:
                value -= IntSum(aval[node], start, a-1)
            return value

        mid = (start + end)//2
        q1 = _query(2*node+1, start, mid)
        q2 = _query(2*node+2, mid+1, end)
        return q1+q2

    value = _query(0, 0, end)
    #print('Query: ', counter)
    return value


a = []
k = []

def Search(tree, l, x):
    """Search end point after update."""
    global a, k
    right = len(k)
    left = l
    counter = 0
    # Binary search to locate end point after update
    while left < right:
        counter += 1
        mid = (left + right)//2
        q  = IntVal(x, l, mid) + k[mid]
        v  = Query(tree, mid+1, mid+1)
        #print(q, v, left, mid, right)
        if q > v:
            left = mid+1
        else:
            right = mid
    print('Search: ', counter)
    return left


def Add(tree, left, x):
    """Update one value."""
    aval, asum = tree

    # Search for value at l and add x
    value = Query(tree, left, left) + x
    # Locate end point after update
    right = Search(tree, left, value)
    # Update the segment tree
    Update(tree, left, right, value)


def PrintArray(tree):
    aval, asum = tree
    s = ''
    for i in range(len(k)+1):
        s += '{} '.format(Query(tree, i, i))
    print(s)


def PreprocKsums(k):
    """Preprocess K sum values."""
    global Sk, SSk

    Sk = [0]*len(k)
    Sk[0] = k[0]
    for i in range(1, len(k)):
        Sk[i] = k[i] + Sk[i-1]

    SSk = [0]*len(Sk)
    SSk[0] = Sk[0]
    for i in range(1, len(Sk)):
        SSk[i] = Sk[i] + SSk[i-1]


def main():
    global a, k

    n = int(input().strip())
    a = input().strip().split()
    a = [int(a[i]) for i in range(n)]
    k = input().strip().split()
    k = [int(k[i]) for i in range(n-1)]
    q = int(input().strip())

    PreprocKsums(k)

    #print(Sk)
    #print(SSk)

    tree = BuildTree(a)

    for j in range(q):
        #PrintArray(tree)
        line = input().split()
        if line[0] == 's':
            l = int(line[1])
            r = int(line[2])
            #print('s {} {}'.format(l, r))
            print(Query(tree, l-1, r-1))
        elif line[0] == '+':
            i = int(line[1])
            x = int(line[2])
            #print('+ {} {}'.format(i, x))
            Add(tree, i-1, x)
        else:
            print('unknown ops')

    #PrintArray(tree)

if __name__ == "__main__":
    threading.Thread(target=main).start()
