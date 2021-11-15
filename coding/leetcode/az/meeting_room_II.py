from heapq import heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        def overlap(i1, i2):
            """Detect overlap intervals"""
            if i1[1] <= i2[0] or i2[1] <= i1[0]:
                return False
            return True

        # sort intervals based on start and end times in reverse order
        intervals.sort(key = lambda x: x[0], reverse=True)
        print(intervals)

        # number of rooms
        max_rooms = 0
        room_heap = []

        while len(intervals) > 0:
            # pop the first meeting interval
            start, end = intervals.pop()
            # is no used room or
            # make available room with meeting done before interval
            while len(room_heap) > 0 and start >= room_heap[0]:
                heappop(room_heap)
            # add the
            heappush(room_heap, end)
            max_rooms = max(max_rooms, len(room_heap))
        return max_rooms