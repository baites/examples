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
            for index in range(len(permutation)+1):
                injected_permutation = permutation[:index] + [num] + permutation[index:]
                injected_permutations.append(injected_permutation)
        return injected_permutations
