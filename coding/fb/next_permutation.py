class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Size of the problem
        size = len(nums)

        def swap(i, j):
            """Swap to elements of nums"""
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        # Reverse the nums
        def reverse(index):
            """Reverse nums from index"""
            subsize = size - index
            for i in range(subsize//2):
                swap(i+index, size-i-1)

        if size == 1:
            return [nums[0]]

        left = size - 1

        while left > 0 and nums[left-1] >= nums[left]:
            left -= 1

        if left == 0:
            reverse(left)
            return

        right = size - 1
        while right > left and nums[left-1] >= nums[right]:
            right -= 1

        swap(left-1, right)
        reverse(left)