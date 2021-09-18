
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join((filter(lambda c: c.isalnum(), s)))
        return s == s[::-1]