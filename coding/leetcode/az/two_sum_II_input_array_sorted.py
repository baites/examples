class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        size = len(numbers)

        for index1, number in enumerate(numbers):
            remaining = target - number
            index2 = bisect.bisect_left(numbers, remaining, index1+1, size)
            if index2 < size and numbers[index2] == remaining:
                return [index1+1, index2+1]

        return []
