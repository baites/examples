
# Add any extra import statements you may need here
from heapq import heappush, heappop

# Add any helper functions you may need here


def findMaxProduct(arr):
    # Write your code here

    output = []
    heap = []

    for value in arr:
        heappush(heap, value)
        if len(heap) < 3:
            output.append(-1)
        elif len(heap) == 3:
            output.append(heap[0] * heap[1] * heap[2])
        else:
            heappop(heap)
            output.append(heap[0] * heap[1] * heap[2])

    return output
