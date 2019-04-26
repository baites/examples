
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


A = [-2, -2, -1, 0, 1, 1, 2]
B = [-1, -1,  0, 0, 1, 1, 2]

print(Solution().findMedianSortedArrays(A, B))
