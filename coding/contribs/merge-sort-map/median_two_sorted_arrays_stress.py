class Naive(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()
        size = len(nums)
        if size % 2 == 1:
            return float(nums[size//2])
        return 0.5*(nums[size//2-1] + nums[size//2])


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


    def findMedianSortedArrays(self, A, B):
        """Compute the median of two sorted arrays."""
        S = len(A) + len(B)
        return 0.5 * (
            self.mergeSortMap(A, B, ((S-1)//2)+1) +\
            self.mergeSortMap(A, B, (S//2)+1)
        )


import random
import time

random.seed(1234)
random.getstate()
tries = 10
size = 4000000
maxv = 10000000
#size = 1000
#maxv = 400

agg_naive = 0.0
agg_solution = 0.0

for n in range(tries):
    val = random.randint(0,maxv)
    size1 = random.randint(0,size)
    size2 = random.randint(0,size)
    if size1 == 0 and size2 == 0:
        continue
    nums1 = [random.randint(-val,val) for i in range(size1)]
    nums2 = [random.randint(-val,val) for i in range(size2)]
    nums1.sort()
    nums2.sort()

    #print('A = {}'.format(nums1))
    #print('B = {}'.format(nums2))

    start = time.time()
    naive = Naive().findMedianSortedArrays(nums1, nums2)
    naive_time = time.time()
    solution = Solution().findMedianSortedArrays(nums1, nums2)
    solution_time = time.time()
    speedup = (naive_time - start)/\
                (solution_time - naive_time)
    agg_naive += naive_time - start
    agg_solution += solution_time - naive_time

    if naive == solution:
        print('naive = {}, solution = {} (x{})'.format(
            naive, solution, speedup
        ))
        print('ok')
    else:
        print('naive = {}, solution = {}'.format(naive, solution))
        print('bad')
        break

print('naive time = {}'.format(agg_naive))
print('solution time = {}'.format(agg_solution))
print('agg speedup = {}'.format(agg_naive/agg_solution))
