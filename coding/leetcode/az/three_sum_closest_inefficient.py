class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        min_delta = None
        result = None

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    num_sum = nums[i] + nums[j] + nums[k]
                    delta = target - num_sum
                    if min_delta is None:
                        min_delta = abs(delta)
                        result = num_sum
                        continue
                    if abs(delta) < min_delta:
                        min_delta = abs(delta)
                        result = num_sum

        return result
