
import heapq

class Naive(object):

    def isPalindrome(self, s, m, n):
        while n > m:
            if s[m] != s[n]:
                return False
            m += 1
            n -= 1
        return True

    def longestPalindrome(self, s):
        r = len(s)
        if r <= 1:
            return r
        M = 1
        for m in range(r):
            for n in range(m+1, r):
                if self.isPalindrome(s, m, n):
                    length = n-m+1
                    if length > M:
                        M = n-m+1
        return M


class Solution(object):

    def isPalindrome(self, s, m, n):
        while n > m:
            if s[m] != s[n]:
                return False
            m += 1
            n -= 1
        return True

    def longestPalindrome(self, s):
        r = len(s)
        if r <= 1:
            return r
        x = 256
        p = 2**31-1
        heap = []
        for m in range(r):
            y = 1
            F = ord(s[m])
            B = ord(s[m])
            for n in range(m+1, r):
                y = (y * x) % p
                F = (F + ord(s[n])*y) % p
                B = (x*B + ord(s[n])) % p
                if F == B:
                    heapq.heappush(heap, (-(n-m+1), m, n))
        while len(heap) > 0:
            l, m, n  = heapq.heappop(heap)
            if self.isPalindrome(s, m, n):
                return -l
        return 1

s = 'ewyedhssshadd'
print(Naive().longestPalindrome(s))
print(Solution().longestPalindrome(s))
#print(Solution().lengthOfLongestSubstring(s))
