
from heapq import heappush, heappop

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        # List to place the heap
        heap = []

        # Loop over the points
        for point in points:
            # Compute the distance
            distance = point[0]**2 + point[1]**2
            # Push to the heap
            heappush(heap, (distance, point))

        # Compose result
        closest_points = []
        for _ in range(k):
            distance, point = heappop(heap)
            closest_points.append(point)

        return closest_points