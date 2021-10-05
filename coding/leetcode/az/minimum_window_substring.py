class Solution:
    def minWindow(self, s: str, t: str) -> str:

        def count_letters(word):
            counters = {}
            for letter in word:
                counters[letter] = counters.setdefault(letter, 0) + 1
            return counters

        if not t or not s:
            return ''

        counters = count_letters(t)

        l, r = 0, 0
        formed = 0
        needed = len(counters)
        window = {}
        ans = float('inf'), None, None

        while r < len(s):

            letter = s[r]
            window[letter] = window.get(letter, 0) + 1

            if letter in counters and window[letter] == counters[letter]:
                formed += 1

            while l <= r and formed == needed:
                letter = s[l]

                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                window[letter] -= 1
                if letter in counters and window[letter] < counters[letter]:
                    formed -= 1
                l += 1

            r += 1

        return "" if ans[0] == float('inf') else s[ans[1]: ans[2]+1]