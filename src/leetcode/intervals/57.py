class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        
        for i in range(len(intervals)):
            newStart, newEnd = newInterval
            currentStart, currentEnd = intervals[i]
            if newEnd < currentStart: # The new interval comes before the existing interval
                result.append(newInterval)
                return result + intervals[i:] # All remaining intervals are larger than the new interval, so add them to the `result` list and return
            elif newStart > currentEnd: # The new interval comes after the existing interval
                # Add the existing interval and then iterate to see if there is an overlap with the next
                result.append(intervals[i])
            else: # The intervals are overlapping, so they must be combined
                # The new interval is merged with the existing interval. Keep the smallest start and largest end
                newInterval = [min(newStart, currentStart), max(newEnd, currentEnd)]
        
        # If the `intervals` list is empty or the new interval ended up as the last
        result.append(newInterval)
        return result
