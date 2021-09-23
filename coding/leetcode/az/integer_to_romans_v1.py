from bisect import bisect_right

class Solution:
    def intToRoman(self, num: int) -> str:

        integers = [
            1, 4, 5, 9, 10,
            40, 50, 90, 100,
            400, 500, 900, 1000
        ]

        romans = [
            "I", "IV", "V", "IX", "X",
            "XL", "L", "XC", "C",
            "CD", "D", "CM", "M"
        ]

        result = ''
        index = len(integers)

        while num > 0:
            # All values in [0, index]
            # are larger than num
            index = bisect_right(integers, num, 0, index)
            result += romans[index-1]
            num -= integers[index-1]

        return result