"""Solution to study!"""

import functools


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        """

        . ---> single character

        * --> 0 or more proceeding characters



        ''
        s*
        """

        n, m = len(s), len(p)

        @functools.lru_cache(None)
        def dp(i, j):
            if i == n:
                if j + 1 < m and p[j + 1] == "*":
                    return dp(i, j + 2)
                else:
                    return j == m
            if j == m:
                return i == n

            # cases, if p[j + 1] == '*'
            if j + 1 < m and p[j + 1] == "*":
                """
                abadfasf
                i
                c*a
                  j
                """
                if s[i] == p[j] or p[j] == ".":
                    # match 0 preceeding,
                    return dp(i + 1, j + 2) or dp(i + 1, j) or dp(i, j + 2)
                else:
                    return dp(i, j + 2)
            elif s[i] == p[j] or p[j] == ".":
                return dp(i + 1, j + 1)
            else:
                return False

        return dp(0, 0)