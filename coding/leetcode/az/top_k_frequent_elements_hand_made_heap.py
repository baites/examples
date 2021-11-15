import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        heap = []

        def parent(index):
            return (index-1)//2

        def left(index):
            return 2*index+1

        def right(index):
            return 2*index+2

        def sift_up(index):
            # get initial parent
            parent_index = parent(index)
            while index > 0 and heap[parent_index][0] > heap[index][0]:
                heap[parent_index], heap[index] = heap[index], heap[parent_index]
                index = parent_index
                parent_index = parent(index)

        def sift_down(index):
            # get all indexes
            min_index = index
            left_index = left(index)
            right_index = right(index)
            # check heap condition to the left
            if left_index < len(heap) and \
                heap[left_index][0] < heap[index][0]:
                min_index = left_index
            # check heap condition to the right
            if right_index < len(heap) and \
                heap[right_index][0] < heap[min_index][0]:
                min_index = right_index
            # Swap min_index if is not index
            if index != min_index:
                heap[index], heap[min_index] = heap[min_index], heap[index]
                sift_down(min_index)

        def insert(node):
            # add element to the heap
            heap.append(node)
            # initial index is tail of heap
            index = len(heap)-1
            # siftup
            sift_up(index)

        def pop():
            # pop last node from heap
            node = heap.pop()
            # replace the root node
            heap[0] = node
            # sift down root
            sift_down(0)

        counters = {}
        for num in nums:
            counters[num] = counters.setdefault(num, 0) + 1

        for key, value in counters.items():
            insert((value, key))

        if len(heap) > k:
            for _ in range(len(heap)-k):
                pop()

        return [key for value, key in heap]