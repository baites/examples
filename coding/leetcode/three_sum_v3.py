# https://leetcode.com/problems/3sum/

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        cache = { nums[i]: i for i in range(len(nums)) }

        result = []
        size = len(nums)
        i1 = 0
        while i1 < size - 2:
            v1 = nums[i1]
            i2 = i1+1
            while i2 < size - 1:
                v2 = nums[i2]
                vsum = v1 + v2
                if (-vsum) in cache and cache[-vsum] > i2:
                    result.append((v1, v2, -vsum))
                i2 = cache[v2] + 1
            i1 = cache[v1] + 1
        return result

#s = Solution().threeSum([-1, 0, 1, 2, -1, -4])
s = Solution().threeSum([0,1,3,-1])
print(s)
