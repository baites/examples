class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:

        intervals.sort()

        # Placeholder for solution
        result = [intervals[0]]

        # Index to intervals list
        index = 1

        # Looping throughout intervals
        while index < len(intervals):
            if result[-1][1] < intervals[index][0]:
                result.append(intervals[index])
            else:
                result[-1] = [result[-1][0], max(result[-1][1],intervals[index][1])]
            index += 1

        return result