from heapq import heappush, heappop, heappushpop

class MedianFinder:

    def __init__(self):
        self._max_heap = []
        self._min_heap = []


    def addNum(self, num: int) -> None:

        if len(self._max_heap) != len(self._min_heap):
            heappush(self._min_heap, -heappushpop(self._max_heap, -num))
        else:
            heappush(self._max_heap, -heappushpop(self._min_heap,  num))


    def findMedian(self) -> float:
        # Median
        if len(self._max_heap) > len(self._min_heap):
            return -self._max_heap[0]
        # else return
        return (self._min_heap[0]-self._max_heap[0])/2