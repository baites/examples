class Solution:

    def permute(self, nums):

        if len(nums) == 1:
            return [nums]
        if len(nums) == 2:
            return [nums, [nums[1], nums[0]]]

        num = nums.pop()
        permutations = self.permute(nums)
        injected_permutations = []
        for permutation in permutations:
            permutation.append(num)
            size = len(permutation)
            injected_permutations.append(list(permutation))
            for index in range(size-1):
                permutation[size-index-2], permutation[size-index-1] =\
                    permutation[size-index-1], permutation[size-index-2]
                injected_permutations.append(list(permutation))
        return injected_permutations
