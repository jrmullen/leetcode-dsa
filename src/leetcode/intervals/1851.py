class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        result = [0] * len(queries) # Pre-populate the `result` with a value of 0
        
        # Sort the intervals so they can be compared in chronological order
        intervals.sort()

        # Sort the queries so they can be processed in chronological order
        # Convert the values into a tuple (query, index) to preserve index values for writing to the correct element in `result`
        queries = sorted((q, i) for i, q in enumerate(queries))

        heap = [] # Min heap with values of tuple (interval length, end time)
        interval = 0 # Track the interval
        for q, i in queries:
            # Iterate over each interval has a start time <= `q` push it onto the heap
            while interval < len(intervals) and intervals[interval][0] <= q:
                start, end = intervals[interval]
                heapq.heappush(heap, (end - start + 1, end))
                interval += 1

            # Remove all intervals from the heap that have end times that are before `q`
            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            # Add the smallest length interval to the `result` list
            result[i] += heap[0][0] if heap else -1
        
        return result
