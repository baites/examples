
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(nums) - 1
        twosum = nums[i] + nums[j]
        while twosum != target:
            if twosum < target:
                i += 1
            else:
                j -= 1
            twosum = nums[i] + nums[j]
        return [i,j]

s = Solution().twoSum([2, 7, 11, 15], 9)
print(s)
