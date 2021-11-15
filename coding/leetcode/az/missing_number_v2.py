class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_set = set(range(len(nums)+1))
        num_set = set(nums)
        return (total_set - num_set).pop()
