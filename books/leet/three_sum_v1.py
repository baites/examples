# https://leetcode.com/problems/3sum/

class Solution(object):
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
        tmp = {}
        for i in range(len(nums)):
            tmp.setdefault(-nums[i], set()).add(i)
        result = []
        veto = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                value = nums[i] + nums[j]
                if value in tmp:
                    indexes = tmp[value] - set([i,j])
                    if len(indexes) > 0:
                        ntuple = (nums[i], nums[j], -value)
                        if ntuple not in veto:
                            result.append(ntuple)
                            self.add(veto, ntuple)
        return result

s = Solution().threeSum([0]*10000)
print(s)
