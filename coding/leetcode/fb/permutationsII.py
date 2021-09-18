class Solution:

    def permuteUnique(self, nums):

        if len(nums) == 1:
            return [nums]
        if len(nums) == 2:
            if nums[0] == nums[1]:
                return [nums]
            else:
                return [nums, [nums[1], nums[0]]]

        num = nums.pop()
        permutations = self.permuteUnique(nums)
        injected_permutations = set()
        for permutation in permutations:
            permutation.append(num)
            size = len(permutation)
            injected_permutations.add(tuple(permutation))
            for index in range(size-1):
                if permutation[size-index-1] == permutation[size-index-2]:
                    continue
                permutation[size-index-2], permutation[size-index-1] =\
                    permutation[size-index-1], permutation[size-index-2]
                injected_permutations.add(tuple(permutation))
        return [list(permutation) for permutation in injected_permutations]
