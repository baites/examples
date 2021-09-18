import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join((filter(lambda c: re.match('[a-z]|[0-9]', c), s)))
        return s == s[::-1]