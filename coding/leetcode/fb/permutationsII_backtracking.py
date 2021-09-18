class Solution:

    def permuteUnique(self, nums):

        result = []

        def count():
            counters = {}
            for num in nums:
                counters[num] = counters.setdefault(num, 0) + 1
            return counters

        def backtrack(counters, comb=[]):

            if len(comb) == len(nums):
                result.append(list(comb))
                return

            for num in counters:
                if counters[num] > 0:
                    comb.append(num)
                    counters[num] -= 1
                    backtrack(counters, comb)
                    comb.pop()
                    counters[num] += 1

        backtrack(count())

        return result