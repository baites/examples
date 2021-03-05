# https://leetcode.com/problems/reverse-string/

class Solution(object):
    def reverseString(self, s, l=0, r=None):
        """
        :type s: List[str]
        :rtype: void Do not return anything, modify s in-place instead.
        """
        if r is None:
            r = len(s)
        if l >= r:
            return
        self.reverseString(s, l+1, r-1)
        tmp = s[l]
        s[l] = s[r-1]
        s[r-1] = tmp

s = ['h','e','l','l','o']
s = ["H","a","n","n","a","h"]

Solution().reverseString(s)
print(s)
