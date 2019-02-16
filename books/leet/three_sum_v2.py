# https://leetcode.com/problems/3sum/

class Solution(object):
    def get(self, nums, i):
        if i >= len(nums)-1:
            return i
        while i+1 < len(nums) and\
            nums[i] == nums[i+1]:
            i += 1
        return i

    def add(self, veto, ntuple):
        veto.add((ntuple[0], ntuple[1], ntuple[2]))
        veto.add((ntuple[2], ntuple[0], ntuple[1]))
        veto.add((ntuple[1], ntuple[2], ntuple[0]))
        veto.add((ntuple[1], ntuple[0], ntuple[2]))
        veto.add((ntuple[2], ntuple[1], ntuple[0]))
        veto.add((ntuple[0], ntuple[2], ntuple[1]))

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        tmp = {}
        for i in range(len(nums)):
            tmp.setdefault(-nums[i], set()).add(i)
        result = []
        veto = set()
        i = 0
        while i < len(nums):
            j = self.get(nums, i+1)
            while j < len(nums):
                value = nums[i] + nums[j]
                if value in tmp:
                    indexes = tmp[value] - set([i,j])
                    if len(indexes) > 0:
                        ntuple = (nums[i], nums[j], -value)
                        if ntuple not in veto:
                            result.append(ntuple)
                            self.add(veto, ntuple)
                j = self.get(nums, j+1)
            i += 1
        return result

s = Solution().threeSum([-1, 0, 1, 2, -1, -4])
#s = Solution().threeSum([0]*1000)
print(s)
