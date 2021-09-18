class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        ssize = len(s)
        psize = len(p)

        def match(sindex, pindex):  # index of the s  # index of the p
            # Implement no partial matching
            # Check if at the end of the pattern
            if pindex == psize:
                # Return if you are at then of the the string
                # If it does it means a match!
                return sindex == ssize

            # A char match is the result of the following conditions
            #   * s index is not len(s) or empty string
            #   * pattern char is the same as string char or
            #   * pattern char is a .
            cmatch = sindex < ssize and p[pindex] in (s[sindex], ".")

            # If a "CHAR ELEMENT"* pattern is found, a match is then
            #   * check match by ignoring the current and next elements
            #     of the pattern for the whole string
            #   * check char match and see if rest of the
            #     string match pattern without ignoring the current
            #     and next elements of the pattern
            if pindex + 1 < psize and p[pindex + 1] == "*":
                return match(sindex, pindex + 2) or (
                    cmatch and match(sindex + 1, pindex)
                )
            # Alternative check if char match and
            # next string and pattern suffix match
            else:
                return cmatch and match(sindex + 1, pindex + 1)

        return match(0, 0)
