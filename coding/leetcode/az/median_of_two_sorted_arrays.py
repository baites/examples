class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Assiming A and B two sorted arrays.
        # We can build an algorithm O(A+B)
        #      a              ILLEGAL!
        # A = -2 -1 0 3 4
        # B =  0  1 2 3 4 5 6
        #         b
        # Assime that a > 0
        #   then in general illegal if B[b] < A[a-1]
        # In case same arrays but switching labels A <-> B
        # Assuming that b > 0
        #   then it is  illegal if A[a] < B[b-1]
        # else a, b point to legal configuration with value
        #   value = A[a] if b == size(B)
        #   value = B[b] if a == size(A)
        #   value = min(A[a], B[b]) otherwise

        # Define illigal configs
        def illegal_increase_n1(n1, n2):
            if n1 == len(nums1):
                return False
            return n2 > 0 and nums1[n1] < nums2[n2-1]

        def illegal_decrease_n1(n1, n2):
            if n2 == len(nums2):
                return False
            return n1 > 0 and nums2[n2] < nums1[n1-1]

        # Array sizes
        size1 = len(nums1)
        size2 = len(nums2)

        # Set array1 to be the smaller
        if size1 > size2:
            nums1, nums2 = nums2, nums1
            size1, size2 = size2, size1

        if size1 == 0:
            if size2%2 == 1:
                return nums2[size2//2]
            else:
                return (nums2[size2//2]+nums2[size2//2-1])/2

        # Compute array value ussing indexes
        def value(n1, n2):
            if n1 == size1:
                return nums2[n2]
            elif n2 == size2:
                return nums1[n1]
            return min(nums1[n1], nums2[n2])

        # Binary search
        left = 0
        right = size1+1

        while 1:
            n1 = (left + right)//2
            n2 = (size1 + size2)//2 - n1
            if illegal_increase_n1(n1, n2):
                left = n1 + 1
            elif illegal_decrease_n1(n1, n2):
                right = n1 - 1
            else:
                break

        value1 = value(n1, n2)

        print(n1, n2)

        # If even return directly value
        if (size1 + size2)%2 == 1:
            return value1

        # Try increasing n1 first
        if n1 == 0 or illegal_increase_n1(n1-1, n2):
            value2 = value(n1,n2-1)
        else:
            value2 = value(n1-1,n2)

        print(value1, value2, n1, n2)

        return (value1+value2)/2