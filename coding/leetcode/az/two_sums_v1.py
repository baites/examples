class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Create target minus value to index map
        indexes = {}
        for index, value in enumerate(nums):
            indexes.setdefault(target-value, set()).add(index)

        # Loop over all the elements
        for index1, value in enumerate(nums):
            # Find a value that add to target
            if value in indexes:
                # Remove index1 (repeated element)
                if index1 in indexes[value]:
                    indexes[value].remove(index1)
                # Do not return same element
                if len(indexes[value]) == 0:
                    continue
                return [index1, indexes[value].pop()]
