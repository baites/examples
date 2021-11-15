from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self._max_heap = []
        self._min_heap = []


    def addNum(self, num: int) -> None:
        # push to the heap max
        heappush(self._max_heap, -num)
        # push max value to min heap
        heappush(self._min_heap, -heappop(self._max_heap))
        # if out of balance
        if len(self._max_heap) < len(self._min_heap):
            # pop from max heap and push to min heap
            heappush(self._max_heap, -heappop(self._min_heap))


    def findMedian(self) -> float:
        # Median
        if len(self._max_heap) > len(self._min_heap):
            return -self._max_heap[0]
        # else return
        return (self._min_heap[0]-self._max_heap[0])/2