
class Naive(object):

    def lengthOfLongestSubstring(self, s):
        r = len(s)
        M = 0
        for i in range(0, r):
            for j in range(i+1, r+1):
                charset = set()
                for k in range(i,j):
                    charset.add(s[k])
                if len(charset) == j-i:
                    M = max(M, j-i)
        return M


class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        r = len(s)
        if r == 0:
            return r
        charset = set()
        for i in range(r):
            charset.add(s[i])
        nchars = len(charset)
        M = 0
        while l < r:
            charset = {}
            for j in range(l,r+1):
                if j == r or s[j] in charset:
                    break
                charset[s[j]] = j
            M = max(M, j-l)
            if j == r or M == nchars:
                break
            l = charset[s[j]] + 1
            while l < r-1 and s[l+1] == s[l]:
                l += 1
        return M


s = 'bbbc'
print(Naive().lengthOfLongestSubstring(s))
print(Solution().lengthOfLongestSubstring(s))

# Runtime: 60 ms, faster than 68.49% of Python online submissions for Longest Substring Without Repeating Characters.
# Memory Usage: 12.1 MB, less than 10.90% of Python online submissions for Longest Substring Without Repeating Characters.
