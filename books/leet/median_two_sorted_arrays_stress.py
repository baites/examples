class Naive1(object):
    def findMedianSortedArrays(self, nums1, nums2):
        nums = nums1 + nums2
        nums.sort()
        size = len(nums)
        if size % 2 == 1:
            return nums[size//2]
        return 0.5*(nums[size//2-1] + nums[size//2])


class Naive2(object):
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

nums1 = [1, 3]
nums2 = [2]
#nums1 = [1, 2]
#nums2 = [3, 4]

naive1 = Naive1().findMedianSortedArrays(nums1, nums2)
print(naive1)

naive2 = Naive2().findMedianSortedArrays(nums1, nums2)
print(naive2)
