class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        cache = { nums[i]: i for i in range(len(nums)) }

        result = []
        size = len(nums)
        i1 = 0
        while i1 < size - 3:
            v1 = nums[i1]
            i2 = i1+1
            while i2 < size - 2:
                v2 = nums[i2]
                i3 = i2 + 1
                while i3 < size - 1:
                    v3 = nums[i3]
                    delta = target - v1 - v2 - v3
                    if delta in cache and cache[delta] > i3:
                        result.append((v1, v2, v3, delta))
                    i3 = cache[v3] + 1
                i2 = cache[v2] + 1
            i1 = cache[v1] + 1
        return result

#s = Solution().fourSum([1, 0, -1, 0, -2, 2], 1)
s = Solution().fourSum([0]*100000, 0)

print(s)
