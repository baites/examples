
class Solution(object):

    def isNotHeadTailCondition(self, X, Y, nX, nY):
        """Check for the negative of the head-tail condition."""
        return nX > len(X) or nX > 0 and nY < len(Y) and X[nX-1] > Y[nY]

    def mergeSortMap(self, A, B, n):
        """Help to find the median between arrays."""

        # Array size
        SA = len(A)
        SB = len(B)

        # Sanity check
        if SA == 0 and SB == 0:
            raise Exception('empty both arrays')
        if n < 1:
            raise IndexError('merge-sort map index out of range')

        # Edge case
        if SA == 0:
            return B[n-1] if n < SB else B[SB-1]
        if SB == 0:
            return A[n-1] if n < SA else A[SA-1]

        # Check swap arrays to keep A as smaller array
        if SA > SB:
            SA, SB = SB, SA
            A, B = B, A

        # Interval initialization
        left = 0
        right = min(n, SA)

        # Binary search
        while 1:
            nA = (left + right)//2
            nB = n - nA
            if self.isNotHeadTailCondition(A, B, nA, nB):
                right = nA - 1
            elif self.isNotHeadTailCondition(B, A, nB, nA):
                left = nA + 1
            else:
                break
        print(nA, nB)
        if nA == 0:
            value = B[nB-1]
        elif nB == 0:
            value = A[nA-1]
        else:
            value = max(A[nA-1], B[nB-1])
        return value

#A = [-2, -2, -1, 0, 1, 1, 2]
#B = [-1, -1,  0, 0, 1, 1, 2]

#n = 14
#A = [-2, -1, -1, 1, 2, 2]
#B = [-3, -3, -3, -2, -1, 0, 1, 1, 1]

n = 2
A = [5]
B = [-4]

print(Solution().mergeSortMap(A, B, n))
