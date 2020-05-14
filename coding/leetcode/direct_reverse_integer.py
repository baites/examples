INT_MAX = 2**31
INT_MIN = -2**31

class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        sign = 1;
        if x < 0:
            x *= -1;
            sign = -1;
        while x != 0:
            pop = x % 10
            x //= 10
            if rev > INT_MAX//10 or rev == INT_MAX//10 and pop > 7:
                return 0
            if -rev < INT_MIN//10 or -rev == INT_MIN//10 and pop < -8:
                return 0
            rev = rev * 10 + pop
        return sign*rev
