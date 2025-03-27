class Solution:
    def checkValidCuts(self, n: int, rectangles: list[list[int]]) -> bool:
        # Split into x- and y-axis pairs
        x = [(start, end) for start, _, end, _ in rectangles]
        y = [(start, end) for _, start, _, end in rectangles]

        # Sort the pairs in ascending order
        x.sort()
        y.sort()

        # Count the number of regions for a list of intervals
        def countRegions(intervals):
            regions = 0 # Track the number of regions that can be created given the list of `intervals`
            last_end = intervals[0][0] # Default to the start time of the first interval
            for start, end in intervals:
                if start >= last_end: # If there is a gap between the `last_end` and the `start`, a cut can be made
                    regions += 1
                last_end = max(last_end, end) # Update `last_end` with the larger end time
            return regions
        
        # If either the x- or y-axis have 3 or more regions 2 clean cuts can be made 
        return countRegions(x) >= 3 or countRegions(y) >= 3
