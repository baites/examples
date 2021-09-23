from bisect import bisect_left

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        # Sort nums values
        nums.sort()

        # Collect the size
        size = len(nums)

        # Define delta
        delta = None

        # 2D scan of the two of the values
        for i in range(size):
            for j in range(i+1, size):
                # Compute complement
                complement = target - nums[i] - nums[j]
                # Use binary search
                k = bisect_left(nums, complement, j+1, size)
                # If complement value is before the end of nums
                # and complement less that value reduces distance update
                if k < size and (delta is None or \
                    abs(complement - nums[k]) < abs(delta)):
                    delta = complement - nums[k]
                # If complement value is the end of nums use the last
                # value if is larger than j to avoid using a element of nums twice
                if k-1 > j and (delta is None or \
                    abs(complement - nums[k-1]) < abs(delta)):
                    delta = complement - nums[k-1]
        return target - delta
