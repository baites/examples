class Solution:
    def isPalindrome(self, s: str) -> bool:
        u = 0
        v = len(s)-1

        s = s.lower()

        while u <= v:
            if not s[u].isalnum():
                u += 1
                continue
            if not s[v].isalnum():
                v -= 1
                continue
            if s[u] != s[v]:
                return False
            u += 1
            v -= 1

        return True