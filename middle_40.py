class Solution:
    def insert(self, intervals, newInterval):
        result = []

        start, end = newInterval
        i = 0

        # 1. Add intervals that are completely before newInterval
        while i < len(intervals) and intervals[i][1] < start:
            result.append(intervals[i])
            i += 1

        # 2. Merge overlapping intervals
        while i < len(intervals) and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1

        result.append([start, end])

        # 3. Add remaining intervals
        while i < len(intervals):
            result.append(intervals[i])
            i += 1

        return result
