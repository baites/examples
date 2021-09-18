# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
bad_version = 4

def isBadVersion(version):
    return version >= bad_version

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Edge case
        if isBadVersion(1):
            return 1

        # Exponetial search
        n = 1
        # left == last known good version
        left = 1
        while not isBadVersion(n):
            left = n
            n *= 2
        # right == last known bad version
        right = n

        while left+1 != right:
            middle = (left+right)//2
            if isBadVersion(middle):
                right = middle
            else:
                left = middle

        return right