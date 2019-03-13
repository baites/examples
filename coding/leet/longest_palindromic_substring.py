
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
        for l in range(r, 1, -1):
            for i in range(r - l + 1):
                if self.isPalindrome(s, i, i+l-1):
                    return s[i:i+l]
        return s[0]

s = 'a'*1000
print(Solution().longestPalindrome(s))

# Runtime: 9876 ms, faster than 5.27% of Python online submissions for Longest Palindromic Substring.
# Memory Usage: 10.8 MB, less than 53.28% of Python online submissions for Longest Palindromic Substring.
