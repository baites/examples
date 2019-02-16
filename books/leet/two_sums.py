# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = [(nums[i], i) for i in range(len(nums))]
        nums.sort()
        i = 0
        j = len(nums) - 1
        twosum = nums[i][0] + nums[j][0]
        while twosum != target:
            if twosum < target:
                i += 1
            else:
                j -= 1
            twosum = nums[i][0] + nums[j][0]
        return [nums[i][1],nums[j][1]]

s = Solution().twoSum([2, 11, 15, 7], 9)
print(s)
