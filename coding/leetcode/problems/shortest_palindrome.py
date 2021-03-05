class Solution:

    def _isPalindrome(self, string, begin, end):
        """Verify if substring is a palindrome."""
        while end > begin:
            if string[begin] != string[end]:
                return False
            begin += 1
            end -= 1
        return True

    def shortestPalindrome(self, string: str) -> str:

        length = len(string)

        if length < 2:
            return string

        prime = 10**9+9
        base = 31

        forward = 0
        backward = 0
        poly = 1

        collisions = []

        for i in range(length):
            c = ord(string[i])
            forward = (forward + poly * c) % prime
            backward = (base * backward + c) % prime
            if forward == backward:
                collisions.append(i)
            poly = (poly * base) % prime

        while len(collisions) > 1:
            end = collisions.pop()
            if self._isPalindrome(string, 0, end):
                return string[length-1:end:-1]+string
        return string[:0:-1]+string

#s = 'bcd'
#print(Solution().shortestPalindrome(s))

# Runtime: 40 ms, faster than 85.74% of Python3 online submissions for Shortest Palindrome.
# Memory Usage: 13.6 MB, less than 14.29% of Python3 online submissions for Shortest Palindrome.
