
# Add any extra import statements you may need here
from heapq import heappush, heappop, heapify

# Add any helper functions you may need here


def maxCandies(arr, k):
    # Write your code here
    # Making all array value negative
    # to create a maxheap
    arr = [-v for v in arr]
    # Heapify the arr
    heapify(arr)

    # Number of candies
    count = 0

    # Minheap root is zero no more candy
    # Running out of time no more candy
    while arr[0] < 0 and k > 0:
        value = heappop(arr)
        count += -value
        heappush(arr, -(-value // 2))
        k -= 1

    print()
    return count
