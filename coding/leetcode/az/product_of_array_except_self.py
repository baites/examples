class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)

        left = [0]*size
        right = [0]*size

        for i in range(len(nums)):
            if i == 0:
                left[0] = nums[0]
                right[size-1] = nums[-1]
                continue
            left[i] = left[i-1] * nums[i]
            right[size-i-1] = right[size-i] * nums[size-i-1]

        result = []
        for i in range(len(nums)):
            if i == 0:
                result.append(right[i+1])
            elif i == size-1:
                result.append(left[i-1])
            else:
                result.append(left[i-1]*right[i+1])
        return result
