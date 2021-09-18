class Solution:

    def findAnagrams(self, s: str, p: str) -> list[int]:

        def get_counters(s):
            counters = {}
            for c in s:
                counters[c] = counters.setdefault(c, 0) + 1
            return counters

        def update_counters(counters, add_char, remove_char):
            counters[add_char] = counters.setdefault(add_char, 0) + 1
            counters[remove_char] -= 1
            if counters[remove_char] == 0:
                del counters[remove_char]

        # Get size of the strings
        ssize = len(s)
        psize = len(p)

        # Check that string no smaller
        # than anagram target
        if ssize < psize:
            return []

        # indexes is placeholder for result
        indexes = []

        # Index to moving substrings of s
        index = 0

        # Create aux set to check for anagrams
        scounters = get_counters(s[:psize])
        pcounters = get_counters(p)

        while 1:
            # Check anagram
            if pcounters == scounters:
                indexes.append(index)
            if index+psize == ssize:
                break
            update_counters(scounters, s[index+psize], s[index])
            index += 1

        return indexes