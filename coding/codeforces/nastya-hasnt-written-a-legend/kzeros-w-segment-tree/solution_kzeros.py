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

    tree = (aval, asum, asize-1)

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


def Update(tree, l, r, x):
    """Update interval value."""
    aval, asum, end = tree

    def _update(node, start, end, x, y = None):
        """Update interval value recursively."""

        # Interval [l,r] is totally out of range
        if r < start or end < l:
            if y is not None:
                aval[node] = y
                asum[node] = y * (end-start+1)
            return

        # Interval [l,r] covers the whole range
        if l <= start and end <= r:
            aval[node] = x
            asum[node] = x * (end-start+1)
            return

        # Interval [l,r] is covered by the whole range
        if start <= r and l <= end and aval[node] is not None:
            y = aval[node] if y is None else y
            aval[node] = None

        mid = (start + end)//2
        _update(2*node+1, start, mid, x, y)
        _update(2*node+2, mid+1, end, x, y)
        asum[node] = asum[2*node+1] + asum[2*node+2]

    _update(0, 0, end, x)
    return tree


def Query(tree, l, r):
    """Update interval value."""
    aval, asum, end = tree

    def _query(node, start, end):
        """Update interval value recursively."""

        # Interval [l,r] is totally out of range
        if r < start or end < l:
            return 0

        # Interval [l,r] covers the whole range
        if l <= start and end <= r:
            return asum[node]

        # Interval [l,r] is covered by the whole range
        if start <= r and l <= end and aval[node] is not None:
            a = max(start, l); b = min(end, r)
            return aval[node] * (b - a + 1)

        mid = (start + end)//2
        q1 = _query(2*node+1, start, mid)
        q2 = _query(2*node+2, mid+1, end)
        return q1+q2

    return _query(0, 0, end)


def Search(tree, l, v):
    """Search end point after update."""
    aval, asum, end = tree
    r = end
    # Binary search to locate end point after update
    while l < r:
        m = (l + r)//2
        q = Query(tree, m, m)
        if v < q:
            r = m-1
        else:
            l = m+1
    # Check if binary search end in next to end point
    if l > 0 and v < Query(tree, l, l):
        return l-1
    return l


def Add(tree, l, x):
    """Update one value."""
    aval, asum, end = tree

    # Search for value at l and add x
    v = Query(tree, l, l) + x
    # Locate end point after update
    r = Search(tree, l, v)
    # Update the segment tree
    Update(tree, l, r, v)


def PrintArray(tree):
    aval, asum, end = tree
    s = ''
    for i in range(end+1):
        s += '{} '.format(Query(tree, i, i))
    print(s)


def main():

    n = int(input().strip())
    a = input().strip().split()
    a = [int(a[i]) for i in range(n)]
    #k = input().strip().split()
    #k = [int(k[i]) for i in range(n-1)]
    q = int(input().strip())

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
