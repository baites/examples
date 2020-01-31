
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


class Solution(object):

    def _compute_polyhashes(self, string):
        """Evaluate the forward and backward polyhashes."""
        # Setting hashing cache
        length = len(string)
        forward = [0]*(length + 1)
        backward = [0]*(length + 1)
        poly = [1]*(length + 1)
        # Computing hashes
        for i in range(length):
            c = ord(string[i])
            forward[i+1] = (forward[i] + c*poly[i]) % self._prime
            backward[i+1] = (self._base*backward[i] + c) % self._prime
            poly[i+1] = (poly[i] * self._base) % self._prime
        return forward, backward, poly

    def __init__(self):
        """Contructor."""
        #self._prime = 2**61-1
        self._prime = 10**9+9
        #self._prime = 331
        #self._base = random.randint(1, self._prime - 1)
        self._base = 31

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
        if size == 0:
            return ''
        # Compute hash strings
        forward, backward, poly = self._compute_polyhashes(string)
        # Search for a palindrome substring
        for length in range(size, 1, -1):
            for offset in range(size - length + 1):
                fhash = (
                    forward[length+offset]-forward[offset]
                )%self._prime
                bhash = (poly[offset]*backward[length+offset]) % self._prime
                bhash -= (poly[length+offset]*backward[offset]) % self._prime
                bhash %= self._prime
                if fhash == bhash and\
                    self._isPalindrome(string, offset, offset+length-1):
                    return length
        return 1


import random
import string
import time

size = 1000
tries = 20
#alphabet = string.ascii_lowercase
alphabet = ['a']+['b']*80#,'c']

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
