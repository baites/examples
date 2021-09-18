class Solution:
    def numDecodings(self, s: str) -> int:

        # array to store subproblems
        dp = [0]*(len(s)+1)

        # initial state
        dp[0] = 1

        # always string of len 1 as 1 except
        # when its value is zero
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(dp)):
            # check if single digit can be decoded
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            val = int(s[i-2:i])
            if val >= 10 and val <= 26:
                dp[i] += dp[i-2]
        return dp[len(s)]