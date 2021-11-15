class Solution:
    def firstUniqChar(self, s: str) -> int:
        indexes = {}
        for i in range(len(s)):
            if s[i] in indexes:
                indexes[s[i]] = -1
            else:
                indexes[s[i]] = i
        min_index = -1
        for _, index in indexes.items():
            if min_index == -1 or index > 0 and index < min_index:
                min_index = index
        return min_index