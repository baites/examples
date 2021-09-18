class Solution:
    def longestValidParentheses(self, s: str) -> int:

        size = len(s)

        # Dynamic program array
        # DP[i+1] is the size of the longest valid substring ending in i
        # DP[0] = 0 null string has zero-sized valid substrings
        # DP[1] = 0 one char strings has zero-sized valid substrings
        DP = [0 for _ in range(size+1)]

        # Loop over the string starting position 1
        # Elements with one char has not valid parehthesis
        for i in range(1,size):
            # First condition substring[size=i-1]()
            if s[i-1] == '(' and s[i] == ')':
                # Check between substring
                DP[i+1] = DP[i-1] + 2
            # Check for ..(longest_valid_substring[size=i-1])
            elif s[i-1-DP[i]] == '(' and s[i] == ')':
                DP[i+1] = DP[i-1-DP[i]] + DP[i] + 2
            else:
                DP[i+1] = DP[i]
        return DP[size]
