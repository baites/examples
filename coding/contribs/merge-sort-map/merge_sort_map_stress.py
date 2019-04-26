
class Naive(object):

    def mergeSortMap(self, A, B, n):
        AB = A + B
        AB.sort()
        S = len(AB)
        # Sanity check
        if n < 1 or n > S:
            raise IndexError('merge-sort map index out of range')
        return AB[n-1]


class Solution(object):

    def isNotHeadTailCondition(self, X, Y, nX, nY):
        """Check for the negative of the head-tail condition."""
        return nX > 0 and nY < len(Y) and X[nX-1] > Y[nY]

    def getMergeSortArrayValue(self, A, B, nA, nB):
        """Get the value of merge-sort array."""
        if nA == 0:
            value = B[nB-1]
        elif nB == 0:
            value = A[nA-1]
        else:
            value = max(A[nA-1], B[nB-1])
        return value

    def mergeSortMap(self, A, B, n):
        """Help to find the median between arrays."""

        # Array size
        SA = len(A)
        SB = len(B)

        # Sanity check
        if SA == 0 and SB == 0:
            raise Exception('empty both arrays')
        if n < 1 or n > SA + SB:
            raise IndexError('merge-sort map index out of range')

        # Edge case one empty array
        if SA == 0:
            return B[n-1]
        if SB == 0:
            return A[n-1]

        # Check swap arrays to keep A as smaller array
        if SA > SB:
            SA, SB = SB, SA
            A, B = B, A

        # Interval initialization
        left = 0
        right = min(n, SA)

        # Binary search
        while 1:
            # Binapartition of nA range
            nA = (left + right)//2
            # Derive value for nB
            nB = n - nA
            # Check if nB is out of range,
            # meaning nA too small.
            if nB > SB:
                left = nA + 1
            # Check if first head/tail condition tails
            # meaning that nA is too large
            elif self.isNotHeadTailCondition(A, B, nA, nB):
                right = nA - 1
            # Check if first head/tail condition tails
            # meaning that nA is too small
            elif self.isNotHeadTailCondition(B, A, nB, nA):
                left = nA + 1
            # Break if all conditions are met
            else:
                break
        # Get the value of merge-sort array
        return self.getMergeSortArrayValue(A, B, nA, nB)


import random
import time

#random.seed(1234)
#random.getstate()
tries = 200
#maxs = 4000000
#maxv = 10000000
maxs = 600
maxv = 400

agg_refs = 0.0
agg_test = 0.0

for n in range(tries):
    val = random.randint(0,maxv)
    SA = random.randint(0, maxs)
    SB = random.randint(0, maxs)
    if SA == 0 and SB == 0:
        continue
    n = random.randint(1, SA+SB)
    A = [random.randint(-val,val) for i in range(SA)]
    B = [random.randint(-val,val) for i in range(SB)]
    A.sort()
    B.sort()

    #print('n = {}'.format(n))
    #print('A = {}'.format(A))
    #print('B = {}'.format(B))

    naive = Naive()
    solution = Solution()

    start = time.time()
    refs = naive.mergeSortMap(A, B, n)
    refs_time = time.time()
    test = solution.mergeSortMap(A, B, n)
    test_time = time.time()
    speedup = (refs_time - start)/\
                (test_time - refs_time)
    agg_refs += refs_time - start
    agg_test += test_time - refs_time

    if refs == test:
        print('refs = {}, test = {} (x{})'.format(
            refs, test, speedup
        ))
        print('ok')
    else:
        print('refs = {}, test = {}'.format(refs, test))
        print('bad')
        break

print('refs time = {}'.format(agg_refs))
print('test time = {}'.format(agg_test))
print('agg speedup = {}'.format(agg_refs/agg_test))
