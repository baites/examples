class Solution:
    def reverse(self, x: int) -> int:
        s = bytearray(str(x).encode())
        l = 0 if x > 0 else 1
        r = len(s)-1
        while l < r:
            tmp = s[l]
            s[l] = s[r]
            s[r] = tmp
            l += 1
            r -= 1
        n = int(s.decode())
        if n > 2**31 or n < -2**31:
            return 0
        return n
