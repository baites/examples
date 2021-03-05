
import heapq

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
        if r == 0:
            return ''
        elif r == 1:
            return s[0]
        x = 256
        p = 2**61-1
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
                return s[m:n+1]
        return s[0]

s = 'a'*2000
print(Solution().longestPalindrome(s))

# Runtime: 7388 ms, faster than 9.08% of Python online submissions for Longest Palindromic Substring.
# Memory Usage: 77.9 MB, less than 5.02% of Python online submissions for Longest Palindromic Substring.
