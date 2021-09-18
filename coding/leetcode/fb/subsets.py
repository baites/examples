class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:

        def product(subsets, element):
            """Make all possible subsets by concatenation"""
            result = []
            for subset in subsets:
                result.append(subset+[element])
            return result

        def powerset(index):
            """Get all subsets in a substrin [:index]"""

            if index == 0:
                return [[]]

            # Partial subset for substring [:index]
            partial_subsets = powerset(index-1)

            # Add previous subsets, plus new combination and the full set
            power = partial_subsets + product(partial_subsets, nums[index-1])

            return power

        return powerset(len(nums))