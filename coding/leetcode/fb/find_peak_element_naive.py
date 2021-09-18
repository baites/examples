class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        size = len(nums)

        for i in range(size):
            if i == 0 and nums[i] > nums[i+1]:
                return i
            elif i == size-1 and nums[i-1] < nums[i]:
                return i
            elif nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                return i

        return -1