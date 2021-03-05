
#import random

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
            #d = ord(string[length-1-i])
            forward[i+1] = (forward[i] + c*poly[i]) % self._prime
            backward[i+1] = (self._base*backward[i] + c) % self._prime
            poly[i+1] = (poly[i] * self._base) % self._prime
        return forward, backward, poly

    def __init__(self):
        """Contructor."""
        #self._prime = 2**61-1
        self._prime = 10**9+9
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
                    return string[offset:offset+length]
        return string[0]

s = 'abacdfgdcaba'
print(Solution().longestPalindrome(s))

# Runtime: 5772 ms, faster than 14.90% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Longest Palindromic Substring.
