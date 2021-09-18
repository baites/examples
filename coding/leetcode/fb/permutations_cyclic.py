class Solution:

    def permute(self, nums):

        if len(nums) == 1:
            return [nums]
        if len(nums) == 2:
            return [nums, [nums[1], nums[0]]]

        num = nums.pop()
        permutations = self.permute(nums)
        cyclic_permutations = []
        for permutation in permutations:
            permutation.append(num)
            size = len(permutation)
            for cycle in range(size):
                cyclic_permutation = [
                    permutation[(i+cycle)%size] for i in range(size)
                ]
                cyclic_permutations.append(cyclic_permutation)
        return cyclic_permutations
