class Naive(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()
        size = len(nums)
        if size % 2 == 1:
            return float(nums[size//2])
        return 0.5*(nums[size//2-1] + nums[size//2])


class Solution(object):

    def findMedianSortedArray(self, A):
        """Find median for an assorted array."""
        S = len(A)
        m = S//2
        if S % 2 == 1:
            return float(A[m])
        return 0.5*(A[m] + A[m-1])

    def isEdgeCase(self, A1, A2):
        """Check for edge cases solutions."""
        # Array size
        S1 = len(A1)
        S2 = len(A2)
        S = S1 + S2
        m = S//2

        # One empty array
        if S1 == 0:
            return self.findMedianSortedArray(A2)
        if S2 == 0:
            return self.findMedianSortedArray(A1)

        # None overlaping arrays
        if A1[-1] < A2[0]:
            if S % 2 == 1:
                if S1 > m:
                    return A1[m]
                else:
                    return A2[m-S1]
            else:
                if S1 > m:
                    return 0.5*(A1[m]+A1[m-1])
                elif m > S1:
                    return 0.5*(A2[m-S1]+A2[m-1-S1])
                else:
                    return 0.5*(A2[0]+A1[-1])
        if A2[-1] < A1[0]:
            if S % 2 == 1:
                if S2 > m:
                    return A2[m]
                else:
                    return A1[m-S2]
            else:
                if S2 > m:
                    return 0.5*(A2[m]+A2[m-1])
                elif m > S2:
                    return 0.5*(A1[m-S2]+A1[m-1-S2])
                else:
                    return 0.5*(A1[0]+A2[-1])
        return None

    def findMedianHelper(self, A1, A2):
        """Help to find the median between arrays."""

        # Array size
        S1 = len(A1)
        S2 = len(A2)
        S = S1 + S2
        m = S//2
        l1 = 0
        r1 = S1+1
        l2 = 0
        r2 = S2+1
        o1 = -1
        o2 = -1
        maxcount = -1

        # Binary search
        while l1 < r1 and l2 < r2:
            m1 = (l1 + r1)//2
            m2 = (l2 + r2)//2
            # Correct value to median location
            count = 0
            while (m1+m2) != m:
                count += 1
                if (m1 + m2) > m:
                    if m1 > l1 and ((m1-1) != o1 or m2 != o2):
                        m1 -= 1
                    else:
                        m2 -= 1
                else:
                    if m1 < (r1-1) and ((m1+1) != o1 or m2 != o2):
                        m1 += 1
                    else:
                        m2 += 1
            maxcount = max(count, maxcount)
            o1 = m1
            o2 = m2
            if m1 > 0 and m2 < S2 and A1[m1-1] > A2[m2]:
               r1 = m1+1
               l2 = m2
            elif m2 > 0 and m1 < S1 and A2[m2-1] > A1[m1]:
                l1 = m1
                r2 = m2+1
            else:
                break
        print(maxcount)
        if m1 < S1 and m2 < S2:
            return min(A1[m1],A2[m2])
        elif m2 == S2:
            return A1[m1]
        else:
            return A2[m2]

    def findMedianSortedArrays(self, A1, A2):
        """
    #    :type A1: List[int]
    #    :type A2: List[int]
    #    :rtype: float
    #    """
        S = len(A1) + len(A2)
        edge = self.isEdgeCase(A1, A2)
        if edge is not None:
            return edge
        median1 = self.findMedianHelper(A1, A2)
        if S % 2 == 1:
            return float(median1)
        if A1[-1] > A2[-1]:
            A1.pop()
        else:
            A2.pop()
        edge = self.isEdgeCase(A1, A2)
        if edge is not None:
            return 0.5*(median1+edge)
        median2 = self.findMedianHelper(A1, A2)
        return 0.5*(median1+median2)


import random
import time

size = 10
maxv = 100

while 1:
    val = random.randint(0,maxv)
    size1 = random.randint(0,size)
    size2 = random.randint(0,size)
    if size1 == 0 and size2 == 0:
        continue
    nums1 = [random.randint(-val,val) for i in range(100)]
    nums2 = [random.randint(-val,val) for i in range(2)]
    nums1.sort()
    nums2.sort()

    print('A1 = {}'.format(nums1))
    print('A2 = {}'.format(nums2))

    start = time.time()
    naive = Naive().findMedianSortedArrays(nums1, nums2)
    naive_time = time.time()
    solution = Solution().findMedianSortedArrays(nums1, nums2)
    solution_time = time.time()
    speedup = (naive_time - start)/\
                (solution_time - naive_time)

    if naive == solution:
        print('naive = {}, solution = {} (x{})'.format(
            naive, solution, speedup
        ))
        print('ok')
    else:
        print('naive = {}, solution = {}'.format(naive, solution))
        print('bad')
        break
