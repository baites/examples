class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        aux = 0
        probe = 0
        
        while probe < len(nums):
            if nums[probe] != 0:
                if aux != probe:
                    nums[aux] = nums[probe]
                aux += 1
            probe += 1
      
        if aux > 0:
            for i in range(aux, len(nums)):
                nums[i] = 0

        return nums