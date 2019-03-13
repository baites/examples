
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
                        #palin = s[i:j+1]
        return M#, palin

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
        M = 1
        x = 31
        p = 199
        for m in range(r):
            y = 1
            F = ord(s[m])
            B = ord(s[m])
            for n in range(m+1, r):
                y *= x
                F = (F + ord(s[n])*y) % p
                B = (x*B + ord(s[n])) % p
                print(F,B,m,n)
                if F == B and self.isPalindrome(s, m, n):
                    length = n-m+1
                    if length > M:
                        M = n-m+1
        return M

s = 'ababa'
print(Naive().longestPalindrome(s))
print(Solution().longestPalindrome(s))
#print(Solution().lengthOfLongestSubstring(s))
