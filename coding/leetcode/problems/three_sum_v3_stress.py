class Naive(object):
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
                            result.append(tuple(sorted(ntuple)))
                            self.add(veto, ntuple)
        return result

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
            i2 = i1 + 1
            while i2 < size - 1:
                v2 = nums[i2]
                vsum = v1 + v2
                if (-vsum) in cache and cache[-vsum] > i2:
                    result.append((v1, v2, -vsum))
                i2 = cache[nums[i2]] + 1
            i1 = cache[nums[i1]] + 1
        return result

#s = Solution().threeSum([-1, 0, 1, 2, -1, -4])
import random

size = 100
vrange = 10

while 1:
    nums = sorted([random.randint(-vrange, vrange) for i in range(size)])
    naive = set(Naive().threeSum(nums))
    solution = set(Solution().threeSum(nums))
    if naive == solution:
        print('input: {}'.format(nums))
        print('ok')
    else:
        print('input: {}'.format(nums))
        print('bad')
        print('s-n:', solution - naive)
        print('n-s:', naive - solution)
        print(naive)
        print(solution)
        break
