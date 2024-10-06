class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort() # Sort the intervals in ascending order

        interval = intervals[0]
        for i in range(1, len(intervals)):
            currentStart, currentEnd = interval
            nextStart, nextEnd = intervals[i]

            # If the intervals are overlapping, merge them and iterate again to check if the next interval is overlapping
            if currentEnd >= nextStart:
                interval = [min(currentStart, nextStart), max(currentEnd, nextEnd)]
            else:
                # There is no overlap, so add the `interval` to the result list and move the pointer forward
                result.append(interval)
                interval = intervals[i]

        # Add the interval from the final iteration to the `result` and return
        result.append(interval)
        return result
