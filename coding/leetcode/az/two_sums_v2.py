class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Create target minus value to index map
        indexes = {}
        for index, value in enumerate(nums):
            if value in indexes:
                return [indexes[value], index]
            indexes[target-value] = index