
class Naive(object):

    def __init__(self):
        self.count = 0

    def isPalindrome(self, s, m, n):
        while n > m:
            self.count += 1
            if s[m] != s[n]:
                return False
            m += 1
            n -= 1
        return True

    def longestPalindrome(self, s):
        r = len(s)
        if r <= 1:
            return r
        M = 1
        for m in range(r):
            for n in range(m+1, r):
                if self.isPalindrome(s, m, n):
                    length = n-m+1
                    if length > M:
                        M = n-m+1
                        #palin = s[i:j+1]
        return M#, palin

import heapq

class Solution(object):

    def __init__(self):
        self.count = 0

    def isPalindrome(self, s, m, n):
        while n > m:
            self.count += 1
            if s[m] != s[n]:
                return False
            m += 1
            n -= 1
        return True

    def longestPalindrome(self, s):
        r = len(s)
        if r <= 1:
            return r
        x = 256
        p = 2**61-1
        heap = []
        for m in range(r):
            y = 1
            F = ord(s[m])
            B = ord(s[m])
            for n in range(m+1, r):
                y = (y * x) % p
                F = (F + ord(s[n])*y) % p
                B = (x*B + ord(s[n])) % p
                if F == B:
                    heapq.heappush(heap, (-(n-m+1), m, n))
        while len(heap) > 0:
            l, m, n  = heapq.heappop(heap)
            print(-l, m, n)
            if self.isPalindrome(s, m, n):
                return -l
        return 1


import random
import string
import time

size = 2000
tries = 10
alphabet = string.ascii_lowercase
#alphabet = ['a']

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
        print('test = {}, ref = {} (x{})'.format(
            test, ref, speedup
        ))
        print(naive.count, solution.count)
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
