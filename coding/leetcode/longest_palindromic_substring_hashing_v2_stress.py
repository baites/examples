
import random

class Naive(object):

    def _isPalindrome(self, string, begin, end):
        """Verify if substring is a palindrome."""
        while end > begin:
            if string[begin] != string[end]:
                return False
            begin += 1
            end -= 1
        return True

    def longestPalindrome(self, string):
        """Solve the problem."""

        # Get string size
        size = len(string)

        # Search for a palindrome substring
        for length in range(size, 1, -1):
            for offset in range(size - length + 1):
                if self._isPalindrome(string, offset, offset+length-1):
                    #return string[offset:offset+length]
                    return length
        return string[0]


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
        #self._prime = 2**61-1
        #self._base = random.randint(1, self._prime - 1)
        self._prime = 271
        self._base = 31
        self._string = string
        self._length = len(string)
        self._offset = 0
        self._counter = 0
        self._compute_polyhashes()

    @property
    def hashes(self):
        return self._hashes

    def _isPalindrome(self):
        """Verify if substring is a palindrome."""
        self._counter += 1
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
        self._poly = poly
        for length in range(size, 1, -1):
            for offset in range(size - length + 1):
                if offset > 0:
                    poly.shift()
                if poly.isPalindrome:
                    #return string[offset:offset+length]
                    return length
            poly.pop()
        return 1


import random
import string
import time

size = 1000
tries = 10
alphabet = string.ascii_lowercase
alphabet = ['a']+['b']*40#,'c']

agg_ref_time = 0
agg_test_time = 0

for i in range(tries):

    pop = ''.join(random.choices(alphabet, k=size))

    naive = Naive()
    solution = Solution()

    start = time.time()
    ref = naive.longestPalindrome(pop)
    ref_time = time.time()
    test = solution.longestPalindrome(pop)
    test_time = time.time()
    speedup = (ref_time - start)/\
                (test_time - ref_time)
    agg_ref_time += ref_time - start
    agg_test_time += test_time - ref_time

    if test == ref:
        print(ref_time - start, test_time - ref_time)
        print('test = {}, ref = {} (x{})'.format(
            test, ref, speedup
        ))
        print('ok')
    else:
        print(pop)
        print('test = {}, ref = {}'.format(
            test, ref
        ))
        print('bad')
        break

print('Agg ref time {}'.format(agg_ref_time))
print('Agg test time {}'.format(agg_test_time))
print('Agg speedup x{}'.format(agg_ref_time/agg_test_time))
