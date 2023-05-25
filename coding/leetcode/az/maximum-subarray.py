class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Get nums size
        size = len(nums)
        # Dynamic programming
        dp = [[0]*(size-i) for i in range(size)]

        # Max value
        max_sum = nums[0]

        # Loop over every ith initial position
        for i in range(size):
            # Set initial value
            dp[i][0] = nums[i]
            max_sum = max(max_sum, dp[i][0])
            # Loop over the different sizes
            for j in range(1, size-i):
                dp[i][j] = dp[i][j-1] + nums[i+j]
                max_sum = max(max_sum, dp[i][j])

        return max_sum
