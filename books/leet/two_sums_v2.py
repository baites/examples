
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp = { target - nums[i]: i for i in range(len(nums)) }
        for j in range(0,len(nums)):
            if nums[j] in tmp:
                i = tmp[nums[j]]
                if i != j:
                    return sorted([i,j])
        return None

s = Solution().twoSum([2, 7, 11, 15], 9)
print(s)
