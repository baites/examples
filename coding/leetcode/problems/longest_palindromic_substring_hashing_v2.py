
import random

class PolyHashPolidrome:
    """Define a polyhash polidrome object."""

    def _compute_polyhashes(self):
        """Evaluate the forward and backward polyhashes."""
        forward = ord(self._string[0])
        backward = ord(self._string[0])
        poly = [1]*self._length
        for i in range(1, self._length):
            c = ord(self._string[i])
            poly[i] = (poly[i-1] * self._base) % self._prime
            forward = (forward + c*poly[i]) % self._prime
            backward = (self._base*backward + c) % self._prime
        self._hashes_zero = (forward, backward)
        self._hashes = (forward, backward)
        self._poly = poly

    def __init__(self, string):
        """Contructor."""
        self._prime = 2**61-1
        self._base = random.randint(1, self._prime - 1)
        self._string = string
        self._length = len(string)
        self._offset = 0
        self._compute_polyhashes()

    @property
    def hashes(self):
        return self._hashes

    def _isPalindrome(self):
        """Verify if substring is a palindrome."""
        begin = self._offset
        end = self._length+self._offset-1
        while end > begin:
            if self._string[begin] != self._string[end]:
                return False
            begin += 1
            end -= 1
        return True

    @property
    def isPalindrome(self):
        """Return true if substring is a palindrome."""
        forward, backward = self._hashes
        if forward != backward:
            return False
        return self._isPalindrome()

    @staticmethod
    def _divide(dividend, divisor, module):
        """Implement modular division."""
        dividend %= module
        inverse = pow(divisor, module-2, module)
        return (inverse*dividend) % module

    def pop(self):
        """Recompute hashes after poping last char."""
        forward, backward = self._hashes_zero
        self._length -= 1
        poly = self._poly[self._length]
        char = ord(self._string[self._length])
        forward = (forward - char * poly) % self._prime
        #backward = ((backward - char)//self._base) % self._prime
        backward = self._divide(backward - char, self._base, self._prime)
        self._hashes_zero = forward, backward
        self._hashes = forward, backward
        self._offset = 0

    def shift(self):
        """Recompute hashes shifting substring."""
        forward, backward = self._hashes
        poly = self._poly[self._length-1]
        prev = ord(self._string[self._offset])
        next = ord(self._string[self._length+self._offset])
        #forward = ((forward - prev)//self._base + next * poly) % self._prime
        forward = (self._divide(forward - prev, self._base, self._prime) + (next * poly) % self._prime) % self._prime
        backward = (self._base*(backward - prev * poly) + next) % self._prime
        self._hashes = forward, backward
        self._offset += 1


class Solution(object):

    def longestPalindrome(self, string):
        offset = 0
        size = len(string)
        poly = PolyHashPolidrome(string)
        for length in range(size, 1, -1):
            for offset in range(size - length + 1):
                if offset > 0:
                    poly.shift()
                if poly.isPalindrome:
                    return string[offset:offset+length]
            poly.pop()
        return string[0]


#s = 'ccaab'

#poly = PolyHashPolidrome(s)
#poly.pop()
#poly.pop()
#poly.pop()
#poly.pop()
#poly.pop()
#print(poly.hashes)

#s = 'ccaa'
#s = 'aa'
#polyA = PolyHashPolidrome(s)
#print(polyA.hashes)

#poly.shift()
#poly.shift()
#poly.shift()
#print(poly.hashes)
#print(poly.isPalindrome)

#s = 'caab'
#s = 'aa'
#poly = PolyHashPolidrome(s)
#print(poly.hashes)

s = 'ccbac'
print(Solution().longestPalindrome(s))
