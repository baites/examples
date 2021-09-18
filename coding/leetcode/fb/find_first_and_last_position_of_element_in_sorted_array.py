class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:

        def bisect_left(target):
            left = 0
            right = len(nums)
            while left < right:
                middle = (left+right)//2
                if nums[middle] < target:
                    left = middle + 1
                else:
                    right = middle
            if left < len(nums) and nums[left] == target:
                return left
            return -1

        def bisect_right(target):
            left = 0
            right = len(nums)
            while left < right:
                middle = (left+right)//2
                if nums[middle] <= target:
                    left = middle + 1
                else:
                    right = middle
            if left > 0 and nums[left-1] == target:
                return left-1
            return -1

        return bisect_left(target),bisect_right(target)
