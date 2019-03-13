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
        for l in range(r, 1, -1):
            for i in range(r - l + 1):
                if self.isPalindrome(s, i, i+l-1):
                    return l
        return 1

s = 'ababaaababa'
print(Naive().longestPalindrome(s))
print(Solution().longestPalindrome(s))
#print(Solution().lengthOfLongestSubstring(s))
