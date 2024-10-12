class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        # Sort intervals in increasing order by their start times
        intervals.sort()
        
        # Track the active end times in a min heap
        heap = []

        for start, end in intervals:
            # Check for events that may have ended before the current event started
            if heap and heap[0] < start:
                heapq.heappop(heap) # Eject the ended interval from the heap
            
            # Push the current end time into the heap
            heapq.heappush(heap, end)
        
        # Each overlapping interval left in the heap requires a unique group
        return len(heap)
