from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Counter elements
        counters = Counter(nums)
        # Return largest element using a heap
        return heapq.nlargest(k, counters, key=counters.get)