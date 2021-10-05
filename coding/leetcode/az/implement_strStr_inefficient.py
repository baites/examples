class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(haystack) < len(needle):
            return -1
        if len(needle) == 0:
            return 0

        for i in range(len(haystack)-len(needle)+1):
            match = True
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    match = False
                    break
            if match:
                return i

        return -1