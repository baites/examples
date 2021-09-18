class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:

        # String size
        size = len(s)

        # Dynamic programming array that define if the
        # prefix of s of size i (index of the list) is a word break
        prefix = [False]*(size+1)
        # Base condition assume true null prefix
        prefix[0] = True

        for i in range(size+1):
            for j in range(i+1, size+1):
                new = None
                if s[i:j] in wordDict and prefix[i]:
                    if j == size:
                        return True
                    prefix[j] = True
        return False
