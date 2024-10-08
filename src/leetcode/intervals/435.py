class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = 0
        intervals.sort(key = lambda x:x[1]) # Sort the intervals by end time
        prevEnd = intervals[0][1] # Default `prevEnd` to the end time of the first interval since they are sorted

        # Iterate over each interval after the first
        for start, end in intervals[1::]:
            if start < prevEnd: # If the start time is before the previous end time, the intervals are overlapping
                # Increment the counter
                # "Delete" the interval (don't update `prevEnd`) with the latest end time to avoid additional overlapping intervals
                result += 1
            else: # The intervals are not overlapping. Update `prevEnd`
                prevEnd = end

        return result
