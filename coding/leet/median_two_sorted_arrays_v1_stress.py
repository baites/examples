class Naive(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()
        size = len(nums)
        if size % 2 == 1:
            return nums[size//2]
        return 0.5*(nums[size//2-1] + nums[size//2])


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        size1 = len(nums1)
        size2 = len(nums2)
        size = size1 + size2
        nums = [0]*(size)
        i1 = 0; i2 = 0; i = 0
        while i1 < size1 or i2 < size2:
            if i1 == size1:
                nums[i] = nums2[i2]
                i2 += 1
            elif i2 == size2:
                nums[i] = nums1[i1]
                i1 += 1
            elif nums1[i1] < nums2[i2]:
                nums[i] = nums1[i1]
                i1 += 1
            else:
                nums[i] = nums2[i2]
                i2 += 1
            i += 1
        if size % 2 == 1:
            return nums[size//2]
        return 0.5*(nums[size//2-1] + nums[size//2])


import random
import time

size = 100000
maxv = 100

while 1:
    nums1 = [random.randint(-maxv,maxv) for i in range(size)]
    nums2 = [random.randint(-maxv,maxv) for i in range(size)]
    nums1.sort()
    nums2.sort()
    solution_time = time.time()

    start = time.time()
    naive = Naive().findMedianSortedArrays(nums1, nums2)
    naive_time = time.time()
    solution = Solution().findMedianSortedArrays(nums1, nums2)
    solution_time = time.time()
    speedup = (naive_time - start)/\
                (solution_time - naive_time)

    if naive == solution:
        print('naive = {}, solution = {} (x{})'.format(
            naive, solution, speedup
        ))
        print('ok')
    else:
        print('naive = {}, solution = {}'.format(naive, solution))
        print('bad')
        break
