class Solution:

    def permute(self, nums):

        result = []

        def backtrack(elems, comb=[]):

            if len(comb) == len(nums):
                result.append(list(comb))
                return

            for num in nums:
                if num in elems:
                    comb.append(num)
                    elems.remove(num)
                    backtrack(elems, comb)
                    comb.pop()
                    elems.add(num)

        backtrack(set(nums))

        return result