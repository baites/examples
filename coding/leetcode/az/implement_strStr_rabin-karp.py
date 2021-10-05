class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # Mersenne prime
        # https://en.wikipedia.org/wiki/Mersenne_prime
        prime = 2^31-1
        base = 31

        h_size = len(haystack)
        n_size = len(needle)

        def get_hash(word):
            value = 0
            power = 1
            for char in word:
                value = (value + ord(char) * power) % prime
                power = (power * base) % prime
            return value

        def get_haystack_hashes():
            # Set array for substring hashes
            # It needs to be same size as pattern
            values = [0]*(h_size - n_size + 1)
            # Set last array value of the last substring
            values[-1] = get_hash(haystack[h_size - n_size:])
            # Compute modular power
            power = 1
            for i in range(n_size):
                power = (power * base) % prime
            # Derive now the other hashes
            for i in range(h_size - n_size - 1, -1, -1):
                values[i] = (
                    ord(haystack[i]) + base * values[i+1] - power * ord(haystack[i + n_size])
                ) % prime
            return values


        if len(haystack) < len(needle):
            return -1
        if len(needle) == 0:
            return 0

        n_hash = get_hash(needle)
        h_hashes = get_haystack_hashes()

        for i in range(h_size - n_size + 1):
            if n_hash != h_hashes[i]:
                continue
            if needle == haystack[i:i + n_size]:
                return i

        return -1