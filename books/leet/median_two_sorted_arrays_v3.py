# https://leetcode.com/problems/median-of-two-sorted-arrays/

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

    def findMedianIndexes(self,
        l1, r1, l2, r2, m
    ):
        o1 = -1; o2 = -1
        while 1:
            m1 = (l1+r1)//2
            m2 = (l2+r2)//2
            if m1 == o1 and m2 == o2:
                for m1 in range(l1, r1):
                    for m2 in range(l2, r2):
                        if m1+m2 == m and\
                            (m1 != o1 or m2 != o2):
                            return m1, m2
            o1 = m1
            o2 = m2
            if (m1 + m2) > m:
                r1 = m1+1
                r2 = m2+1
            elif (m1 + m2) < m:
                l1 = m1
                l2 = m2
            else:
                return m1, m2

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

        # Binary search
        while 1:
            m1, m2 = self.findMedianIndexes(
                l1, r1, l2, r2, m
            )
            if m1 > 0 and m2 < S2 and A1[m1-1] > A2[m2]:
               r1 = m1
               l2 = m2+1
            elif m2 > 0 and m1 < S1 and A2[m2-1] > A1[m1]:
                l1 = m1+1
                r2 = m2
            else:
                break
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
            return float(edge)
        median1 = self.findMedianHelper(A1, A2)
        if S % 2 == 1:
            return float(median1)
        if A1[-1] > A2[-1]:
            A1.pop()
        else:
            A2.pop()
        median2 = self.findMedianHelper(A1, A2)
        return 0.5*float(median1+median2)

A1 = [1, 2]
A2 = [3, 4]

import random

solution = Solution().findMedianSortedArrays(A1, A2)
print(solution)

# Runtime: 64 ms, faster than 52.83% of Python online submissions for Median of Two Sorted Arrays.
# Memory Usage: 10.9 MB, less than 100.00% of Python online submissions for Median of Two Sorted Arrays.
