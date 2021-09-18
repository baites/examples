class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        def merge2(interval1, interval2):
            if interval1[1] < interval2[0] or\
                interval2[1] < interval1[0]:
                return None
            return [
                min(interval1[0],interval2[0]),
                max(interval1[1],interval2[1])
            ]

        intervals.sort()

        # Placeholder for solution
        result = [intervals[0]]

        # Index to intervals list
        index = 1

        # Looping throughout intervals
        while index < len(intervals):
            interval = merge2(result[-1], intervals[index])
            if interval is None:
                result.append(intervals[index])
            else:
                result[-1] = interval
            index += 1

        return result