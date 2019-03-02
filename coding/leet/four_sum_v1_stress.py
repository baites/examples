class Naive(object):
    def add(self, veto, ntuple):
        veto.add((ntuple[0], ntuple[1], ntuple[2]))

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        veto = set()
        for i1 in range(len(nums)):
            for i2 in range(i1+1, len(nums)):
                for i3 in range(i2+1, len(nums)):
                    for i4 in range(i3+1, len(nums)):
                        delta = target - nums[i1] - nums[i2] - nums[i3] - nums[i4]
                        if delta == 0:
                            tmplist = [nums[i1], nums[i2], nums[i3], nums[i4]]
                            tmplist.sort()
                            tmplist = tuple(tmplist)
                            if tmplist not in veto:
                                result.append(tmplist)
                                veto.add(tmplist)
        return result

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

#s = Solution().threeSum([-1, 0, 1, 2, -1, -4])
import random

size = 100
vrange = 100

while 1:
    target = random.randint(-vrange, vrange)
    nums = sorted([random.randint(-vrange, vrange) for i in range(size)])
    naive = set(Naive().fourSum(nums, target))
    solution = set(Solution().fourSum(nums, target))
    if naive == solution:
        print('input: {}, target = {}'.format(nums, target))
        print('ok')
    else:
        print('input: {}, target = {}'.format(nums, target))
        print('bad')
        print('s-n:', solution - naive)
        print('n-s:', naive - solution)
        print(naive)
        print(solution)
        break
