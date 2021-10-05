class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Count letters as anagram signature
        def count_letters(word):
            offset = ord('a')
            counters = [0]*26
            for letter in word:
                counters[ord(letter) - offset] += 1
            return counters

        groups = {}
        for word in strs:
            counters = count_letters(word)
            groups.setdefault(tuple(counters), []).append(word)

        return groups.values()
